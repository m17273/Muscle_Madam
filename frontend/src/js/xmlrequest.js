"use strict";

let editorName = document.querySelector(".editor-name");
let editorInstagram = document.querySelector(".editor-instagram");
let editorIntroduction = document.querySelector(".editor-introduction");
let editorList = document.querySelector(".editor-list");
let editorCommentArea = document.querySelector(".editor-comment-area");
let target;


editorList.addEventListener("click", (e) => {
  target = e.target;
  if (target.className === "editor-icon") {
    xmlRequest_editor(target.dataset.pk);
    // xmlRequest_comment(target.dataset.pk);
    // xmlRequest_menus_restaurant(target.dataset.pk)
  }
});

function xmlRequest_editor(pk) {
  let request = new XMLHttpRequest();
  request.open("GET", `http://127.0.0.1:8080/editors/?editor_pk=${pk}`, true);
  request.responseType = "json";
  request.send();
  request.onload = function () {
    editorFind(request.response);
  };
};

function editorFind(editorinfo) {
  for (let i=0; i<editorinfo.length; i++) {
    editorNameChange(editorinfo[i]["editor_name"]);
    editorIntroductionChange(editorinfo[i]["editor_intro"]);
    editorCommentSet(editorinfo[i]['comments'])
  };
};

function editorNameChange(nickname) {
  editorName.innerText = nickname;
};

function editorIntroductionChange(introduction) {
  editorIntroduction.innerText = introduction;
};

function editorCommentSet(editors) {

  editorCommentArea.innerText = "";
  for (let i = 0; i < editors.length; i++) {
    let commentbox = document.createElement("div");
    let comment = editors[i]["content"];
    commentbox.setAttribute("class", "editor-comment-box");
    commentbox.innerHTML = `
            <div class="comment-img"></div>
            <div class="editor-comment">
                <p class="comment-title">임시</p>
                <p class="comment">${comment}</p>
            </div>
        `;
    editorCommentArea.append(commentbox);
  };





}
