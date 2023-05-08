/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: conversation.js
 * DATE: May 5, 2023
 */

//Confirmation for requesting a match. 
function confSubmit(form) {
    if (confirm("Are you sure you want to request a match?")) {        
        document.getElementById("confirmMatch").value = "True";
    }

    else {
       alert("No match request submitted");
       document.getElementById("confirmMatch").value = "False";
       return 0;
    }
}