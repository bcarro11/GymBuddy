/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: loginPage.js
 * DATE: April 8, 2023
 */

var uploadField = document.getElementById("file");

uploadField.onchange = function() {
    if(this.files[0].size > 2200000){
       alert("File is too big!");
       this.value = "";
    };
};