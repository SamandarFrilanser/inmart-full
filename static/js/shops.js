let locat_name = document.querySelectorAll('.box a'),
    locat = document.querySelectorAll('.frame iframe'),
    filial_name = document.querySelector('.info h3'),
    addres = document.querySelector('.location p'),
    cal_center = document.querySelector('.call-center p');

let lang_box = document.querySelector('.change-lang'),
    Ru_lang = document.querySelector('.btn-1'),
    Uz_lang = document.querySelector('.btn-2');

lang_box.addEventListener('click', function () {
    Ru_lang.classList.toggle('active');
})


locat[0].style.display = 'block';

locat_name[0].addEventListener('click', () => {
    locat[0].src = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2584.7124486214566!2d67.3045645153025!3d37.24546157985931!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f3533f435ece3bd%3A0xb5aaa0f5f8c55b1a!2sSafran%20restaurant%202!5e1!3m2!1sru!2s!4v1635649579803!5m2!1sru!2s";

    locat[0].style.display = 'block';
    locat[1].style.display = 'none';
    locat[2].style.display = 'none';
    locat[3].style.display = 'none';
})
locat_name[1].addEventListener('click', () => {
    locat[1].src = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3175.9019995032363!2d67.30666001530264!3d37.250032579858356!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f3533917b5bdc87%3A0xef9a4d793e18e935!2sIndenim%20savdo%20markazi%20-Termez!5e0!3m2!1sru!2s!4v1635761327230!5m2!1sru!2s";

    locat[0].style.display = 'none';
    locat[1].style.display = 'block';
    locat[2].style.display = 'none';
    locat[3].style.display = 'none';

    filial_name.textContent = 'Termiz';
    addres.textContent = 'Surxondaryo viloyati,Termiz shahri';
    cal_center.textContent = '+998 91 888 00 01';
})
locat_name[2].addEventListener('click', () => {
    locat[2].src = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3132.167284614142!2d67.89223421533215!3d38.2756148796714!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38b511e746f9cb2d%3A0x515c0e4d12925acf!2sA%20Print!5e0!3m2!1sru!2s!4v1635739507871!5m2!1sru!2s";

    locat[0].style.display = 'none';
    locat[1].style.display = 'none';
    locat[2].style.display = 'block';
    locat[3].style.display = 'none';

    filial_name.textContent = 'Denov filiali';
    addres.textContent = 'Surxondaryo viloyati,Denov tumani';
    cal_center.textContent = '+998 91 848 20 91';
})
locat_name[3].addEventListener('click', () => {
    locat[3].src = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d41208.91953463917!2d67.38196061758352!3d37.51157326559982!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38cab37ca4722a01%3A0xe0a2149c223738fc!2z0JTQttCw0YDQutGD0YDQs9Cw0L0sINCj0LfQsdC10LrQuNGB0YLQsNC9!5e1!3m2!1sru!2s!4v1635765301546!5m2!1sru!2s";

    locat[0].style.display = 'none';
    locat[1].style.display = 'none';
    locat[2].style.display = 'none';
    locat[3].style.display = 'block';

    filial_name.textContent = 'Jarqurgon filiali';
    addres.textContent = 'Surxondaryo viloyati,Jarqurgon tumani';
    cal_center.textContent = '+998 91 785 23 81';

})

    

