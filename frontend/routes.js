/* ComplianceForge — une URL par page : https://complianceforge.test/<page> */
(function () {
    "use strict";

    if (window.__cfRoutesInstalled) {
        return;
    }
    window.__cfRoutesInstalled = true;

    const PAGES = [
        "dashboard", "organisation", "profil", "registre", "formulaires",
        "conformite", "risques", "incidents", "documents"
    ];

    const USER_PAGES = {
        "mon-profil": "afficherMonProfil",
        "parametres": "afficherParametres",
        "securite": "afficherSecurite"
    };

    let applying = false;
    let done = false;
    let intended = null;
    let timer = null;

    const locked = () => document.body.classList.contains("cf-auth-locked");

    function segment() {
        return location.pathname.replace(/^\/+|\/+$/g, "").split("/")[0].toLowerCase();
    }

    function setUrl(path) {
        if (applying || location.pathname === path) {
            return;
        }
        history.pushState({}, "", path);
    }

    function applyRoute() {
        const seg = segment();
        applying = true;
        try {
            if (USER_PAGES[seg] && typeof window[USER_PAGES[seg]] === "function") {
                window[USER_PAGES[seg]]();
            } else if (PAGES.includes(seg) && typeof window.navigate === "function") {
                window.navigate(seg);
            } else {
                if (typeof window.navigate === "function") {
                    window.navigate("dashboard");
                }
                history.replaceState({}, "", "/dashboard");
            }
        } catch (error) {
            console.warn("[ComplianceForge] Route non appliquée :", error);
        }
        setTimeout(function () { applying = false; }, 150);
    }

    /* Pages principales : window.navigate(page) */
    function wrapAll() {
        if (typeof window.navigate === "function" && !window.navigate.__cfRoute) {
            const original = window.navigate;
            const wrapped = function (page) {
                const result = original.apply(this, arguments);
                if (typeof page === "string" && PAGES.includes(page)) {
                    setUrl("/" + page);
                }
                return result;
            };
            wrapped.__cfRoute = true;
            window.navigate = wrapped;
        }

        Object.keys(USER_PAGES).forEach(function (path) {
            const name = USER_PAGES[path];
            const original = window[name];
            if (typeof original === "function" && !original.__cfRoute) {
                const wrapped = function () {
                    const result = original.apply(this, arguments);
                    setUrl("/" + path);
                    return result;
                };
                wrapped.__cfRoute = true;
                window[name] = wrapped;
            }
        });
    }

    wrapAll();
    setTimeout(wrapAll, 1000);

    /* Clic sur le menu latéral et sur « Retour au tableau de bord » */
    document.addEventListener("click", function (event) {
        const item = event.target.closest(".nav-item[data-page]");
        if (item) {
            event.preventDefault();
            setUrl("/" + item.dataset.page);
            return;
        }
        const back = event.target.closest("button, a");
        if (back && /retour au tableau de bord/i.test(back.textContent || "")) {
            setUrl("/dashboard");
        }
    });

    /* Boutons Précédent / Suivant du navigateur */
    window.addEventListener("popstate", function () {
        if (!locked()) {
            applyRoute();
        }
    });

    /* Connexion / déconnexion */
    const first = segment();
    if (PAGES.includes(first) || USER_PAGES[first]) {
        intended = "/" + first;
    }

    let wasLocked = locked();
    if (wasLocked) {
        history.replaceState({}, "", "/connexion");
    }

    new MutationObserver(function () {
        const now = locked();
        if (now === wasLocked) {
            return;
        }
        wasLocked = now;

        if (now) {
            history.replaceState({}, "", "/connexion");
        } else {
            done = true;
            clearInterval(timer);
            if (intended) {
                history.replaceState({}, "", intended);
                intended = null;
            }
            setTimeout(applyRoute, 50);
        }
    }).observe(document.body, { attributes: true, attributeFilter: ["class"] });

    /* Rechargement d'une page déjà connecté : on attend la session. */
    let tries = 0;
    timer = setInterval(function () {
        tries += 1;
        if (done) {
            clearInterval(timer);
            return;
        }
        if (window.currentUser && !locked()) {
            done = true;
            clearInterval(timer);
            applyRoute();
        } else if (tries > 40) {
            clearInterval(timer);
            if (!locked()) {
                done = true;
                applyRoute();
            }
        }
    }, 250);
})();
