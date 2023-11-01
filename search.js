document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const resultsContainer = document.getElementById('results');
    const loadingIndicator = document.getElementById('loading');

    searchButton.addEventListener('click', () => {
        const searchTerm = searchInput.value.trim().toLowerCase();
        resultsContainer.innerHTML = '';
        loadingIndicator.style.display = 'block';

        if (searchTerm.length >= 3) {
            fetch('https://testing-web.cloud/external/search/resoluciones.json')
                .then(response => response.json())
                .then(data => {
                    const results = searchInFiles(data, searchTerm);
                    const sortedResults = sortResultsByDate(results);
                    displayResults(sortedResults, data);
                })
                .finally(() => {
                    loadingIndicator.style.display = 'none';
                });
        } else {
            loadingIndicator.style.display = 'none';
            resultsContainer.innerHTML = '<p>Por favor, ingresa al menos 3 caracteres para buscar.</p>';
        }
    });

    function searchInFiles(data, searchTerm) {
        return data.filter(entry => {
            const name_res = entry.nombre.toLowerCase();
            const content = entry.contenido.toLowerCase();
            return (content.includes(searchTerm) + name_res.includes(searchTerm));
        });
    }

    function sortResultsByDate(results) {
        return results.sort((a, b) => new Date(b.fecha) - new Date(a.fecha));
    }

    function displayResults(results, data) {
        if (results.length === 0) {
            resultsContainer.innerHTML = '<li>No se encontraron resultados.</li>';
        } else {
            results.forEach(result => {
                const entry = data.find(item => item.nombre === result.nombre);
                if (entry) {
                    const listItem = document.createElement('li');
                    const link = document.createElement('a');
                    link.href = 'https://testing-web.cloud/external/search/resoluciones/' + entry.ubicacion + '.pdf';
                    link.textContent = entry.nombre + ' - ' + entry.fecha;
                    link.target = '_blank';
                    listItem.appendChild(link);
                    resultsContainer.appendChild(listItem);
                }
            });
        }
    }
});
