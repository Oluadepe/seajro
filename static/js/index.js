// This is the script for styling and manipulating elements

const logo = document.getElementsByClassName('logo');

async function getWeather() {
    const response = await fetch('https://ipwhois.app/json/');
    const data = await response.json();
    const lat = data.latitude;
    const lon = data.longitude;

    const weatherResponse = await fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({lon: lon, lat: lat})
    });

    const weatherData = await weatherResponse.json();
    console.log(weatherData);
    document.getElementById("city_name").innerHTML = weatherData.city_name;
    document.getElementById("temp").innerHTML = weatherData.temp;
    document.getElementById("weather-desc").innerHTML = weatherData.description;
    document.getElementById("country_code").innerHTML = weatherData.country_code;
}

 window.addEventListener('load', getWeather);
//document.addEventListener('DOMContentLoaded', getWeather);
