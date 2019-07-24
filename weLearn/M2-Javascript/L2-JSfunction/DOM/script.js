const myButton = document.querySelector("#myButton");
const myBox = document.querySelector("#box");
myButton.addEventListener('click', (event) => {
  console.log("Like button clicked!");
  myButton.innerHTML ="Liked! ";
  myButton.style.backgroundColor = "lightgreen";
});
