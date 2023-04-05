/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: createAccount.js
 * DATE: April 4, 2023
 */

const cnclCreate = document.getElementById("cancelCreateBtn").addEventListener("click", goHome);
const createAcc = document.getElementById("createForm").addEventListener("submit", getAccInfo);

function getAccInfo(event){
    event.preventDefault();

    const data = new FormData(event.target);
    
    const value = Object.fromEntries(data.entries());
    
    console.log({ value });
    console.log("getAcc");
}

function goHome(){
    window.location.href="login.html";
    console.log("OUT");
}