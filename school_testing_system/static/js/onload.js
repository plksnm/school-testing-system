
var a = document.getElementById("frog_on_wheels");
var left = a.getBoundingClientRect().left;
var i = parseInt(left);
var d = 1;
var timerId = setInterval(function() {
  var width = document.body.clientWidth;
  var left2 = width*0.25 //левая часть экрана, от которой едет лягуха
  var right2 = width * 0.75 //правая часть
  a.style.left = i.toString()+'px';
  i+=d;
  if (i>right2)
  {
    d = -1;
    a.style.transform = "scaleX(-1)";
  }

  if (i<left2){
    a.style.transform = "";
    d = 1;
  }

}, 10);
