document.addEventListener("DOMContentLoaded", () => {
    const observer = new MutationObserver((mutationsList, observer) => {
      for (const mutation of mutationsList) {
        if (mutation.type === "childList") {
          if (document.querySelector('mjx-container[jax="SVG"]')) {
            console.log("MathJax gebruikt nu SVG rendering.");
            observer.disconnect();
            // remove banner
            document.querySelectorAll('.bd-header-announcement').forEach(function(el) {
                el.style.display = 'none';
              });
          }
        }
      }
    });
  
    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  });