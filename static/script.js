// ===============================
// Elements
// ===============================

const themeBtn = document.getElementById("theme-btn");
const body = document.body;

const quote = document.getElementById("quote");
const copyBtn = document.getElementById("copy-btn");

const toast = document.getElementById("toast");

const form = document.querySelector("form");
const generateBtn = document.querySelector(".generate-btn");

// ===============================
// Dark / Light Mode
// ===============================

themeBtn.addEventListener("click", () => {

    body.classList.toggle("light-mode");

    if (body.classList.contains("light-mode")) {

        themeBtn.innerHTML = "☀️";
        localStorage.setItem("theme", "light");

    } else {

        themeBtn.innerHTML = "🌙";
        localStorage.setItem("theme", "dark");

    }

});

// ===============================
// Load Saved Theme
// ===============================

window.onload = () => {

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "light") {

        body.classList.add("light-mode");
        themeBtn.innerHTML = "☀️";

    }

};

// ===============================
// Copy Quote
// ===============================

copyBtn.addEventListener("click", () => {

    navigator.clipboard.writeText(quote.innerText);

    toast.innerHTML = "📋 Quote copied successfully!";
    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 2000);

});

// ===============================
// Loading Button
// ===============================

form.addEventListener("submit", () => {

    generateBtn.classList.add("loading");

});