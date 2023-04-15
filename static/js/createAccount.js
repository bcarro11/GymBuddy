/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: createAccount.js
 * DATE: April 4, 2023
 */

const cnclCreate = document.getElementById("cancelCreateBtn").addEventListener("click", goHome);

function goHome(){
    window.location.href="login";
    console.log("OUT");
}