const formName = document.querySelector(".form .name");
const formTitle = document.querySelector(".form .title");

const card = document.querySelector(".card");
const cardName = document.querySelector(".card .name");
const cardTitle = document.querySelector(".card .title .value");

createCardBtn.addEventListener("click", function () {
  card.classList.add("show");
  cardName.innerHTML = formName.value;
});
