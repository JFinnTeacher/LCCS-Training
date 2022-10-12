//https://www.w3docs.com/snippets/javascript/how-to-make-http-get-request-in-javascript.html

//write data function
function httpWrite(writeTS){
  let xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.open("GET",writeTS,false);
  xmlHttpReq.send(null);
  return xmlHttpReq.responseText;
}

//get data function - pulling data down from Thingspeak
function httpGet(readTS){
  let xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.open("GET", readTS, false);
  xmlHttpReq.send(null);
  return xmlHttpReq.responseText;
}

//setting up some sample data to write to thingspeak
let fnames = prompt("First name?");
let lnames = prompt("Last name?");
let age = prompt("Age?");

//user needs to change the api_key 
let myDataToSend = 'https://api.thingspeak.com/update?api_key=PX7FRI5CBNVSL6IC&field1='+fnames+'&field2='+lnames+'&field3='+age;
//writing data to thingspeak (generating random names and ages)
httpWrite(myDataToSend);  

/*
//the below code gets the number of entries in the channel
status = httpGet('https://api.thingspeak.com/channels/1858859/status.json?api_key=MJU2KDAIZQJZTDBJ');
//console.log(status);
const obj = JSON.parse(status);
//console.log(obj);
//console.log(obj['feeds'].length);
entries = obj['feeds'].length;
*/
entries = 2;
getfeed = httpGet('https://api.thingspeak.com/channels/1858859/feeds.json?api_key=MJU2KDAIZQJZTDBJ&results='+entries.toString());
feed = JSON.parse(getfeed);
console.log(feed);
document.getElementById("demo").innerHTML = feed['feeds'][1]['field1']+" "+feed['feeds'][1]['field2']+" is "+feed['feeds'][1]['field3']+" years old.";



//console.log(feed['feeds']);
/*
//Runs through entries and sends data to the console
for(i=0;i<entries;i++)
{
  console.log(feed['feeds'][i]['field1'],feed['feeds'][i]['field2'],"is",feed['feeds'][i]['field3'],"years old.");
};
*/

/*
randomname = Math.floor(Math.random()*entries);
document.getElementById("demo").innerHTML = feed['feeds'][randomname]['field1']+" "+feed['feeds'][randomname]['field2']+" is "+feed['feeds'][randomname]['field3']+" years old.";
*/


// Code below shows how to use data from thingspeak to dynamically change webpage:
/*
document.getElementById("mycolour").style.backgroundColor = "rgb("+feed['feeds'][1]['field3'].toString()+",0,"+feed['feeds'][1]['field3'].toString()+")";
*/
