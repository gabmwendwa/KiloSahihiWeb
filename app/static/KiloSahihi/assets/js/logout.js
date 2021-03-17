function logout() {
    if (localStorage.session_token) {

        //console.log(userinfo);
        //return;

        let thename = "Dashboard Logout";
        let theaction = "User of Identification Number " + userinfo.pk.toString() + " has logged out.";
        let theuser = userinfo.user;
        let thestatus = "Active";

        var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
        try {
            fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                resp.json().then((data) => {
                    if (data.name) {
                        localStorage.removeItem("session_token");
                        localStorage.removeItem("session_user");
                        location.assign(applink + "login/");
                    } else {
                        alert("Something went wrong. Please refresh page and try again.");
                    }
                });
            });
        } catch (err) {
            console.log(err);
        }
    }
}