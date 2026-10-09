/* ComplianceForge — Tableau de bord : emojis, accès rapides, dernière analyse */
(function () {
    "use strict";
    if (window.__cfDashFix) { return; }
    window.__cfDashFix = true;

    const API = () => window.API_BASE || "https://api.complianceforge.test";
    const PICTO = /^\s*(?:\p{Extended_Pictographic}[\uFE0F\u200D]*)+\s*/u;
    const ICONS = { organisation: "🏢", formulaires: "📄", registre: "📋", incidents: "🚨",
        conformite: "📊", risques: "⚠️", documents: "📁", profil: "👤", dashboard: "🏠" };
    const _fetch = window.fetch.bind(window);

    const st = document.createElement("style");
    st.textContent = `
html body .quick-card > span:first-child { display:flex !important; align-items:center; justify-content:center;
    font-size:20px !important; line-height:1 !important; opacity:1 !important; visibility:visible !important; text-indent:0 !important; }
html body .quick-card strong { white-space:normal !important; overflow:visible !important; text-overflow:clip !important; line-height:1.25 !important; }
html body .quick-card small { white-space:normal !important; overflow:visible !important; text-overflow:clip !important; }`;
    document.head.appendChild(st);

    /* ---------- Accès rapides ---------- */
    function fixQuickCards() {
        document.querySelectorAll(".quick-card").forEach((card) => {
            const m = /navigate\(\s*['"]([\w-]+)['"]/.exec(card.getAttribute("onclick") || "");
            const strong = card.querySelector("strong");
            const icon = card.querySelector(":scope > span");
            const fromTitle = strong && PICTO.exec(strong.textContent || "");
            const emoji = (m && ICONS[m[1]]) || (fromTitle && fromTitle[0].trim()) || "📌";
            if (icon && !PICTO.test(icon.textContent || "")) { icon.textContent = emoji; }
            if (strong && PICTO.test(strong.textContent || "")) {
                strong.textContent = strong.textContent.replace(PICTO, "");
            }
        });
    }

    /* ---------- Cartes Analyse / Scoring ---------- */
    function labelOf(text) {
        return Array.from(document.querySelectorAll("span")).find((s) =>
            s.textContent.replace(PICTO, "").trim().toLowerCase() === text);
    }
    function valueEl(id, labelText) {
        let v = document.getElementById(id);
        if (v) { return v; }
        const l = labelOf(labelText);
        if (!l) { return null; }
        v = l.parentElement.querySelector("strong");
        if (!v) {
            v = document.createElement("strong");
            l.insertAdjacentElement("afterend", v);
        }
        return v;
    }
    function decorate(valueNode, labelText, emoji) {
        const l = (valueNode && valueNode.parentElement && Array.from(valueNode.parentElement.querySelectorAll("span"))
            .find((s) => s.textContent.replace(PICTO, "").trim().toLowerCase() === labelText)) || labelOf(labelText);
        if (l && !PICTO.test(l.textContent)) { l.textContent = emoji + " " + l.textContent.trim(); }
    }
    const fmt = (n) => Number(n).toLocaleString("fr-FR", { maximumFractionDigits: 1 });
    const norm = (s) => String(s || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    function levelColor(n) {
        const k = norm(n);
        if (k.startsWith("faible") || k.startsWith("bas")) { return "#067647"; }
        if (k.startsWith("moyen") || k.startsWith("modere")) { return "#b54708"; }
        return "#b42318";
    }
    function setText(el, txt, color) {
        if (!el) { return; }
        if (el.textContent !== txt) { el.textContent = txt; }
        if (color && el.style.color !== color) { el.style.color = color; }
    }

    let cache = null, refreshing = false, lastEl = null;

    function apply() {
        const conf = valueEl("dashboard-score-conformite", "score de conformité");
        const risk = valueEl("dashboard-score-risque", "score de risque");
        const lvl = valueEl("dashboard-niveau-risque", "niveau de risque");
        const trt = valueEl("dashboard-traitement-evalue", "traitement évalué");
        decorate(conf, "score de conformité", "✅");
        decorate(risk, "score de risque", "⚠️");
        decorate(lvl, "niveau de risque", "🎯");
        decorate(trt, "traitement évalué", "🔎");
        if (!cache) { return; }
        const { t, lc, lr, when } = cache;
        const date = new Date(when);
        const quand = isNaN(date) ? "" : date.toLocaleString("fr-FR", { dateStyle: "short", timeStyle: "short" });
        if (lc) { setText(conf, fmt(lc.score_global) + " %"); }
        if (lr) {
            setText(risk, fmt(lr.score_global));
            const n = String(lr.niveau || "");
            setText(lvl, n.charAt(0).toUpperCase() + n.slice(1), levelColor(n));
        }
        const id = t.id || t.traitement_id || "";
        const nom = t.nom_traitement || t.nom || t.name || ("Traitement #" + String(id).slice(0, 8));
        setText(trt, nom);
        if (trt) { trt.title = nom; }
        const sm = (el) => el && el.parentElement && el.parentElement.querySelector("small");
        const s1 = sm(conf), s2 = sm(risk), s4 = sm(trt);
        if (s1) { setText(s1, "Dernière évaluation" + (quand ? " : " + quand : "")); }
        if (s2) { setText(s2, "Dernière évaluation" + (quand ? " : " + quand : "")); }
        if (s4) { setText(s4, "Dernier traitement analysé"); }
    }

    async function refresh() {
        if (refreshing) { return; }
        refreshing = true;
        try {
            const raw = await (await _fetch(API() + "/traitements")).json();
            const list = Array.isArray(raw) ? raw : (raw.items || raw.data || raw.traitements || []);
            let best = null;
            await Promise.all(list.map(async (t) => {
                const id = t.id || t.traitement_id;
                if (!id) { return; }
                try {
                    const [c, r] = await Promise.all([
                        _fetch(API() + "/traitements/" + id + "/scores/conformite").then((x) => (x.ok ? x.json() : [])),
                        _fetch(API() + "/traitements/" + id + "/scores/risque").then((x) => (x.ok ? x.json() : []))
                    ]);
                    const last = (a) => (Array.isArray(a) ? a : [a]).filter(Boolean)
                        .sort((x, y) => String(y.date_calcul).localeCompare(String(x.date_calcul)))[0];
                    const lc = last(c), lr = last(r);
                    const when = [lc && lc.date_calcul, lr && lr.date_calcul].filter(Boolean).sort().pop();
                    if (when && (!best || when > best.when)) { best = { t, lc, lr, when }; }
                } catch (_) {}
            }));
            if (best) { cache = best; }
        } catch (e) {
            console.warn("[ComplianceForge] Dernière analyse indisponible :", e);
        }
        refreshing = false;
        apply();
    }

    /* Rafraîchit après chaque calcul de score */
    window.fetch = function (input, init) {
        const p = _fetch(input, init);
        try {
            const url = typeof input === "string" ? input : ((input && input.url) || "");
            const method = ((init && init.method) || (input && input.method) || "GET").toUpperCase();
            if (method === "POST" && /\/scores\/calculer/.test(url)) {
                p.then((r) => { if (r.ok) { setTimeout(refresh, 800); } }).catch(() => {});
            }
        } catch (_) {}
        return p;
    };

    let timer = null;
    function tick() {
        fixQuickCards();
        apply();
        const el = document.getElementById("dashboard-score-conformite");
        if (el && el !== lastEl) { lastEl = el; refresh(); }
    }
    new MutationObserver(() => { clearTimeout(timer); timer = setTimeout(tick, 120); })
        .observe(document.body, { childList: true, subtree: true, characterData: true });
    tick();
})();
