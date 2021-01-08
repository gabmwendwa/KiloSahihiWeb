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

/*
$(function () {
    $('form').submit(function () {
        $('#result').text(JSON.stringify($('form').serializeObject()));
        return false;
    });
});
*/

var reg_form = $('#register_form').parsley();


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
                        optionsdata += '<option value="' + data[i]["id"] + '">' + data[i]["name"] + '</option>';
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

document.getElementById("submit-btn").addEventListener("click", function (event) {
    if (reg_form.isValid()) {
        event.preventDefault();
        submitRegisterForm(this);
    }
});

document.getElementById("register_form").addEventListener("submit", function (event) {
    if (reg_form.isValid()) {
        event.preventDefault()
    }
});

function submitRegisterForm(elem) {
    var durl = apilink;
    var form_name = elem.getAttribute("data-form-name");
    var inputobj = $('form').serializeObject();
    var dataobj = JSON.stringify(inputobj);
    var what, whatTitle;

    switch (form_name) {
        case "register_farmer":
            durl += "farmers";
            what = "farmer";
            whatTitle = "Farmer";
            break;
        case "register_factory":
            durl += "factories";
            what = "factory";
            whatTitle = "Factory";
            break;
        case "register_device":
            durl += "devices";
            what = "device";
            whatTitle = "Device";
            break;
        case "register_fro":
            durl += "clerks";
            what = "clerk";
            whatTitle = "Clerk";
            break;
        case "register_produce":
            durl += "produce";
            what = "produce";
            whatTitle = "Produce";
            break;
    }
    try {
        fetch(durl, { method: 'post', headers: getheaders, body: dataobj, }).then((resp) => {
            resp.json().then((data) => {
                //console.log(data);
                switch (form_name) {
                    case "register_fro":
                    case "register_farmer":
                        if (data.username == inputobj.username) {
                            let thename = "Dashboard "+whatTitle+" Registration";
                            let theaction = "User of Identification Number " + userinfo.pk.toString() + " has registered a new "+what+" of Identification Number "+data.id+" and Username "+data.username+".";
                            let theuser = userinfo.user;
                            let thestatus = "Active";

                            var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                            try {
                                fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                                    resp.json().then((data) => {
                                        if (data.name) {
                                            alert("Registered successfully.");
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
                            if (data.username)
                                alert("Username already exists. Please use another one.");
                            else if (data.national_id)
                                alert("National ID already exists. Please use another one.");
                            else if (data.phone_number)
                                alert("Phone number already exists. Please use another one.");
                            else
                                alert("Something went wrong. Try again.");
                        }
                        break;
                    case "register_factory":
                        if (data.name == inputobj.name) {
                            let thename = "Dashboard "+whatTitle+" Registration";
                            let theaction = "User of Identification Number " + userinfo.pk.toString() + " has registered a new "+what+" of Identification Number "+data.id+" and Name "+data.name+".";
                            let theuser = userinfo.user;
                            let thestatus = "Active";

                            var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                            try {
                                fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                                    resp.json().then((data) => {
                                        if (data.name) {
                                            alert("Registered successfully.");
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
                            if (data.name)
                                alert("Factory name already exists. Please use another one.");
                            else
                                alert("Something went wrong. Try again.");
                        }
                        break;
                    case "register_device":
                        if (data.imei == inputobj.imei) {
                            let thename = "Dashboard "+whatTitle+" Registration";
                            let theaction = "User of Identification Number " + userinfo.pk.toString() + " has registered a new "+what+" of Identification Number "+data.id+" and Name "+data.name+".";
                            let theuser = userinfo.user;
                            let thestatus = "Active";

                            var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                            try {
                                fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                                    resp.json().then((data) => {
                                        if (data.name) {
                                            alert("Registered successfully.");
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
                            if (data.imei)
                                alert("IMEI already exists. Please use another one.");
                            else
                                alert("Something went wrong. Try again.");
                        }
                        break;
                    case "register_produce":
                        if (data.name == inputobj.name) {
                            let thename = "Dashboard "+whatTitle+" Registration";
                            let theaction = "User of Identification Number " + userinfo.pk.toString() + " has registered a new "+what+" of Identification Number "+data.id+" and Name "+data.name+".";
                            let theuser = userinfo.user;
                            let thestatus = "Active";

                            var auditobj = { "name": thename, "action": theaction, "user": theuser, "status": thestatus };
                            try {
                                fetch(apilink + "audits", { method: 'post', headers: getheaders, body: JSON.stringify(auditobj), }).then((resp) => {
                                    resp.json().then((data) => {
                                        if (data.name) {
                                            alert("Registered successfully.");
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
                            if (data.name)
                                alert("Product name already exists. Please use another one.");
                            else
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