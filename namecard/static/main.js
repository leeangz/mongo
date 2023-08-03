function createCard() {
  const name = document.querySelector(".name").value;
  const title = document.querySelector(".title").value;
  const phone = document.querySelector(".phone").value;
  const email = document.querySelector(".email").value;

  const nameElement = document.querySelector(".card .name");
  const titleElement = document.querySelector(".card .title .value");
  const phoneElement = document.querySelector(".card .phone .value");
  const emailElement = document.querySelector(".card .email .value");

  nameElement.innerText = name;
  titleElement.innerText = title;
  phoneElement.innerText = phone;
  emailElement.innerText = email;

  document.querySelector(".card").style.display = "flex";
}
