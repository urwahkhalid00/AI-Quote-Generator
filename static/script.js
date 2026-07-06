// ===============================
// Elements
// ===============================

const themeBtn = document.getElementById("theme-btn");

const body = document.body;

const quote = document.querySelector(".quote-box h2");

const copyBtn = document.querySelectorAll(".action-btn")[0];

// ===============================
// Dark / Light Mode
// ===============================

themeBtn.addEventListener("click", () => {

    body.classList.toggle("light-mode");

    if(body.classList.contains("light-mode")){

        themeBtn.innerHTML = "☀️";

        localStorage.setItem("theme","light");

    }

    else{

        themeBtn.innerHTML = "🌙";

        localStorage.setItem("theme","dark");

    }

});

// ===============================
// Load Saved Theme
// ===============================

window.onload = () => {

    const savedTheme = localStorage.getItem("theme");

    if(savedTheme === "light"){

        body.classList.add("light-mode");

        themeBtn.innerHTML = "☀️";

    }

}

// ===============================
// Copy Quote
// ===============================

copyBtn.addEventListener("click", () => {

    navigator.clipboard.writeText(quote.innerText);

    copyBtn.innerHTML = "✅ Copied";

    setTimeout(() => {

        copyBtn.innerHTML = "📋 Copy";

    },2000);

});