/* Authors: Giuseppe Scoppino, Nathanael Thompson 2013-2014 */

function Clock()
{
    /* Clock To Do List
    *  ----------------------
    * Get current time, then add to it
    * Display time and date at bottom of screen
    */
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    
    minutes = ( minutes < 10 ? "0" : "" ) + minutes;
    seconds = ( seconds < 10 ? "0" : "" ) + seconds;
    
    var timeOfDay = ( hours < 12 ) ? "AM" : "PM";
    hours = ( hours > 12 ) ? hours - 12 : hours;
    hours = ( hours == 0 ) ? 12 : hours;
    
    var currentTimeString = hours + ":" + minutes + ":" + seconds + " " + timeOfDay;
    document.getElementById("clock").firstChild.nodeValue = currentTimeString;
    
};

window.onload = function() {
    Clock();
    setInterval('Clock()', 1000);
};

document.getElementById("submit_library").onclick= function() {
    window.location['href'] = document.getElementById('library_selector').value;
};
