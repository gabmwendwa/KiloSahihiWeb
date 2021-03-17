let current_url = window.location.href;

let url_arr = current_url.split("/");

let current_domain = url_arr[2].split(":")[0];

let apiport = "8000";
let appport = "8001";

let apilink = location.protocol + "//" + current_domain + ":" + apiport + "/api/";

let applink = location.protocol + "//" + current_domain + ":" + appport + "/";

var getheaders = new Headers();
getheaders.append("Authorization", "Token " + localStorage.session_token);
getheaders.append("Content-Type", "application/json");


let userinfo = JSON.parse(localStorage.session_user);

console.log("Authorization", "Token " + localStorage.session_token);

/**
 * Returns a random number between min (inclusive) and max (exclusive)
 */
function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

/**
 * Returns a random integer between min (inclusive) and max (inclusive).
 * The value is no lower than min (or the next integer greater than min
 * if min isn't an integer) and no greater than max (or the next integer
 * lower than max if max isn't an integer).
 * Using Math.round() will give you a non-uniform distribution!
 */
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var rand1 = [getRandomInt(20, 99),getRandomInt(20, 99),getRandomInt(20, 99),getRandomInt(20, 99),getRandomInt(20, 99),getRandomInt(20, 99)];
var rand2 = getRandomInt(50, 100);
var rand3 = getRandomInt(60, 100);
