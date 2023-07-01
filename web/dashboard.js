let data = JSON.parse(localStorage.getItem("user")) || [];
let owner = document.getElementById("owner-info");
let dataArr = [];
dataArr.push(data);
console.log(dataArr);
function showInfo() {
  if (owner.style.display === "block") {
    owner.style.display = "none";
  } else {
    owner.style.display = "block";
  }

  owner.innerHTML = "";

  dataArr.forEach(function (el) {
    let name = document.createElement("h3");
    name.innerText = "Name: " + el.name;
    let email = document.createElement("h3");
    email.innerText = "Email: " + el.email;
    owner.append(name, email);
  });
}

function logout() {
  localStorage.removeItem("user");
  window.location.href = "index.html";
}

let mlContent = document.getElementById("content-cont");
let right_cont=document.getElementById('right-cont');

function showReg() {
  event.preventDefault();
  right_cont.innerHTML=null;
  mlContent.innerHTML ="";
  let iframe = document.createElement('iframe');
  iframe.src = "https://app.powerbi.com/reportEmbed?reportId=232dae11-b836-4e46-ad6a-f92c070b2f3e&autoAuth=true&ctid=a4089f7d-e186-426a-8e42-6f27d34a2b5a";
  iframe.style.width = "100%";
  iframe.style.height = "100%";
  right_cont.appendChild(iframe);
}

function showClass() {
  event.preventDefault();
  right_cont.innerHTML=null;
  mlContent.innerHTML = ``;
  let iframe = document.createElement('iframe');
  iframe.src = "http://localhost:8501/";
  iframe.style.width = "100%";
  iframe.style.border='none'
  iframe.style.margin='0px';
  iframe.style.height = "100%";
  iframe.style.overflowY='hidden'
  // iframe.style.background='transparent'
  right_cont.appendChild(iframe);
}
