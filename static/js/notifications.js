/**
 * GROUP: Gym Buddy
 * MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
 * COURSE: CMSC 495:7383
 * FILE: notifactions.js
 * DATE: May 4, 2023
 */

/**
 * Asynchronous request for message/match notifications.
 */

async function fetchNotifications(){
    let res = await fetch('/getnotifications');
    let json = await res.json();
    if(json){
        let type = json['type']
        let message = json['message']
        let userid = json['triggerUser']
        document.getElementById('alert-type').textContent = type;
        document.getElementById('alert-message').textContent = message;
        document.getElementById('alert-container').style.display = 'flex'
        document.getElementById('alert-type').onclick = (() => {
            window.location.href = '/message/' + String(userid);
        });
        document.getElementById('alert-message').onclick = (() => {
            window.location.href = '/message/' + String(userid);
        });
        //window.alert(json)
        $('#ajaxUpdate').load(document.URL +  ' #ajaxUpdate');
    }
    setTimeout(fetchNotifications, 30000);
}

fetchNotifications();