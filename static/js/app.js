const copyDate = document.getElementById("year");
const date = new Date();
const timeEl = document.getElementById("time");

const news = document.getElementById('card news');

let year = date.getFullYear();
copyDate.textContent = year;

const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
timeEl.textContent = currentTime;

