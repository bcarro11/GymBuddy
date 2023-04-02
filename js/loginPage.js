/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: loginPage.js
 * DATE: April 4, 2023
 */
const submit = document.getElementById("submitBtn").addEventListener("click", submitFunction);
const createAcc = document.getElementById("createAccountBtn").addEventListener("click", goToCreateAcc);


function submitFunction(){
    var stat = document.getElementById("usrInput").value;
    document.getElementById("loginError").innerHTML = stat;
    // if (stat == "" || stat == null) {
    //     document.getElementById("loginError").innerHTML = "error";
    // } else {
    //     document.getElementById("loginError").innerHTML = "Noerror";
    // }
}

function goToCreateAcc(){
    window.location.href="createAccount.html";
    
}