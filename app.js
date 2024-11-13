const div_navigation = document.getElementById("navigation")

const cargarNavbar = (url) => {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("Error al cargar el navbar");
            }
            return response.text();
        })
        .then(html => {
            div_navigation.innerHTML = html;
        })
        .catch(error => {
            console.error("Error:", error);
        });
}

cargarNavbar("/pages/partials/navbar.html")