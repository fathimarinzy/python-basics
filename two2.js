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
// function week(){
//     var d=document.getElementById("1").value.toLowerCase();
//     if (d=="sunday" || d=="monday"){
//         window.alert("week end")
//     }
//     else if(d=="tuesday"||d=="wednesday"||d=="thursday"||d=="friday"){
//         window.alert("week day")
//     }
//     else{
//         window.alert("invalid")
//     }
// }

// ======================================================
// switch

// var fruits="Apple"
// switch(fruits){
//     case "Banana":
//         text="Banana is good";
//         console.log(text);
//         break;
//     case "Orange":
//         text="Orange is good";
//     case "Apple":
//         text="Apple is Awesome";
//         console.log(text);
//         break;
//     default :
//         text="I have never heard of that fruit...";
//         console.log(text);
// }
// eg
// ope="+"
// var a=10;
// var b=20;
// switch(ope){
//     case "+":
//         res=a+b
//         document.write(res)
//         break;
//     case "-":
//         res=a-b
//         document.write(res)
//         break;
//     case "*":
//         res=a*b
//         document.write(res)
//         break;
//     case "\\":
//         res=a+b
//         document.write(res)
//         break;
//     default:
//         document.write("invalid")   

// }

// ====================================
// while and do while
// var i=0;
// while(i<5){
//     console.log(i);
//     i++
// }

// var i=0;
// do{
//     console.log(i);
//     i++
// }while(i<5)


// var i=0;
// while(i>5){
//     console.log(i);
//     i++
// }


// var i=0;
// do{
//     console.log(i);
//     i++
// }while(i>5)


// factorial of a number
// var i=5;
// var fact=1;
// while(i>0){
//     fact*=i;
//     i--
// }
// // document.write(fact);
// console.log(fact);

// sum of first 10 numbers

var i=1;
var sum=0;
while(i<=10){
    sum+=i;
    i++
}
console.log(sum);