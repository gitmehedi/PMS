/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function () {
    var counter = 0;
    var images = [
        "bgf.jpg",
        "bga.jpg",
        "bgb.png",
        "bgc.jpg",
        "bgd.png",
        "bge.jpg",
        "bgg.jpg",
        "bgh.jpg",
        "bgi.jpg",
        "bgj.jpg"
    ];
    var rand = images[Math.floor(Math.random() * images.length)];

    var image = "url('" + baseUrl + "/bundles/media/images/bgimages/" + rand + "')";

    $("#bgimg").css('background-image', image);

    $(document).on('change', '#upload_image', previewImage);
    setInterval(startRotator, 3000);

    function startRotator() {

        if (counter >= images.length) {
            counter = 0;
        }
        var image = "url('" + baseUrl + "/bundles/media/images/bgimages/" + images[counter] + "')";

        $('#bgimg').animate(function () {
            $(this).css('background-image', image).animate({opacity: .6});
        });
        counter++;
    }
});


function previewImage() {

    var fullPath = $('#upload_image').val();
    var extention = fullPath.split(".");
    var ext = extention[extention.length - 1].toUpperCase();
    var defaultImg = "/images/default.png";

    var supportExt = ['JPG', 'JEPG'];
    if ($.inArray(ext, supportExt) > -1) {
        var oFReader = new FileReader();
        oFReader.readAsDataURL(document.getElementById("upload_image").files[0]);
        oFReader.onload = function (oFREvent) {
            var oImg = document.createElement("img");
            oImg.setAttribute('src', oFREvent.target.result);
            oImg.setAttribute('alt', 'Style Image');
            oImg.setAttribute('class', 'img-responsive');
            $("#preview").html(oImg);
        };
    } else {
        alert("Invalid Image. Only JPG image is allowed.");
        $('#upload_image').val('');
        $('.img-responsive').attr('src', defaultImg);
    }
}





