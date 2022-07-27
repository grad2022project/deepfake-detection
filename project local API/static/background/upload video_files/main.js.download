$("form").on("change", ".file-upload-field", function(){
    $(this).parent(".file-upload-wrapper").attr("data-text",$(this).val().replace(/.*(\/|\\)/,''));
})

const image_input = document.querySelector("#upload");

image_input.addEventListener("change", function() {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploaded_image = reader.result
    document.querySelector("#vv").style.backgroundImage = `url(${uploaded_image})`;
  });
  reader.readAsDataURL(this.files[0]);
});

// **************************************************************************************************
function vvupload(){
  var input = document.getElementById("upload");
  var freader = new FileReader();
  freader.readAsDataURL(input.files[0]);
  freader.onload = function(){
    document.getElementById("uploadvideo").src=freader.result;

  }
}


// /***********************************************************************************************



// window.URL = window.URL || window.webkitURL;
//         let videoElement = null;
//         window.addEventListener('load', function() {
//             videoElement = document.getElementById('upload');
//         })

//         function loadVideo(event) {
//             let file = event.target.files[0];
//             // Info
//             let info = document.getElementById('xx');
//             info.innerHTML = ""

//             // Remove old video element
//             videoElement.remove();

//             // Create new video element
//             videoElement = document.createElement('video')
//             videoElement.controls = true;


//             // Source Element
//             let source = document.createElement('source')
//             source.src = URL.createObjectURL(file)
//             source.type = file.type
//             // Add to HTML
//             videoElement.appendChild(source);
//             document.body.appendChild(videoElement)

//         }