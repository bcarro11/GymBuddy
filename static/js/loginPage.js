/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: loginPage.js
 * DATE: April 4, 2023
 */

const submit = document.getElementById("loginForm").addEventListener("submit", submitFunction);

const createAcc = document.getElementById("createAccountBtn").addEventListener("click", goToCreateAcc);


function submitFunction(event){
    event.preventDefault();

    let data = new FormData(event.target);
    
    let value = Object.fromEntries(data.entries());

    console.log(value);    

    fetch('/login', {
        headers : {
            'Content-Type' : 'application/json'
        },
        method : 'POST',
        body : JSON.stringify(value)
    })
    .then(function (response){

        if(response.ok) {
            console.log("response ok");
            let x = response.json()                    
            .then(function(x) {
                console.log(x)
                // let x = response.json
                if(x['response'] == "YES") {
                    console.log("SUCCESS");
                    goToProfilePage();
                } else {
                    console.log(x['response']);
                    // alert(x['response']);
                }
            });
        }
        else {
            // throw Error('Something went wrong');
            alert("NO");
        }
    })
    .catch(function(error) {
        console.log(error);
    });

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

function goToProfilePage(test){
    window.location.href="profilePage";
}

function goToCreateAcc(){
    window.location.href=("createAccount");  
}