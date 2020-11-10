var getheaders = new Headers();
getheaders.append("Authorization", "Token " + localStorage.session_token);
getheaders.append("Content-Type", "application/json");
var reg_form = $('#register_form').parsley();


function getOptionsList(what, selectid) {
    var durl = "http://localhost:8003/api/";
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

if(reg_form.isValid()) {
    document.getElementById("submit-btn").addEventListener("click", function (event) {
        event.preventDefault();
        submitRegisterForm();
    });
    
    document.getElementById("register_form").addEventListener("submit", function (event) {
        event.preventDefault()
    });
}

function submitRegisterForm() {
    console.log("create submit object");
}