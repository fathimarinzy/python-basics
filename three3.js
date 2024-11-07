// for loop
// ===================================
for(i=0;i<5;i++){
    // console.log(i)
    // document.write(i)
    document.getElementById("h").innerHTML=i
}

// javascript arrays
// =========================================
var cars=['saab','volvo','bmw'];
for (var i in cars){
    console.log(i)
    document.write(i)

}

var cars=['saab','volvo','bmw'];
for (var i of cars){
    console.log(i)
    document.write(i)

}

// javascript objects
// =========================================
var person={firstname:'john',lastname:'doe',age:46};
for (var i in person){
    console.log(person[i])
}

// =======================================

var p1=document.createElement("p");
p1.textContent="welcome to new html content" ;
document.body.append(p1)

var ul=document.createElement("ul")
var li=document.createElement("li")
li.textContent="click"
ul.append(li)
document.body.append(ul)

var x=document.createElement("button");
x.textContent="hai hello"
document.body.append(x)