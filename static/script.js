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

const toast = document.getElementById("toast");

copyBtn.addEventListener("click", () => {

    navigator.clipboard.writeText(quote.innerText);

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    },2000);

});
// ===============================
// Loading Button
// ===============================

const form = document.querySelector("form");

const generateBtn = document.querySelector(".generate-btn");

form.addEventListener("submit", () => {

    generateBtn.classList.add("loading");

});

// ===============================
// Favorite Quote
// ===============================

const favoriteBtn = document.getElementById("favorite-btn");

favoriteBtn.addEventListener("click", () => {

    const favoriteQuote = {
        quote: quote.innerText,
        author: document.querySelector(".quote-box h3").innerText
    };

    let favorites = JSON.parse(localStorage.getItem("favorites")) || [];

    // Duplicate check
    const alreadyExists = favorites.some(item => item.quote === favoriteQuote.quote);

    if (!alreadyExists) {

        favorites.push(favoriteQuote);

        localStorage.setItem("favorites", JSON.stringify(favorites));

        toast.innerHTML = "❤️ Added to Favorites";

    } else {

        toast.innerHTML = "Already in Favorites";

    }

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 2000);

});