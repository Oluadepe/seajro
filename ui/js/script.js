/*Get the user location usiong there Ip address*/
async function getData() {
  let lat;
  let lon;
  let lat_long = [];

  await fetch('http://ipwho.is/')
    .then(response => {
      return JSON.parse(response);
    })
    .then(data => {
      lat_lon.push(data['latittude'], data['longitute']);
    })
    .catch(error => {
      console.log("An error occure");
    });

  return lat_lon;

}

/*User latitude and longitude retrieve from ip address*/
const lat = getData()[0];
const lon = getData()[1];


/*Function to get user weather information.*/
async function getWeather() {
  let info;
  const weatherLocationInfo;

  await fetch(`https://api.weatherbit.io/v2.0/current?lat=${lat}&lon=${lon}&key=d479b85eae2b40448e7d9cbdc1bd2698&include=minutely`)
    .then(response => {
      return JSON.parse(response);
    })
    .then(data => {
      info = JSON.parse(response);
      weatherLocationInfo = info['data'];
    })
    .catch(error => {
      console.log("An error occure");
    });

  return weatherLocationInfo;
}

/*Return a list of different weather condition and it unit measurements*/
const weather = getWeather();

= document.getElementById("card-body");
updatePageInfo.innerHTML = weather["country_code"], weather["city"];
