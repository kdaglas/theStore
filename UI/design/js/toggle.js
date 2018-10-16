/* --- function to verify attendant or owner --- */
function Check(){
  var username = document.querySelector("#username").value;
  var password = document.querySelector("#password").value;
  if(username==='user' && password ==="user"){
    window.location.href ="homepage.html";
  }else if(username==='admin' && password ==="admin"){
    var username = document.querySelector("#username").value;
    var password = document.querySelector("#password").value;
    window.location.href ="admin.html";
  }else{
  }
}


/* --- function to hide and reveal the categories --- */
var acc = document.getElementsByClassName("cat-items");
var i;
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight){
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}


/* --- functions to add an iten to the cart--- */
function sugar() { 
  document.getElementById('sugar').style.display = "block";
}
function clothes() { 
document.getElementById('clothes').style.display = "block";
}
function books() { 
document.getElementById('books').style.display = "block";
}
function soda() { 
document.getElementById('soda').style.display = "block";
}
function vaseline() { 
document.getElementById('vaseline').style.display = "block";
}
function water() { 
document.getElementById('water').style.display = "block";
}
function salt() { 
document.getElementById('salt').style.display = "block";
}


/* --- function to chhnge the tab for the attendant --- */
function openAttendant(evt, attendantName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(attendantName).style.display = "block";
  evt.currentTarget.className += " active";
}

/* --- this gives keeps one of the divs with default to always show --- */
document.getElementById("defaultOpen").click();


/* --- function to chhnge the tab for the adding buttons --- */
function openAction(evt, actionName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(actionName).style.display = "block";
  evt.currentTarget.className += " active";
}

/* --- this gives keeps one of the divs with default to always show --- */
document.getElementById("defaultOpen").click();
