// function display(y){
//     var d=document.getElementById("input1").value
//     window.alert(d)
//     window.alert(y)
// }

// ===============================================
// javascript operators======

// ===========
// arithmetic operators
// var a=10;
// var b=20;
// document.write(a+b)
// document.write("<br>")

// var a=100;
// var b=20;
// document.write(a-b)
// document.write("<br>")

// var a=10;
// var b=20;
// document.write(a*b)
// document.write("<br>")

// var a=103;
// var b=20;
// document.write(a/b)
// document.write("<br>")

// var a=103;
// var b=20;
// document.write(a%b)
// document.write("<br>")

// var a=100;
// a++
// document.write(a)
// document.write("<br>")

// var a=100;
// a--
// document.write(a)
// document.write("<br>")

// to add two numbers
// function add(){
//     var d=document.getElementById("1").value
//     var t=document.getElementById("2").value
//     // to get the type of input field
//     // console.log(typeof(d)) 
//     // console.log(typeof(t))
//     // to change the string into number
//     x1=Number(d)
//     x2=Number(t)
//     // console.log(typeof(x1)) 
//     // console.log(typeof(x2))
//     // console.log(x1+x2)
//     document.write(x1+x2)

// }

// ===================================================
// comparison operators
// var a=25;
// var b=25;
// document.write(a==b )
// document.write("<br>")

// var a=25;
// var b="25";
// document.write(a==b)
// document.write("<br>")

// var a=25;
// var b=25;
// document.write(a===b )
// document.write("<br>")

// var a=25;
// var b="25";
// document.write(a===b)
// document.write("<br>")


// =============================================
// logical operators
// var a=25;
// var b=25;
// document.write(a==b && a>=b)
// document.write("<br>")


// var a=25;
// var b=25;
// document.write(a==b || a>=b)
// document.write("<br>")

// var a=25;
// var b=25;
// document.write(!(a==b))
// document.write("<br>")

// ===============================================
// assignment operator
// var a=25;
// a+=1
// document.write(a)
// document.write("<br>")

// var a=25;
// a-=1
// document.write(a)
// document.write("<br>")

// var a=25;
// a*=2
// document.write(a)
// document.write("<br>")

// var a=25;
// a/=4
// document.write(a)
// document.write("<br>")

// var a=25;
// a%=3
// document.write(a)
// document.write("<br>")

// =====================================================
// conditional statements
// var x=20;
// if(x>0){
//     window.alert("x is greater than zero")
// }
// else if (x==0){
//     window.alert("x is zero")
// }
// else{
//     window.alert("x is neagtive")
// }


// to check odd or even number
// function check(){
//     var d=document.getElementById("1").value
//     console.log(typeof(d))
//     x=Number(d)
//     if (x%2==0){
//         document.write("even number")
//     }
//     else{
//         document.write("odd number")
//     }
    
// }

// to check the day
function week(){
    var d=document.getElementById("1").value
    if (d=="sunday" && "Monday"){
        window.alert("week end")
    }
    else if(d=="Tuesday"||"Wednesday"||"Thursday"||"Friday"){
        window.alert("week day")
    }
    else{
        window.alert("invalid")
    }


}