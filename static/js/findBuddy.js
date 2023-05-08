/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: findBuddy.js
 * DATE: April 8, 2023
 */


/**
 * Handles cancel search on find buddy page 
 * Routes back to profile page.
 */
const createAcc = document.getElementById("cancelSearch").addEventListener("click", goCancelSearch);

function goCancelSearch(){
    window.location.href="profilePage";  
}