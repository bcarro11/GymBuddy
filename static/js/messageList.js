/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: messageList.js
 * DATE: May 4, 2023
 */


//Refreshes inbox when it returns to visible (helps update read/unread message colors)
document.onvisibilitychange = () => {

    if (document.visibilityState === "visible") {
        location.reload();        
    }

};