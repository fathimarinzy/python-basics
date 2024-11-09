function myFunction(){
    alert("hello");
    document.getElementById("h").innerHTML="changed after 3000 miilisecnds"
}


    // js popup boxes 
//  =========================================
// alert
function alertbox(){
    alert("hello")
}

// conform
// function conformbox(){
//     var x;
// if (confirm("press a button!")==true){
//         x="you pressed ok";
//         document.getElementById("h1").innerHTML=x

// }else{
//         x="you pressed cancel";
//         document.getElementById("h1").innerHTML=x

// }
// }
// prompt
// function promptbox(){
//     var person=prompt("please enter your name");
// if(person!=null){
//     document.getElementById("h2").innerHTML="Hello"+person+" !how are you";
// }

// }

// value kodkathe click cheyumbo consolil null fiels varum else case work ayit
// function promptbox(){
//     var person=prompt("please enter your name");
// if(person){
//     console.log(person,"*****")

//     document.getElementById("h2").innerHTML="Hello"+person+" !how are you";
// }
// else{
//     console.log(person,"null field")
// }

// }

// exception handling
// =========================================
// function display(){
//     try{
//         alet('hello')

//     }
//     catch(e){
//         console.log(e)
//         console.log("alert is the corresct spelling")
//     }
//     finally{
//         console.log("always executes")
//     }
// }

function display(){
    try{
        // alet('hello')
        var a=10;
        var b=0;
       
        if (b==0){
            throw("zero division error")
        }
        else{
            alert(a/b)
        }

    }   
    catch(e){
        console.log(e)
        console.log("alert is the correct spelling")
    }
    finally{
        console.log("always executes")
    }
}
