  document.addEventListener("DOMContentLoaded", () => {
    const observer = new MutationObserver((mutationsList, observer) => {
      for (const mutation of mutationsList) {
        if (mutation.type === "childList") {
          if (document.querySelector('mjx-container[jax="SVG"]')) {
            console.log("MathJax gebruikt nu SVG rendering.");
           // remove banner
           document.querySelectorAll('.bd-header-announcement').forEach(function(el) {
            if (typeof InstallTrigger !== 'undefined') {
              el.style.display = 'none';
            }
            });
            
          // remove tippy's
          document.querySelectorAll('.tippy-box').forEach(function(el) {
            el.style.display = 'none';
          });
          }

          if (document.querySelector('mjx-container[jax="CHTML"]')) {
            console.log("MathJax gebruikt nu CHTML rendering.");
           // add banner
            document.querySelectorAll('.bd-header-announcement').forEach(function(el) {
              if (typeof InstallTrigger !== 'undefined') {
                el.style.display = 'flex';
              }
              });
            // enable tippy's
          document.querySelectorAll('.tippy-box').forEach(function(el) {
            el.style.display.removeProperty( 'display' );
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