$.fn.serializeObject = function () {
    var o = {};
    var a = this.serializeArray();
    $.each(a, function () {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

var getid = location.pathname;
var getidarr = getid.split("/");

getid = getidarr[getidarr.length - 2];
var gettype = getidarr[getidarr.length - 3];


var getheaders = new Headers();
getheaders.append("Authorization", "Token " + localStorage.session_token);
getheaders.append("Content-Type", "application/json");
var set_form = $('#settings_form').parsley();



function getOptionsList(what, selectid) {
    var durl = apilink;
    var opstr;
    var selectbody = document.getElementById(selectid);
    switch (what) {
        case "factory":
            durl += "factories";
            opstr = "Factory";
            break;
        case "cooperative":
            durl += "cooperatives";
            opstr = "Cooperative";
            break;
        case "product":
            durl += "produce";
            opstr = "Product";
            break;
    }
    try {
        fetch(durl, { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var optionsdata = '<option value="" selected>-Choose ' + opstr + '-</option>';
                if (data.length) {
                    for (var i = 0; i < data.length; i++) {
                        optionsdata += '<option id="' + data[i]["id"] + '" value="' + data[i]["id"] + '">' + data[i]["name"] + '</option>';
                    }
                    selectbody.innerHTML = optionsdata;
                }
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}


function getFormData() {
    var durl = apilink;
    switch (gettype) {
        case "factory":
            durl += "factories/" + getid;
            break;
        case "fro":
            durl += "clerks/" + getid;
            break;
        case "cooperative":
            durl += "cooperatives/" + getid;
            break;
        case "product":
            durl += "produce/" + getid;
            break;
        case "farmer":
            durl += "farmers/" + getid;
            break;
        case "device":
            durl += "devices/" + getid;
            break;
    }
    try {
        fetch(durl, { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                for (var key in data) {
                    $("input#" + key).val(data[key]);
                }
                switch (gettype) {
                    case "farmer":
                    case "fro":
                        $("input#confirm_password").val(data["password"]);
                        $('#factory').find('#' + data["factory"]).attr("selected", "true");
                        break;
                    case "factory":
                        $('#cooperative').find('#' + data["cooperative"]).attr("selected", "true");
                        $('#product').find('#' + data["product"]).attr("selected", "true");
                        break;
                    case "product":
                        break;
                    case "device":
                        $('#factory').find('#' + data["factory"]).attr("selected", "true");
                        break;
                }
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}

document.getElementById("submit-btn").addEventListener("click", function (event) {
    if (set_form.isValid()) {
        event.preventDefault();
        submitSettingsForm(this);
    }
});

document.getElementById("delete-btn").addEventListener("click", function (event) {
    if (set_form.isValid()) {
        event.preventDefault();
        //deleteForm(this);
        var r = confirm("Are you sure you want to delete this record?");
        if (r == true) {
            deleteFormRecord(this);
        }
    }
});

document.getElementById("settings_form").addEventListener("submit", function (event) {
    if (set_form.isValid()) {
        event.preventDefault()
    }
});

function submitSettingsForm(elem) {
    var durl = apilink;
    var form_name = elem.getAttribute("data-form-name");
    var inputobj = $('form').serializeObject();
    var dataobj = JSON.stringify(inputobj);
    var what, whatTitle;

    switch (form_name) {
        case "settings_farmer":
            durl += "farmers/" + getid;
            what = "farmer";
            whatTitle = "Farmer";
            break;
        case "settings_factory":
            durl += "factories/" + getid;
            what = "factory";
            whatTitle = "Factory";
            break;
        case "settings_device":
            durl += "devices/" + getid;
            what = "device";
            whatTitle = "Device";
            break;
        case "settings_fro":
            durl += "clerks/" + getid;
            what = "clerk";
            whatTitle = "Clerk";
            break;
        case "settings_produce":
            durl += "produce/" + getid;
            what = "produce";
            whatTitle = "Produce";
            break;
    }
    try {
        fetch(durl, { method: 'put', headers: getheaders, body: dataobj, }).then((resp) => {
            resp.json().then((data) => {
                switch (form_name) {
                    case "settings_fro":
                    case "settings_farmer":
                        if (data.username == inputobj.username) {

                            let thename = "Dashboard " + whatTitle + " Edited";
                            let theaction = "User of Identification Number " + userinfo.pk.toString() + " has edited a " + what + " of Identification Number " + data.id + " and Username " + data.username + ".";
                            let theuser = userinfo.user;
                            let thestatus = "Active";

                            var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                            try {
                                fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                                    resp.json().then((data) => {
                                        if (data.name) {
                                            alert("Editted successfully.");
                                            location.reload();
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
                            alert("Something went wrong. Try again.");
                        }
                        break;
                    case "settings_factory":
                        if (data.name == inputobj.name) {
                            let thename = "Dashboard " + whatTitle + " Edited";
                            let theaction = "User of Identification Number " + userinfo.pk.toString() + " has edited a " + what + " of Identification Number " + data.id + " and Name " + data.name + ".";
                            let theuser = userinfo.user;
                            let thestatus = "Active";

                            var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                            try {
                                fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                                    resp.json().then((data) => {
                                        if (data.name) {
                                            alert("Editted successfully.");
                                            location.reload();
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
                            alert("Something went wrong. Try again.");
                        }
                        break;
                    case "settings_device":
                        if (data.imei == inputobj.imei) {
                            let thename = "Dashboard " + whatTitle + " Edited";
                            let theaction = "User of Identification Number " + userinfo.pk.toString() + " has edited a " + what + " of Identification Number " + data.id + " and Name " + data.name + ".";
                            let theuser = userinfo.user;
                            let thestatus = "Active";

                            var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                            try {
                                fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                                    resp.json().then((data) => {
                                        if (data.name) {
                                            alert("Editted successfully.");
                                            location.reload();
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
                            alert("Something went wrong. Try again.");
                        }
                        break;
                    case "settings_produce":
                        if (data.name == inputobj.name) {
                            let thename = "Dashboard " + whatTitle + " Edited";
                            let theaction = "User of Identification Number " + userinfo.pk.toString() + " has edited a " + what + " of Identification Number " + data.id + " and Name " + data.name + ".";
                            let theuser = userinfo.user;
                            let thestatus = "Active";

                            var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                            try {
                                fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                                    resp.json().then((data) => {
                                        if (data.name) {
                                            alert("Editted successfully.");
                                            location.reload();
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
                            alert("Something went wrong. Try again.");
                        }
                        break;
                }
            });
        });
    }
    catch (err) {
        console.log(err);
    }
    return false;
}


function deleteFormRecord(elem) {
    var durl = apilink;
    var form_name = elem.getAttribute("data-form-name");
    var inputobj = $('form').serializeObject();
    var dataobj = JSON.stringify(inputobj);
    var what, whatTitle;

    switch (form_name) {
        case "settings_farmer":
            durl += "farmers/" + getid;
            what = "farmer";
            whatTitle = "Farmer";
            break;
        case "settings_factory":
            durl += "factories/" + getid;
            what = "factory";
            whatTitle = "Factory";
            break;
        case "settings_device":
            durl += "devices/" + getid;
            what = "device";
            whatTitle = "Device";
            break;
        case "settings_fro":
            durl += "clerks/" + getid;
            what = "clerk";
            whatTitle = "Clerk";
            break;
        case "settings_produce":
            durl += "produce/" + getid;
            what = "produce";
            whatTitle = "Produce";
            break;
    }
    try {
        fetch(durl, { method: 'delete', headers: getheaders, body: dataobj, }).then((resp) => {
            if (resp.ok) {
                let thename = "Dashboard " + whatTitle + " Deleted";
                let theaction = "User of Identification Number " + userinfo.pk.toString() + " has deleted a " + what + " of Identification Number " + getid + ".";
                let theuser = userinfo.user;
                let thestatus = "Active";

                var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                try {
                    fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                        resp.json().then((data) => {
                            if (data.name) {

                                alert("Deleted successfully.");
                                switch (form_name) {
                                    case "settings_fro":
                                        location.assign(applink.trim() + 'fro/');
                                        break;
                                    case "settings_farmer":
                                        location.assign(applink.trim() + 'farmers/');
                                        break;
                                    case "settings_factory":
                                        location.assign(applink.trim() + 'factories/');
                                        break;
                                    case "settings_device":
                                        location.assign(applink.trim() + 'devices/');
                                        break;
                                    case "settings_produce":
                                        location.assign(applink.trim() + 'products/');
                                        break;
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
                alert("Something went wrong. Try again.");
            }
        });
    }
    catch (err) {
        console.log(err);
    }
    return false;
}

function redirectNotFound() {
    setTimeout(function () {
        var checkdata = $("input#id").val();
        if (!checkdata) {
            location.assign(applink.trim() + '404/');
        }
    }, 3000);
}