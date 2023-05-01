/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: loginPage.js
 * DATE: April 8, 2023
 */



var uploadBtn = document.getElementById("uploadProfPic");
var refresh = false;

uploadBtn.onclick = function() {
    refresh = true;
};

document.onvisibilitychange = () => {

    if (document.visibilityState === "visible" && refresh) {
        refresh = false;
        location.reload();        
    }

};