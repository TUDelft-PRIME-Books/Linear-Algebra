  document.addEventListener('DOMContentLoaded', function() {
    // Check if the logo has already been added
    if (document.querySelector('.custom-logo')) {
      return;
    }
    
    var logoDiv = document.createElement('div');
    logoDiv.classList.add('custom-logo');
    logoDiv.innerHTML = '<img src="https://d2k0ddhflgrk1i.cloudfront.net/Websections/Huisstijl/Bouwstenen/Logo/Descriptor/TUDelft_logo_descriptor_rgb.png" alt="TU Delft logo" style="width: 100%;">';
    var navBar = document.querySelector('.bd-sidebar');
    
    if (navBar) {
      navBar.appendChild(logoDiv);
    }
  });
   