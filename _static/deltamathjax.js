(function () {
    var isFirefox = navigator.userAgent.toLowerCase().includes('firefox');
    var output = isFirefox ? 'svg' : 'chtml';
  
    // Laad MathJax vanaf CDN
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-' + output + '.js';
    script.async = true;
    document.head.appendChild(script);
  })();
  