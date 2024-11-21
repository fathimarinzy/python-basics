// $(document).ready(function(){
//     $("p").hide();
// })


// $(document).ready(function(){
//     $("button").click(function(){
//          $("p").hide();
//     })
// })


// $(document).ready(function(){
//     $("button").click(function(){
//         $("button").hide();
//     })
// })
// //  or
// $(document).ready(function(){
//     $("button").click(function(){
//         $(this).hide();
//     })
// })

// id and class hiding
// $(document).ready(function(){
//         $("#b1").click(function(){
//             $("#p1").hide();
//         })

//         $(".b2").click(function(){
//             $(".p2").hide();
//         })

//         $("button").click(function(){
//             $("p").hide();
//         })

//         $("button").click(function(){
//             $(this).hide();
//         })
// })


// jquery effects
// $(document).ready(function(){
//     $("#b1").click(function(){
//         $("p").hide();
//     })

//     $("#b2").click(function(){
//         $("p").show();
//     })

//     $("#b3").click(function(){
//         $("p").toggle();
//     })

// })

// jquery event methods
// mouseevents - click, dblclick = doubleclick, mouseenter, mouseleave,hover
// key board events - keypress, keydown,keyup
// form events - submit, change , focus, blur
// document/window - load, resize, scroll, unload

// $(document).ready(function(){
//     $("#b1").click(function(){
//                 $("p").toggle();
//         })
    // $("#b2").dblclick(function(){
    //     $("p").hide();
    // })
    // $("#b3").mouseenter(function(){
    //     $("p").hide();
    // })
    // $("#b4").mouseleave(function(){
    //     $("p").hide();
    // })
    // $("#b5").hover(function(){
    //     $("p").hide();
    // })
   
    // $("#b6").keypress(function(){
    //     $("p").hide();
    // })

    // $("#b7").keydown(function(){
    //     $("p").hide();
    // })

    // $("#b8").keyup(function(){
    //     $("p").hide();
    // })

    
//     $("input").focus(function(){
//         $(this).css("background-color","red");
//     })

//     $("input").blur(function(){
//         $(this).css("background-color","green");
//     })

//     $("#b").click(function(){
//             $("p").css("color","blue");
//         })

//     $("p").click(function(){
//             $("p").css("color","blue");
//         })

//     $("p").hover(function(){
//             $("p").css("color","blue");
//         })
// })



// class2
// $(document).ready(function(){
    // sliding methods
    // $("#b1").click(function(){
    //     $("div").slideUp();
    // })
    // $("#b1").click(function(){
    //     $("div").slideDown();
    // })
    // $("#b1").click(function(){
    //     $("div").slideToggle();
    // })
    // fading methods
    // $("#b2").click(function(){
    //     $("div").fadeIn(3000);
    // })
    // $("#b1").click(function(){
    //     $("div").fadeOut(3000);
    // })
    // $("#b3").click(function(){
    //     $("div").fadeToggle(3000);
    // })
    // $("#b3").click(function(){
    //     $("div").fadeTo(3000);
    // })
// })


// callback function
// $(document).ready(function(){
//     $("#b1").click(function(){
//         $("p").hide(1000);
//             alert("The paragraph is now hidden");
//     })
// })

// $(document).ready(function(){
//     $("#b1").click(function(){
//         $("p").hide("slow",function(){
//             alert("The paragraph is now hidden");
//         });
//     });
// });

// $(document).ready(function(){
//     $("#b1").click(function(){
//         $("div").slideUp(2000).slideDown(2000).hide(2000).show(2000);
//     });
// });

// $(document).ready(function(){
//     $("#b1").click(function(){
//         $("div").slideUp(2000).slideDown(2000).css("background-color","green").fadeOut(2000).fadeIn(2000).css("background-color","red").hide(2000).show(2000).css("background-color","yellow");
//     });
// });


// $(document).ready(function(){
//     $("#b1").click(function(){
//         $("div").slideUp(2000).slideDown(2000,(function(){
//             $("div").css("background-color","green");
//                 })).fadeOut(2000).fadeIn(2000,function(){
//             $("div").css("background-color","red");
//                 }).hide(2000).show(2000,function(){
//             $("div").css("background-color","yellow");
//         });
//     });
// });


$(document).ready(function(){
    $("#b1").click(function(){
        $("p").append("<b>Appended text</b>");
    
    });
    $("#b2").click(function(){
        $("p").prepend("<i>Appended item</i>");
    
    });
    $("#b3").click(function(){
        $("p").before("<b>Appended text</b>");
    
    });
    $("#b4").click(function(){
        $("p").after("<i>Appended item</i>");
    
    });
});