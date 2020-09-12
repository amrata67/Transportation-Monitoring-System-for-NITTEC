function renderTime(){
    var dayarray = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
    var montharray = new Array("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
    var today = new Date();
    var temp = 'AM';
    if(today.getHours()>12){
    hour = today.getHours() - 12;
        temp = 'PM';
    }
    else{
    hour = today.getHours();
       temp = 'AM';
    }
    var myClock = document.getElementById("clockDisplay");
    myClock.textContent = " " +dayarray[today.getDay()]+ ", "+montharray[today.getMonth()]+ " " +today.getDate()+ ", "+today.getFullYear()+"  "+hour+":"+today.getMinutes()+":"+today.getSeconds()+" "+temp;
    myClock.innerText = " " +dayarry[mydate.getDay()]+ ", "+montharray[today.getMonth()]+ " " +today.getDate()+", "+today.getFullYear()+"  "+hour+":"+today.getMinutes()+":"+today.getSeconds()+" "+temp ;
    setTimeout("renderTime()", 1000);
}
renderTime();