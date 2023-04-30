async function fetchNotifications(){
    let res = await fetch('/getnotifications');
    let json = await res.json();
    if(json){
        window.alert(json)
    }
    setTimeout(fetchNotifications, 3000);
}

fetchNotifications();