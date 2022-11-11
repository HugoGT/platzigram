const iClose = document.getElementById("message-close");
const message = document.querySelector(".message")

iClose.addEventListener("click", closeMessages);

function closeMessages() {
  message.style.display = "none";
}