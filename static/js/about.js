const about_us_img = document.querySelectorAll(".about_us .content img"),
    content_text = document.querySelector(".content-text-span"),
    contentText = document.querySelectorAll(".about_us .content .box-1 .text p");
window.addEventListener('resize', function () {
    if (window.innerWidth >= 768) {
        about_us_img[0].style.display = "inline-block";
        content_text.style.cssText = "display:none;";
    } else {
        about_us_img[0].style.display = "none";
        content_text.style.cssText = "display:block; margin-top: 10px;";
    }
    if (window.innerWidth >= 768 && window.innerWidth <= 991) {
        contentText[0].style.paddingLeft = "25px";
        contentText[1].style.paddingRight = "25px";
    } else {
        contentText[0].style.paddingLeft = "0";
        contentText[1].style.paddingRight = "0";
    }
})
if (window.innerWidth < 768) {
    about_us_img[0].style.display = "none";
    content_text.style.cssText = "display:block; margin-top: 10px;";
}
if (window.innerWidth >= 768 && window.innerWidth <= 991) {
    contentText[0].style.paddingLeft = "25px";
    contentText[1].style.paddingRight = "25px";
}
