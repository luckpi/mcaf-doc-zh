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

  function buildLink() {
    var zh = isZhPage();
    var a = document.createElement("a");
    a.id = "mcaf-lang-toggle";
    a.href = "#";
    a.textContent = zh ? "English" : "中文";
    a.title = zh ? "Switch to English" : "切换到中文";
    a.addEventListener("click", function (e) {
      e.preventDefault();
      setLang(zh ? "en" : "zh");
    });

    // Insert into top nav as a right-aligned <li>, before "index" in DOM order.
    // Since li.right floats right, DOM order index/next/previous renders as
    // previous | next | index visually. Inserting before index puts it:
    // previous | next | index | 中文
    var topNav = document.querySelector("div.related > ul, div.related ul");
    if (topNav) {
      var li = document.createElement("li");
      li.className = "right";
      li.appendChild(a);
      li.appendChild(document.createTextNode(" |"));
      var firstRight = topNav.querySelector("li.right");
      if (firstRight) {
        topNav.insertBefore(li, firstRight);
      } else {
        topNav.appendChild(li);
      }
      return;
    }

    // Fallback: footer
    var footer = document.querySelector("div.footer");
    if (footer) {
      footer.appendChild(document.createTextNode(" | "));
      footer.appendChild(a);
      return;
    }

    // Last resort: fixed corner
    a.style.cssText =
      "position:fixed;top:6px;right:10px;z-index:9999;" +
      "font-size:12px;color:#fff;text-decoration:none;font-family:inherit;";
    document.body.appendChild(a);
  }

  function addStyle() {
    var css = [
      "#mcaf-lang-toggle{color:#fff;text-decoration:none;}",
      "#mcaf-lang-toggle:hover{text-decoration:underline;}"
    ].join("\n");
    var s = document.createElement("style");
    s.id = "mcaf-lang-toggle-style";
    s.textContent = css;
    document.head.appendChild(s);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { addStyle(); buildLink(); });
  } else {
    addStyle(); buildLink();
  }
})();
