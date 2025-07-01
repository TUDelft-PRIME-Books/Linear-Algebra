document.addEventListener("DOMContentLoaded", () => {
    const toggleButtonId = "toggle-dropdown-button";
    const rootDropdownState = "dropdowns-opened";

    const headerEnd = document.querySelector(".article-header-buttons");
    if (headerEnd) {
        const button = document.createElement("button");
        button.id = toggleButtonId;
        button.className = "btn btn-sm nav-link pst-navbar-icon pst-js-only";
        button.title = "Open all dropdowns";
        button.innerHTML = '<i class="fa-solid fa-angles-down"></i>';

        headerEnd.prepend(button);
    }

    document.getElementById(toggleButtonId)?.addEventListener("click", () => {
        if (document.body.classList.contains(rootDropdownState)) {
            closeDropdowns();
        } else {
            openDropdowns();
        }
    });

    function openDropdowns() {
        document.body.classList.add(rootDropdownState);
        const button = document.getElementById(toggleButtonId);
        if (button) {
            button.innerHTML = '<i class="fa-solid fa-angles-up"></i>';
            button.title = "Close all dropdowns";
        }
        const details = document.querySelectorAll('details.dropdown');
        details.forEach(detail => {
            if (!detail.open) {
                detail.open = true;
            }
        });
        const divs = document.querySelectorAll('div.dropdown');
        divs.forEach(div => {
            div.classList.remove('toggle-hidden');
        });
        const buttons = document.querySelectorAll('button.toggle-button');
        buttons.forEach(button => {
            button.classList.remove('toggle-button-hidden');
        });

        console.log("Dropdowns opened");
        
    }

    function closeDropdowns() {
        document.body.classList.remove(rootDropdownState);
        const button = document.getElementById(toggleButtonId);
        if (button) {
            button.innerHTML = '<i class="fa-solid fa-angles-down"></i>';
            button.title = "Open all dropdowns";
        }
        const details = document.querySelectorAll('details.dropdown');
        details.forEach(detail => {
            if (detail.open) {
                detail.open = false;
            }
        });
        const divs = document.querySelectorAll('div.dropdown');
        divs.forEach(div => {
            div.classList.add('toggle-hidden');
        });
        const buttons = document.querySelectorAll('button.toggle-button');
        buttons.forEach(button => {
            button.classList.add('toggle-button-hidden');
        });

        console.log("Dropdowns closed");
    }
});