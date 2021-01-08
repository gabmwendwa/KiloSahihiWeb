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

