function getWeather() {
    const city = document.getElementById("city").value;
    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    fetch("/get_weather", {method: "POST",headers: { "Content-Type": "application/json" },body: JSON.stringify({ city })})
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("weather-result").innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            document.getElementById("weather-result").innerHTML = `
                <h3>${data.city}</h3>
                <p>Temperature: ${data.temperature}°C</p>
                <p>Humidity: ${data.humidity}%</p>
                <p>Condition: ${data.description}</p>
            `;
        }
    })
    .catch(error => console.error("Error fetching weather:", error));
}
