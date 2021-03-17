var options1={series:[{data:[rand1[0],rand1[1],rand1[2],rand1[3],rand1[4],rand1[5]]}],fill:{colors:["#008000"]},chart:{type:"bar",width:70,height:40,sparkline:{enabled:!0}},plotOptions:{bar:{columnWidth:"50%"}},labels:[1,2,3,4,5,6,7,8,9,10,11],xaxis:{crosshairs:{width:1}},tooltip:{fixed:{enabled:!1},x:{show:!1},y:{title:{formatter:function(e){return""}}},marker:{show:!1}}};

var chart1=new ApexCharts(document.querySelector("#farmers-chart"),options1);

chart1.render();

var options={fill:{colors:["#f42434"]},series:[rand2],chart:{type:"radialBar",width:45,height:45,sparkline:{enabled:!0}},dataLabels:{enabled:!1},plotOptions:{radialBar:{hollow:{margin:0,size:"60%"},track:{margin:0},dataLabels:{show:!1}}}};

var chart=new ApexCharts(document.querySelector("#factories-chart"),options);

chart.render();

options={fill:{colors:["#008000"]},series:[rand3],chart:{type:"radialBar",width:45,height:45,sparkline:{enabled:!0}},dataLabels:{enabled:!1},plotOptions:{radialBar:{hollow:{margin:0,size:"60%"},track:{margin:0},dataLabels:{show:!1}}}};

(chart=new ApexCharts(document.querySelector("#fros-chart"),options)).render();

var options2={series:[{data:[rand1[4],rand1[1],rand1[5],rand1[3],rand1[0],rand1[2]]}],fill:{colors:["#f42434"]},chart:{type:"bar",width:70,height:40,sparkline:{enabled:!0}},plotOptions:{bar:{columnWidth:"50%"}},labels:[1,2,3,4,5,6,7,8,9,10,11],xaxis:{crosshairs:{width:1}},tooltip:{fixed:{enabled:!1},x:{show:!1},y:{title:{formatter:function(e){return""}}},marker:{show:!1}}};

var chart2=new ApexCharts(document.querySelector("#devices-chart"),options2);

chart2.render();

options={chart:{height:339,type:"line",stacked:!1,toolbar:{show:!1}},stroke:{width:[0,2,4],curve:"smooth"},plotOptions:{bar:{columnWidth:"30%"}},colors:["#008000"],series:[{name:"Desktops",type:"column",data:[23,11,22,27,13,22,37,21,44,22,30]}],fill:{opacity:[.85,.25,1],gradient:{inverseColors:!1,shade:"light",type:"vertical",opacityFrom:.85,opacityTo:.55,stops:[0,100,100,100]}},labels:["01/01/2003","02/01/2003","03/01/2003","04/01/2003","05/01/2003","06/01/2003","07/01/2003","08/01/2003","09/01/2003","10/01/2003","11/01/2003"],markers:{size:0},xaxis:{type:"datetime"},yaxis:{title:{text:"Points"}},tooltip:{shared:!0,intersect:!1,y:{formatter:function(e){return void 0!==e?e.toFixed(0)+" points":e}}},grid:{borderColor:"#f1f1f1"}};

(chart=new ApexCharts(document.querySelector("#transactions-analytics-chart"),options)).render();