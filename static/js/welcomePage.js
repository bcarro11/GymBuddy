/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: welcomePage.js
 * DATE: April 15, 2023
 */


/**
 * Button handler for welcome page.
 * Routes back to login on click.
 */
const createAcc = document.getElementById("loginBtn").addEventListener("click", goToLogin);

function goToLogin(){
    window.location.href=("login");  
}