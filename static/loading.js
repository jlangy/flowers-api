function createSpinner(){
  const accessibilitySpan = document.createElement("SPAN");
  accessibilitySpan.classList.add("sr-only");
  const spinner = document.createElement("DIV");
  spinner.classList.add("spinner-border");
  spinner.setAttribute("role", "status");
  spinner.appendChild(accessibilitySpan);
  return spinner;
}


window.onload = function(){
  const uploadFileBtn = document.getElementById("upload-file-button");
  uploadFileBtn.onclick = function(){
    uploadFileBtn.innerHTML = "";
    uploadFileBtn.appendChild(createSpinner());
    uploadFileBtn.setAttribute("disabled", true)
  }
}

window.addEventListener('unload', function(event) {
  document.getElementById('upload-file-button').innerHTML = "Predict!";
});

