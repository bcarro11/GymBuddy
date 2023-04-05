/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: loginPage.js
 * DATE: April 4, 2023
 */

const submit = document.getElementById("loginForm").addEventListener("submit", submitFunction);
// submit.addEventListener("submit", submitFunction);

const createAcc = document.getElementById("createAccountBtn").addEventListener("click", goToCreateAcc);


function submitFunction(event){
    event.preventDefault();
    
    let data = new FormData(event.target); 
    
    let value = Object.fromEntries(data.entries());

    window.location.href="profilePage.html"; 

    // console.log(value);

    // POST TO SERVER VIA FETCH
    // const response = await fetch('https://gymbuddy.com', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json; charset=utf-8'
    //     },
    //     body: JSON.stringify(value),
    // })
    

    // var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    // var a = loginForm.psw.value;
    
    // var strongRegex = new RegExp("(?=.{8,})");
    // if(strongRegex.test(a)) {
    //     alert('Great Password!');
    // } else {
    //     alert('Bad Password!');
    // }



    // Update <p>loginError</p>
    // var msg = "No Error";
    // loginError.innerHTML = msg;

}

function goToCreateAcc(){
    window.location.href="createAccount.html";  
}