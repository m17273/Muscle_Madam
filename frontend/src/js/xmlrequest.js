"use strict"

let editorName = document.querySelector(".editor-name");
let editorInstagram = document.querySelector(".editor-instagram");
let editorIntroduction = document.querySelector(".editor-introduction");
let editorList = document.querySelector(".editor-list");
let editorCommentArea = document.querySelector('.editor-comment-area');
let target;

editorList.addEventListener("click", (e) => {
  target = e.target
  if (target.className === 'editor-icon'){
      xmlRequest();
  }
  
});

function xmlRequest() {
  let request = new XMLHttpRequest();
  request.open("GET", "src/js/test.json", true);
  request.responseType = "json";
  request.send();
  request.onload = function () {
    editorFind(request.response);
  };
}

function editorFind(jsonObj) {
  let editors = jsonObj["editor"];
  for (let i in editors) {
    if (editors[i]["name"] === target.dataset.name) {
      editorNameChange(editors[i]["nickname"]);
      editorInstagramChange(editors[i]["instagram"]);
      editorIntroductionChange(editors[i]["introduction"]);
      editorCommentChange(editors[i]["comments"])
      console.log(editors[i]["comments"])
    }
  }
}

function editorNameChange(nickname) {
  editorName.innerText = nickname;
}

function editorInstagramChange(instagram) {
  editorInstagram.innerText = instagram;
}

function editorIntroductionChange(introduction) {
  editorIntroduction.innerText = introduction;
}
function editorCommentChange(comments) {
    editorCommentArea.innerText = '';
    for (let i in comments) {
        let commentbox = document.createElement('div');
        let title = comments[i]["name"];
        let date = comments[i]["date"];
        let comment = comments[i]["comment"];
        commentbox.setAttribute('class', "editor-comment-box")
        commentbox.innerHTML = `
            <div class="comment-img"></div>
            <div class="editor-comment">
                <p class="comment-title">${title}</p>
                <p class="comment-date">${date}</p>
                <p class="comment">${comment}</p>
            </div>
        `
        editorCommentArea.append(commentbox)
    }
}