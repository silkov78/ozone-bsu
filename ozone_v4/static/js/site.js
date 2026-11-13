// Общие помощники нового фронта ННИЦ МО БГУ
(function () {
  const LOCALES = { ru: "ru-RU", be: "be-BY", en: "en-GB" };
  const lang = document.documentElement.lang || "ru";
  const locale = LOCALES[lang] || "ru-RU";
  const UVI = {
    ru: ["низкий", "умеренный", "высокий"],
    be: ["нізкі", "умераны", "высокі"],
    en: ["low", "moderate", "high"],
  }[lang] || ["низкий", "умеренный", "высокий"];

  // даты
  window.shortDate = s => new Date(s).toLocaleDateString(locale, { day: "numeric", month: "long" });
  window.fmtDate = s => new Date(s).toLocaleDateString(locale, { day: "numeric", month: "long", year: "numeric" });

  // уровень УФ-индекса: [css-класс, подпись]
  window.uviClass = v => v < 3 ? ["uvi-low", UVI[0]] : v < 6 ? ["uvi-mod", UVI[1]] : ["uvi-high", UVI[2]];

  // последнее непустое значение параметра в массиве наблюдений
  window.lastOf = (rows, key) => {
    for (let i = rows.length - 1; i >= 0; i--) if (rows[i][key] != null) return { date: rows[i].date, value: rows[i][key], i };
    return null;
  };

  // плавная смена раскладки (View Transitions), без анимации — если пользователь её отключил
  window.REDUCED_MOTION = matchMedia("(prefers-reduced-motion: reduce)").matches;
  window.smooth = fn => document.startViewTransition && !REDUCED_MOTION ? document.startViewTransition(fn) : fn();

  // Chart.js-плагин: линия аккуратно прорисовывается слева направо
  window.drawIn = {
    id: "drawIn",
    beforeDatasetsDraw(c) {
      if (REDUCED_MOTION) return;
      c.$t0 ??= performance.now();
      const t = Math.min(1, (performance.now() - c.$t0) / 2200), p = Math.sin(t * Math.PI / 2), a = c.chartArea;
      c.ctx.save(); c.ctx.beginPath(); c.ctx.rect(a.left - 2, a.top - 10, (a.right - a.left + 4) * p, a.bottom - a.top + 20); c.ctx.clip();
      if (t < 1) requestAnimationFrame(() => c.draw());
    },
    afterDatasetsDraw(c) { if (!REDUCED_MOTION) c.ctx.restore(); },
  };

  // шапка: тёмная поверх hero, светлая ниже; бургер-меню
  document.addEventListener("DOMContentLoaded", () => {
    const hero = document.querySelector(".hero"), hd = document.querySelector(".header");
    if (hero && hd) {
      document.body.classList.add("has-hero");
      const upd = () => hd.classList.toggle("dark", hero.getBoundingClientRect().bottom > 68);
      addEventListener("scroll", upd, { passive: true }); upd();
    }
    document.querySelector(".burger")?.addEventListener("click", () => document.getElementById("nav").classList.toggle("open"));
  });
})();

// ===== Версия для слабовидящих =====
(function () {
  const KEY = "a11y", h = document.documentElement;
  const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } };
  const save = s => { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} };
  function apply(s) {
    h.classList.remove("a11y", "a11y-bw", "a11y-wb", "a11y-noimg");
    if (s.on) {
      h.classList.add("a11y", "a11y-" + (s.scheme || "bw"));
      if (s.img === "off") h.classList.add("a11y-noimg");
      h.style.setProperty("--a11y-zoom", s.size || 1.25);
    } else h.style.removeProperty("--a11y-zoom");
    const panel = document.getElementById("a11y-panel");
    if (!panel) return;
    panel.hidden = !s.on;
    panel.querySelectorAll("[data-size]").forEach(b => b.classList.toggle("on", +b.dataset.size === +(s.size || 1.25)));
    panel.querySelectorAll("[data-scheme]").forEach(b => b.classList.toggle("on", b.dataset.scheme === (s.scheme || "bw")));
    panel.querySelectorAll("[data-img]").forEach(b => b.classList.toggle("on", b.dataset.img === (s.img || "on")));
    document.getElementById("a11y-toggle")?.setAttribute("aria-pressed", s.on ? "true" : "false");
    window.dispatchEvent(new Event("resize")); // графики пересчитают размер
  }
  document.addEventListener("DOMContentLoaded", () => {
    let s = load();
    apply(s);
    const set = patch => { s = { ...s, ...patch }; save(s); apply(s); };
    document.getElementById("a11y-toggle")?.addEventListener("click", () => set({ on: !s.on }));
    const panel = document.getElementById("a11y-panel");
    panel?.addEventListener("click", e => {
      const b = e.target.closest("button"); if (!b) return;
      if (b.dataset.size) set({ size: +b.dataset.size });
      else if (b.dataset.scheme) set({ scheme: b.dataset.scheme });
      else if (b.dataset.img) set({ img: b.dataset.img });
      else if ("off" in b.dataset) set({ on: false });
    });
  });
})();
