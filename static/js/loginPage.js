/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: loginPage.js
 * DATE: April 4, 2023
 */



/**
 * Handles login page buttons.
 * Routes to profile page or create account.
 */
const createAcc = document.getElementById("createAccountBtn").addEventListener("click", goToCreateAcc);


function goToProfilePage(test){
    window.location.href=("profilePage");
}

function goToCreateAcc(){
    window.location.href=("createAccount");  
}