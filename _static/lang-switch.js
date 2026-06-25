/* MCAF doc bilingual toggle (offline-capable, no external deps) */
(function () {
  "use strict";
  var STORAGE_KEY = "mcaf-lang";
  var pref;
  try { pref = localStorage.getItem(STORAGE_KEY) || "en"; } catch (e) { pref = "en"; }

  function isZhPage() {
    return /\.zh\.html(\?|$|#)/.test(location.pathname) || /\.zh\.html(\?|$|#)/.test(location.href);
  }
  function zhUrlFor(url) {
    if (url.indexOf('.html') === -1) {
      return url.replace(/\/(\?|#|$)/, function (m, p1) {
        return "/index.zh.html" + p1;
      });
    }
    return url.replace(/\.html(\?|#|$)/, function (m, p1) {
      return ".zh.html" + p1;
    });
  }
  function enUrlFor(url) {
    if (url.indexOf('.zh.html') === -1) {
      return url;
    }
    if (/index\.zh\.html/.test(url)) {
      return url.replace(/index\.zh\.html(\?|#|$)/, function (m, p1) {
        return "" + p1 || "/";
      }).replace(/\/$/, "/");
    }
    return url.replace(/\.zh\.html(\?|#|$)/, function (m, p1) {
      return ".html" + p1;
    });
  }

  // Auto-redirect to keep the user in their preferred language across navigation.
  try {
    if (pref === "zh" && !isZhPage()) {
      var z = zhUrlFor(location.href);
      if (z !== location.href) { location.replace(z); return; }
    } else if (pref === "en" && isZhPage()) {
      var e = enUrlFor(location.href);
      if (e !== location.href) { location.replace(e); return; }
    }
  } catch (e) {}

  function setLang(lang) {
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
    if (lang === "zh" && !isZhPage()) {
      location.replace(zhUrlFor(location.href));
    } else if (lang === "en" && isZhPage()) {
      location.replace(enUrlFor(location.href));
    }
  }

  function buildButton() {
    var btn = document.createElement("button");
    btn.id = "mcaf-lang-toggle";
    btn.type = "button";
    btn.textContent = isZhPage() ? "English" : "中文";
    btn.title = isZhPage() ? "Switch to English" : "切换到中文";
    btn.addEventListener("click", function () {
      setLang(isZhPage() ? "en" : "zh");
    });
    document.body.appendChild(btn);
  }

  function addStyle() {
    var css = [
      "#mcaf-lang-toggle{",
      "position:fixed;top:8px;right:10px;z-index:9999;",
      "background:#1e6f3c;color:#fff;border:1px solid #155a2e;",
      "padding:5px 12px;font-size:13px;font-weight:600;",
      "border-radius:4px;cursor:pointer;line-height:1.4;",
      "box-shadow:0 1px 3px rgba(0,0,0,.25);font-family:inherit;",
      "}",
      "#mcaf-lang-toggle:hover{background:#287a47;}",
      "#mcaf-lang-toggle:active{transform:translateY(1px);}"
    ].join("\n");
    var s = document.createElement("style");
    s.id = "mcaf-lang-toggle-style";
    s.textContent = css;
    document.head.appendChild(s);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { addStyle(); buildButton(); });
  } else {
    addStyle(); buildButton();
  }
})();
