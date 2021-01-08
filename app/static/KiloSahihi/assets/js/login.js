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
        fetch(apilink + "token/", { method: 'post', headers: myheaders, body: JSON.stringify(dataobj), }).then((resp) => {
            resp.json().then((data) => {
                if (data.token) {
                    let thename = "Dashboard Login";
                    let theaction = "User of Identification Number " + data.pk.toString() + " has logged in.";
                    let theuser = data.user;
                    let thestatus = "Active";

                    let sess_token = data.token;
                    let sess_data = data;

                    var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                    myheaders.append("Authorization", "Token " + sess_token);
                    try {
                        fetch(apilink + "audits", { method: 'post', headers: myheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                            resp.json().then((data) => {
                                if (data.name) {
                                    localStorage.setItem("session_token", sess_token);
                                    localStorage.setItem("session_user", JSON.stringify(sess_data));
                                    if (localStorage.last_location) {
                                        location.assign(localStorage.last_location);
                                        localStorage.removeItem("last_location");
                                    }
                                    else {
                                        location.assign(applink + "home/");
                                    }
                                }
                                else {
                                    alert("Something went wrong. Please refresh page and try again.");
                                }
                            });
                        });
                    }
                    catch (err) {
                        console.log(err);
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