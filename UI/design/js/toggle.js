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
