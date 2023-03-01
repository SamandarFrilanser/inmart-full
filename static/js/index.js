window.addEventListener('DOMContentLoaded', (e) => {
    let right_btn = document.querySelector('#next_btn'),
        left_btn = document.querySelector('#prev_btn'),
        parent_content = document.querySelector('.section-2 .section-banner');
//   News carousel
    right_btn.addEventListener('click', () => {
        parent_content.scrollLeft += 285 * 4;
    });

    left_btn.addEventListener('click', () => {
        parent_content.scrollLeft -= 285 * 4;
    })

    let new_prev = document.querySelector('#new_prev'),
        new_next = document.querySelector('#new_next'),
        parent_conten = document.querySelector('.section-3 .section-banner');
    if (new_prev !== null) {
        new_prev.addEventListener('click', () => {
            parent_conten.scrollLeft -= 570;
        })

        new_next.addEventListener('click', () => {
            parent_conten.scrollLeft += 570;
        })
    }
    for (let obj of document.getElementsByClassName('filter_btn')) {
        obj.addEventListener('click', function (e) {
            e.preventDefault();
            if (this.dataset.filterType === "_all") {
                for (let box of document.getElementsByClassName("box_1")) {
                    box.style.display = 'block';
                }
                return;
            }
            for (let box of document.getElementsByClassName('box_1')) {
                if (box.dataset.itemType === obj.dataset.filterType) {
                    box.style.display = 'block';
                } else {
                    box.style.display = 'none';
                }
            }
        })
    }
})