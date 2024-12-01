// to get date
function display(){
    var d=new Date();
    document.getElementById("kkk").innerHTML=d;
    document.getElementById("kkk").innerHTML=d.getDate();
    document.getElementById("kkk").innerHTML=d.getMonth();
    document.getElementById("kkk").innerHTML=d.getDay();
    document.getElementById("kkk").innerHTML=d.getHours();
    document.getElementById("kkk").innerHTML=d.getMinutes();
    document.getElementById("kkk").innerHTML=d.getSeconds();
    document.getElementById("kkk").innerHTML=d.getFullYear();

}

// to set date
// function display(){
//     var d=new Date();
//     d.setDate(10);
//     d.setFullYear(2024);
//     document.getElementById("kkk").innerHTML=d;

// }

// math functions
// function display(){
//     // var a=9;
//     // document.write(Math.sqrt(a)+"<br>");

//     var a=-9;
//     document.write(Math.abs(a)+"<br>");
//     document.write(Math.min(10,20,30,40)+"<br>");
//     document.write(Math.max(10,20,30,40)+"<br>");
//     document.write(Math.pow(10,2)+"<br>");
//     document.write(Math.round(7.62)+"<br>");
//     document.write(Math.random()+"<br>");
//     document.write(Math.ceil(1.9)+"<br>");
//     document.write(Math.ceil(1.1)+"<br>");
//     document.write(Math.floor(1.1)+"<br>");
//     document.write(Math.floor(1.9)+"<br>");

// }


// string functions
// =================================
// var txt="javascript";
// document.write(txt+"<br>");


// var txt="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
// document.write(txt.length+"<br>");


// var txt="javascript";
// document.write(txt[5]+"<br>");


// var txt="java";
// var txt1="script"
// document.write(txt.concat(txt1)+"<br>");


// var x="HELLO";
// document.write(x.toLowerCase()+"<br>");


// var x="HELLO";
// document.write(x.toUpperCase()+"<br>");


// var a="     java      ";
// document.write(a.trim()+"<br>");

// var a="java      ";
// document.write(a.trim()+"<br>");

// var a="     java";
// document.write(a.trim()+"<br>");

// var a="j a v a";
// document.write(a.trim()+"<br>");

// var a="javascript";
// document.write(a.slice(1,5)+"<br>");
// document.write(a.slice(-5,-1)+"<br>");

// var a="javascript";
// document.write(a.substring(1,5)+"<br>");
// // document.write(a.substring(-5,-1)+"<br>");

// var a="john snow";
// document.write(a.replace("snow","down")+"<br>");

// var a="hello";
// document.write(a.charAt(1)+"<br>");

// var a="rain in spain";
// document.write(a.startsWith("rain"));
// document.write(a.endsWith("in"));
// document.write("<br>");

// regular expressions
// ====================================
var x="javascript is easy"
var y=x.search(/v/)
document.write(y+"<br>")

var x="javascript is easy"
var y=x.search(/a/)
document.write(y+"<br>")

var y="welcome to javascript "
var x=/[els]/g
res=y.match(x)
document.write(res+"<br>")

var y="w9*el5co0me t8o jav&a1245scr7ipt"
var x=/[^0-7]/g
res=y.match(x)
document.write(res+"<br>")

var y="w9*el5co0me t8o jav&a1245scr7ipt"
var x=/[0-7]/g
res=y.match(x)
document.write(res+"<br>")

var y="w9*el5co0me t8o jav&a1245scr7iptzz"
var x=/[l|z]/g
res=y.match(x)
document.write(res+"<br>")


var y="welcome to javascript "
var x=/[^abcwj]/g
res=y.match(x)
document.write(res+"<br>")


var y="welcome111111 t8o java1script "
var x=/[\d]/g
res=y.match(x)
document.write(res+"<br>")

var y="welcome111111 t8o java1script "
var x=/[\w]/g
res=y.match(x)
document.write(res+"<br>")