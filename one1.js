// window.alert("welcome");

document.write("welcome");
document.write("<i>welcome</i>");

// console.log("welcome to javascript");

// document.getElementById("h").innerHTML="changed";
// =====================================================

function display(){
    document.getElementById("h").innerHTML="changed";
}

function display1(){
    document.getElementById("h").innerHTML="changed";
}

function display2(){
    document.getElementById("h").innerHTML="changed";
}

// =======================================================
// var,let,const

// var
// document.write("<br>");
// var a=10;
// document.write(a);
// document.write("<br>");

// var a=10;
// var a=20;
// document.write(a);
// document.write("<br>");

// a=100;
// var a;
// document.write(a);
// document.write("<br>");

// var a;
// a=101;
// document.write(a);
// document.write("<br>");

// ==========================
// let
// let b=20;
// document.write(b);
// document.write("<br>");

// once b is initialised so same name cant be possible
// let b=20;
// document.write(b);
// document.write("<br>");

// not possible
// let c=20;
// let c=30;
// document.write(c);
// document.write("<br>");

// let d;
// d=500;
// document.write(d);
// document.write("<br>");


// t=100;
// let t;
// document.write(t);
// document.write("<br>");

// ===============================
// const
// only this is possible
const r=10000;
document.write(r);
document.write("<br>");

// not possible
// const r=10000;
// document.write(r);
// document.write("<br>");

// not possible
// const rr=10000;
// const rr=10000;
// document.write(rr);
// document.write("<br>");


// not possible
// const y;
// y=10000;
// document.write(y);
// document.write("<br>");


// not possible
// z=10000;
// const z;
// document.write(z);
// document.write("<br>");

// ====================================================================
function display(){
    var x = document.getElementById("h");
                // x.style.fontSize = "25px";
                // x.style.color = "red";
                // x.style.backgroundColor="yellow";
                x.style.cssText="color:red;text-align:center;"
}