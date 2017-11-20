
var a = document.getElementById("frog_on_wheels");
var left = a.getBoundingClientRect().left;
var i = parseInt(left);
var d = 1;
var timerId = setInterval(function() {
  a.style.left = i.toString()+'px';
  i+=d;
  if (i>880)
  {
    d = -1;
    a.style.transform = "scaleX(-1)";
  }

  if (i<450){
    a.style.transform = "";
    d = 1;
  }

}, 10);
// for (var i = parseInt(left); i<=500; i++){
//   delay(function(){
//     a.style.left = i.toString()+'px';
//   }, 10);
// }
