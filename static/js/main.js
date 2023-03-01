// Nav

const navOpenBtn = document.querySelector(
    " .header .subheader .right-side .nav-btn"
);

const navCloseBtn = document.querySelector(
    " .header .header-top .lang-close .nav-close"
);

const mobileNav = document.querySelector(" .header .header-top");

navOpenBtn.addEventListener("click", () => {
    mobileNav.classList.add("open-nav");
    navOpenBtn.classList.add("opacity");
});

navCloseBtn.addEventListener("click", () => {
    mobileNav.classList.remove("open-nav");
    navOpenBtn.classList.remove("opacity");
});

function modal_func(pk) {
    const plusBtn = document.getElementById('add-' + pk);
    const minusBtn = document.getElementById('remove-' + pk);
    const buy_btn = document.getElementById('buy-btn-' + pk);
    const counter = document.getElementById('product-number-' + pk);
    let s = parseInt(counter.innerText, 10);
    plusBtn.addEventListener("click", () => {
        s++;
        counter.innerHTML = s;
        if (cart[pk] === undefined) {
            cart[pk] = {'quantity': 1};
        } else {
            cart[pk]['quantity'] += 1;
        }
    });
    minusBtn.addEventListener("click", () => {
        s--;
        if (s > 0) {
            cart[pk]['quantity'] -= 1;
        } else {
            s = 0;
            delete cart[pk];
        }
        counter.innerHTML = s;
    });
    const modal = document.querySelector('.modal-' + pk);
    modal.style.cssText = `
    display: flex;
    justify-content: center;
    align-items: center;
  `;
    document.body.style.overflow = "hidden";

    function closemodal() {
        modal.style.display = 'none';
        document.body.style.overflow = "";
    }

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            if (s !== 0 && user !== 'AnonymousUser') {
                updateUserOrder(pk, 0, s)
            } else {
                if (s !== 0 && user === 'AnonymousUser') {
                    addCookieItem();
                }
            }
            closemodal();
        }
    })
    buy_btn.addEventListener("click", () => {
        if (s !== 0 && user !== 'AnonymousUser') {
            updateUserOrder(pk, 0, s)
        } else {
            if (s !== 0 && user === 'AnonymousUser') {
                addCookieItem();
            } else {
                closemodal();
            }
        }
    });
}

function addCookieItem() {
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
    location.reload()
}

function updateUserOrder(productId, action, counter) {
    if (typeof (action) === 'undefined') action = 0;
    if (typeof (counter) === 'undefined') counter = 0;
    if (user !== 'AnonymousUser') {
        const url = '/update-item/';
        fetch(
            url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(
                    {
                        'productId': productId,
                        'action': action,
                        'counter': counter
                    }
                )
            }
        ).then(
            (response) => {
                return response.json();
            }
        ).then(
            (data) => {
                location.reload();
            }
        )
    } else {
        if (action === 'add') {
            cart[productId]['quantity'] += 1;
        }
        if (action === 'remove') {
            cart[productId]['quantity'] -= 1;
            if (cart[productId]['quantity'] <= 0) {
                delete cart[productId]
            }
        }
        document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
        location.reload();
    }
}

function orderRemove(id) {
    if (user !== 'AnonymousUser') {
        const url = '/remove-order-items/';
        fetch(
            url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(
                    {
                        'orderId': id,
                    }
                )
            }
        ).then(
            (response) => {
                return response.json();
            }
        ).then(
            (data) => {
                location.reload();
            }
        )
    } else {
        delete cart[id];
        document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
        location.reload();
    }

}

function take_away() {
    document.getElementById('form-checkout').innerHTML = ''
}

function curyer() {
    let html = "<div class=\"blok_input\">\n<span>Shahar</span> <br>\n<input type=\"text\" placeholder=\"Shahar\">\n</div>";
    html += "<div class=\"blok_input\">\n<span>Tuman</span> <br>\n<input type=\"text\" placeholder=\"Tuman\">\n</div>"
    html += "<div class=\"blok_input\">\n<span>Ko'cha nomi</span> <br>\n<input type=\"text\" placeholder=\"Ko'cha\">\n</div>"
    html += "<div class=\"block_input\">\n<div class=\"house_name\">\n" +
        "<span>Uy raqami</span> <br>\n<input type=\"number\" placeholder=\"6\">\n</div>\n" +
        "<div class=\"house_num\">\n<span>Xonadon raqami</span> <br>\n<input type=\"number\" placeholder=\"2\">\n</div>\n</div>"
    document.getElementById('form-checkout').innerHTML = html
}


function change_image(img_url, pk) {
    document.getElementById("edit-image-" + pk).src = img_url
}