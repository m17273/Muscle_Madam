"use strict";

let clickedName;
let clickedBefore;
let editorLine = document.querySelector('.editor-line');
editorList.addEventListener("click", (e) => {
  clickedName = e.target;
  if (clickedBefore && clickedBefore !== clickedName) {
    iconRestore(clickedBefore);
  }
  iconChange(clickedName);
});

function iconChange(clickedName) {
  switch (clickedName.dataset.name) {
    case "윤영택":
      clickedName.src = "src/icons/youngtaekR.png";
      editorLine.src = "src/icons/editorYoung.png"
      clickedBefore = clickedName;
      break;
    case "문지현":
      clickedName.src = "src/icons/jihyunR.png";
      editorLine.src = "src/icons/editorJi.png"
      clickedBefore = clickedName;
      break;
    case "박상민":
      clickedName.src = "src/icons/sangminR.png";
      editorLine.src = "src/icons/editorSang.png"
      clickedBefore = clickedName;
      break;
    case "고유진":
      clickedName.src = "src/icons/youjinR.png";
      editorLine.src = "src/icons/editorYou.png"
      clickedBefore = clickedName;
      break;
    case "이주은":
      clickedName.src = "src/icons/jooeunR.png";
      editorLine.src = "src/icons/editorJoo.png"
      clickedBefore = clickedName;
      break;
  }
}

function iconRestore(clickedBefore) {

  switch (clickedBefore.dataset.name) {
    case "윤영택":
      clickedBefore.src = "src/icons/youngtaek.png";
      break;
    case "문지현":
      clickedBefore.src = "src/icons/jihyun.png";
      break;
    case "박상민":
      clickedBefore.src = "src/icons/sangmin.png";
      break;
    case "고유진":
      clickedBefore.src = "src/icons/youjin.png";
      break;
    case "이주은":
      clickedBefore.src = "src/icons/jooeun.png";
      break;
  }
}
