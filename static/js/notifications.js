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
    }
    setTimeout(fetchNotifications, 30000);
}

fetchNotifications();