function loadtable(tableid) {
    $("#" + tableid).DataTable({
        lengthChange: !1,
        buttons: [
            "copy",
            "excel",
            "pdf",
            "print"
        ]
    }).buttons().container().appendTo("#" + tableid + "_wrapper .col-md-6:eq(0)")
}

var tablebody = document.getElementById('result-body');

function getFarmerList() {
    try {
        fetch(apilink + "farmers", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";

                if (data.length) {
                    var j = 0;
                    for (var i = 0; i < data.length; i++) {
                        j += 1;
                        tabledata += '<tr class="custom-pointer" title="Edit." onclick="window.open(\'' + applink.trim() + 'settings/farmer/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>' + j.toString() + '</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["username"] + '</td>';
                        tabledata += '<td>' + data[i]["national_id"] + '</td>';
                        tabledata += '<td>' + data[i]["phone_number"] + '</td>';
                        tabledata += '<td>' + data[i]["bank_branch"] + '</td>';
                        tabledata += '<td>' + data[i]["bank_account_name"] + '<br>[' + data[i]["bank_account"] + ']</td>';
                        // tabledata += '<td>' + data[i]["bank_account_name"] + '</td>';
                        // tabledata += '<td>' + data[i]["bank_account"] + '</td>';
                        tabledata += '<td>' + data[i]["acres"] + '</td>';
                        tabledata += '<td>' + data[i]["lat"] + ", " + data[i]["lon"] + '</td>';
                        tabledata += (data[i]["factory"] == null) ? '<td>empty</td>' : '<td>' + data[i]["factory"]["name"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                    loadtable("datatable-buttons");
                }
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}


function getFactoriesList() {
    try {
        fetch(apilink + "factories", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    var j = 0;
                    for (var i = 0; i < data.length; i++) {
                        j += 1;
                        tabledata += '<tr class="custom-pointer" title="Edit." onclick="window.open(\'' + applink.trim() + 'settings/factory/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>' + j.toString() + '</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["product"]["name"] + '</td>';
                        tabledata += (data[i]["cooperative"] == null) ? '<td>empty</td>' : '<td>' + data[i]["cooperative"]["name"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                loadtable("datatable-buttons");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}


function getDeviceList() {
    try {
        fetch(apilink + "devices", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    // console.log(data);
                    // console.log(data[0]);
                    var j = 0;
                    for (var i = 0; i < data.length; i++) {
                        j += 1;
                        tabledata += '<tr class="custom-pointer" title="Edit." onclick="window.open(\'' + applink.trim() + 'settings/device/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>' + j.toString() + '</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["imei"] + '</td>';
                        tabledata += (data[i]["factory"] == null) ? '<td>empty</td>' : '<td>' + data[i]["factory"]["name"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                loadtable("datatable-buttons");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}


function getProductList() {
    try {
        fetch(apilink + "produce", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    var j = 0;
                    for (var i = 0; i < data.length; i++) {
                        j += 1;
                        tabledata += '<tr class="custom-pointer" title="Edit." onclick="window.open(\'' + applink.trim() + 'settings/product/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>' + j.toString() + '</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["status"] + '</td>';
                        tabledata += '<td>' + data[i]["reg_date"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                loadtable("datatable-buttons");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}

function getFROList() {
    try {
        fetch(apilink + "clerks", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    var j = 0;
                    for (var i = 0; i < data.length; i++) {
                        j += 1;
                        tabledata += '<tr class="custom-pointer" title="Edit." onclick="window.open(\'' + applink.trim() + 'settings/fro/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>' + j.toString() + '</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["username"] + '</td>';
                        tabledata += '<td>' + data[i]["national_id"] + '</td>';
                        tabledata += '<td>' + data[i]["phone_number"] + '</td>';
                        tabledata += (data[i]["factory"] == null) ? '<td>empty</td>' : '<td>' + data[i]["factory"]["name"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                loadtable("datatable-buttons");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}

function getTransactionList() {
    try {
        fetch(apilink + "transactions", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    var j = 0;
                    for (var i = data.length - 1; i >= 0; i--) {
                        j += 1;
                        // tabledata += '<tr class="custom-pointer" title="Edit." onclick="window.open(\''+applink.trim()+'view/transaction/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<tr>';
                        tabledata += '<td>' + j.toString() + '</td>';
                        tabledata += '<td>' + data[i]["tx_code"] + '</td>';
                        tabledata += '<td>' + data[i]["weight"] + '</td>';
                        tabledata += '<td>' + data[i]["total_payout"] + '</td>';
                        tabledata += '<td>' + data[i]["farmer"]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["device"]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["produce"]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["tx_date"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                loadtable("datatable-buttons");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}

function getAuditList() {
    try {
        fetch(apilink + "audits", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                var j = 0;
                if (data.length) {
                    for (var i = data.length - 1; i >= 0; i--) {
                        console.log(data);
                        console.log(data[0]);
                        j += 1;
                        // tabledata += '<tr class="custom-pointer" title="Edit." onclick="window.open(\''+applink.trim()+'settings/farmer/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<tr>';
                        tabledata += '<td>' + j.toString() + '</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["action"] + '</td>';
                        tabledata += '<td>' + data[i]["user"] + '</td>';
                        tabledata += '<td>' + data[i]["date"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                loadtable("datatable-buttons");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}
