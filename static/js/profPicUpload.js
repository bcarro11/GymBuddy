/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: profPicUpload.js
 * DATE: April 22, 2023
 */


/**
 * Handles profile picture upload feature.
 */
var uploadField = document.getElementById("file");
var closeTab = document.getElementById("close");
var fSize = document.getElementById("fileSize");

uploadField.onchange = function() {
    //Calculates size of selected image and displays it to user.
    let size = this.files[0].size;
    if (size >= 1000000){
        fSize.innerHTML = (size / 1000000) + "MB";
    } else {
        fSize.innerHTML = (size / 1000) + "KB";
    }
    //Limit picture to 1MB
    if(this.files[0].size > 1000000){
       alert("File is too big!\nFile must be less than 1MB");
       this.value = "";
    };
};

//Close tab feature.
closeTab.onclick = function() {
    close();
};