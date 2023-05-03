async function fetchNotifications(){
    let res = await fetch('/getnotifications');
    let json = await res.json();
    if(json){
        let type = json['type']
        let message = json['message']
        document.getElementById('alert-type').textContent = type;
        document.getElementById('alert-message').textContent = message;
        document.getElementById('alert-container').style.display = 'flex'
        //window.alert(json)
    }
    setTimeout(fetchNotifications, 30000);
}

fetchNotifications();