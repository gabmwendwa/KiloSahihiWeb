function loadtable(tableid) {
    var t = $(tableid).DataTable({ "columnDefs": [{ "searchable": false, "orderable": false, "targets": 0 }], });
    t.on('order.dt search.dt', function () { t.column(0, { search: 'applied', order: 'applied' }).nodes().each(function (cell, i) { cell.innerHTML = i + 1; }); }).draw();
}

var getheaders = new Headers();
getheaders.append("Authorization", "Token " + localStorage.session_token);
getheaders.append("Content-Type", "application/json");
var tablebody = document.getElementById('result-body');

function getFarmerList() {
    try {
        fetch("http://localhost:8003/api/farmers", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    for (var i = 0; i < data.length; i++) {
                        tabledata += '<tr class="gradeA pointer" title="' + data[i]["name"] + '." onclick="window.open(\''+applink.trim()+'settings/farmer/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>#</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["username"] + '</td>';
                        tabledata += '<td>' + data[i]["national_id"] + '</td>';
                        tabledata += '<td>' + data[i]["phone_number"] + '</td>';
                        tabledata += '<td>' + data[i]["bank_branch"] + '</td>';
                        tabledata += '<td>' + data[i]["bank_account_name"] + '</td>';
                        tabledata += '<td>' + data[i]["bank_account"] + '</td>';
                        tabledata += '<td>' + data[i]["acres"] + '</td>';
                        tabledata += '<td>' + data[i]["lat"] + ", " + data[i]["lon"] + '</td>';
                        tabledata += '<td>' + data[i]["factory"]["name"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                App.dataTables();
                loadtable("#table4");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}


function getFactoriesList() {
    try {
        fetch("http://localhost:8003/api/factories", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    for (var i = 0; i < data.length; i++) {
                        tabledata += '<tr class="gradeA pointer" title="' + data[i]["name"] + '." onclick="window.open(\''+applink.trim()+'settings/factory/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>#</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["product"]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["cooperative"]["name"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                App.dataTables();
                loadtable("#table4");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}


function getDeviceList() {
    try {
        fetch("http://localhost:8003/api/devices", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    for (var i = 0; i < data.length; i++) {
                        tabledata += '<tr class="gradeA pointer" title="' + data[i]["name"] + '." onclick="window.open(\''+applink.trim()+'settings/device/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>#</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["imei"] + '</td>';
                        tabledata += '<td>' + data[i]["factory"]["name"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                App.dataTables();
                loadtable("#table4");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}


function getProductList() {
    try {
        fetch("http://localhost:8003/api/produce", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    for (var i = 0; i < data.length; i++) {
                        tabledata += '<tr class="gradeA pointer" title="' + data[i]["name"] + '." onclick="window.open(\''+applink.trim()+'settings/product/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>#</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["status"] + '</td>';
                        tabledata += '<td>' + data[i]["reg_date"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                App.dataTables();
                loadtable("#table4");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}

function getFROList() {
    try {
        fetch("http://localhost:8003/api/clerks", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    for (var i = 0; i < data.length; i++) {
                        tabledata += '<tr class="gradeA pointer" title="' + data[i]["name"] + '." onclick="window.open(\''+applink.trim()+'settings/fro/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<td>#</td>';
                        tabledata += '<td>' + data[i]["name"] + '</td>';
                        tabledata += '<td>' + data[i]["username"] + '</td>';
                        tabledata += '<td>' + data[i]["national_id"] + '</td>';
                        tabledata += '<td>' + data[i]["phone_number"] + '</td>';
                        tabledata += '<td>' + data[i]["factory"]["name"] + '</td>';
                        tabledata += '</tr>';
                    }
                    tablebody.innerHTML = tabledata;
                }
                App.dataTables();
                loadtable("#table4");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}

function getTransactionList() {
    try {
        fetch("http://localhost:8003/api/transactions", { method: 'get', headers: getheaders, }).then((resp) => {
            resp.json().then((data) => {
                var tabledata = "";
                if (data.length) {
                    for (var i = 0; i < data.length; i++) {
                        // tabledata += '<tr class="gradeA pointer" title="' + data[i]["name"] + '." onclick="window.open(\''+applink.trim()+'view/transaction/' + data[i]["id"] + '/\', \'_self\')">';
                        tabledata += '<tr class="gradeA pointer" title="' + data[i]["name"] + '.">';
                        tabledata += '<td>#</td>';
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
                App.dataTables();
                loadtable("#table4");
            });
        });
    }
    catch (err) {
        console.log(err);
    }
}