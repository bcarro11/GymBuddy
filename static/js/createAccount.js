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
    

    fetch('/createAccount', {
        headers : {
            'Content-Type' : 'application/json'
        },
        method : 'POST',
        body : JSON.stringify(value)
    })
    .then(function (response){

        if(response.ok) {
            response.json()
            .then(function(response) {
                console.log(response);
            });
        }
        else {
            throw Error('Something went wrong');
        }
    })
    .catch(function(error) {
        console.log(error);
    });
    
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
    window.location.href="/login";
    console.log("OUT");
}