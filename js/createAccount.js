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

    let data = new FormData(event.target);
    
    let value = Object.fromEntries(data.entries());

    console.log(value);
    
    window.location.href="profilePage.html"; 

    // POST TO SERVER VIA FETCH
    // const response = await fetch('https://gymbuddy.com', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json; charset=utf-8'
    //     },
    //     body: JSON.stringify(value),
    // })

    // for multi-selects
    // value.name = data.getAll('name');

    // Check to see if passwords match.
    // var pwd1 = value["password1"];
    // var pwd2 = value["password2"];
    // var comp = pwd1.localeCompare(pwd2).toString();
    // if(comp == 0){
    //     console.log("Passwords Match");
    // } else {
    //     console.log("Passwords DO NOT Match");
    // }

}

function goHome(){
    window.location.href="login.html";
    console.log("OUT");
}