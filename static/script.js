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