document.getElementById("login-btn").addEventListener("click", function (event) {
    event.preventDefault();
    login();
});
document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault()
});

var uname = "";
var pword = "";

function login() {
    var dataobj = { "username": uname, "password": pword };

    var myheaders = new Headers();
    // myheaders.append("Authorization", "Token a7ecffc7330ff088d7b91f0c0b5d27036b19acfa")
    myheaders.append("Content-Type", "application/json");

    try {
        fetch("http://localhost:8003/api/token/", { method: 'post', headers: myheaders, body: JSON.stringify(dataobj), }).then((resp) => {
            resp.json().then((data) => {
                if (data.token) {
                    localStorage.setItem("session_token", data.token);
                    if (localStorage.last_location) {
                        location.assign(localStorage.last_location);
                        localStorage.removeItem("last_location");
                    }
                    else {
                        location.assign("http://localhost:8002/home/");
                    }
                }
                else {
                    alert("Incorrect username and password.");
                }
            });
        });
    }
    catch (err) {
        console.log(err);
    }
    return false;
}