// localStorage.removeItem("session_token");

if (localStorage.session_token) {
  location.assign("http://localhost:8002/home/");
}  