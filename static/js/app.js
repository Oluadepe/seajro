const copyDate = document.getElementById("year")
const timeEl = document.getElementById("time")
const date = new Date();

let year = date.getFullYear();
copyDate.textContent = year;

const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
timeEl.textContent = currentTime;
