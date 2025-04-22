console.log("✅ popup.js loaded");

window.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".popup-wrapper").forEach(wrapper => {
    const trigger = wrapper.querySelector(".popup-trigger");
    const bubble = wrapper.querySelector(".popup-bubble");

    if (!trigger || !bubble) return;

    let hideTimeout;

    const showBubble = () => {
      clearTimeout(hideTimeout);
      document.querySelectorAll(".popup-bubble").forEach(b => b.style.display = "none");
      bubble.style.display = "block";

      if (window.renderMathInElement) {
        renderMathInElement(bubble, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\(", right: "\\)", display: false },
            { left: "\\[", right: "\\]", display: true }
          ],
          throwOnError: false
        });
      }
    };

    const hideBubble = () => {
      hideTimeout = setTimeout(() => {
        bubble.style.display = "none";
      }, 200);
    };

    // Click toggle
    trigger.addEventListener("click", e => {
      e.stopPropagation();
      const visible = bubble.style.display === "block";
      document.querySelectorAll(".popup-bubble").forEach(b => b.style.display = "none");
      if (!visible) showBubble();
    });

    // Hover
    trigger.addEventListener("mouseenter", showBubble);
    trigger.addEventListener("mouseleave", hideBubble);
    bubble.addEventListener("mouseenter", () => clearTimeout(hideTimeout));
    bubble.addEventListener("mouseleave", hideBubble);

    // Global close
    document.addEventListener("click", () => bubble.style.display = "none");
    document.addEventListener("keydown", e => {
      if (e.key === "Escape") {
        bubble.style.display = "none";
      }
    });

    // ✅ Render math in the trigger label itself
    if (window.renderMathInElement) {
      renderMathInElement(trigger, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false },
          { left: "\\(", right: "\\)", display: false },
          { left: "\\[", right: "\\]", display: true }
        ],
        throwOnError: false
      });
    }
  });
});






// add touch support

/* Pointer‑events → synthetic touch‑events for Touch‑Punch -------------- */
(function () {
  if (!window.PointerEvent) return;               // old browsers

  function makeTouchList(e) {
    return [{
      identifier : e.pointerId,
      target     : e.target,
      clientX    : e.clientX,
      clientY    : e.clientY,
      pageX      : e.pageX,
      pageY      : e.pageY,
      screenX    : e.screenX,
      screenY    : e.screenY
    }];
  }

  function dispatchSynthetic(original, type) {
    const touchEvent = new Event(type, { bubbles:true, cancelable:true });
    touchEvent.touches        =
    touchEvent.targetTouches  =
    touchEvent.changedTouches = makeTouchList(original);
    original.target.dispatchEvent(touchEvent);
  }

  ["pointerdown","pointermove","pointerup","pointercancel"]
    .forEach(peType => {
      window.addEventListener(peType, ev => {
        if (ev.pointerType !== "touch" && ev.pointerType !== "pen") return;
        switch (peType) {
          case "pointerdown":   dispatchSynthetic(ev,"touchstart");  break;
          case "pointermove":   dispatchSynthetic(ev,"touchmove");   break;
          case "pointerup":     dispatchSynthetic(ev,"touchend");    break;
          case "pointercancel": dispatchSynthetic(ev,"touchcancel"); break;
        }
      }, true);                               // capture phase ⇒ before jQuery‑UI
    });
})();
