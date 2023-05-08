/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: profilePage.js
 * DATE: April 8, 2023
 */


/**
 * Handles reloading profile page on view 
 * (so that profile pic dispalys after being upload without manual refresh)
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

/**
 * 
 * Handles confirmation prompt for when user clicks delete account
 * (Helps prevent accidental deletion.)} form 
 */
function confSubmit(form) {
    if (confirm("Are you sure you want to delete your account?")) {        
        document.getElementById("deleteAccount").value = "True";
    }

    else {
       alert("Your account is still active.");
       document.getElementById("deleteAccount").value = "False";
       return 0;
    }
}