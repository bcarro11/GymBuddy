/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: loginPage.js
 * DATE: April 15, 2023
 */

// const submit = document.getElementById("loginForm").addEventListener("submit", submitFunction);

const createAcc = document.getElementById("loginBtn").addEventListener("click", goToLogin);

function goToLogin(){
    window.location.href=("login");  
}