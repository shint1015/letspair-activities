document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('travelForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        const style = document.getElementById('style').value;
        const place = document.getElementById('place').value;
        const duration = document.getElementById('duration').value;
        const demand = document.getElementById('demand').value;
        const response = await fetch('http://localhost:8000/travel-story', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ style, place, duration, demand })
        });
        const data = await response.json();
        document.getElementById('result').innerHTML = `<div class='story'><h2>Your Travel Story</h2>${data.story}</div>`;
    });
});
