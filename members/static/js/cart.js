let cartItems = []


function updateCartCount() {
    let cartItemCount = cartItems.length;
    const cartCountEl = document.querySelector('.cart');
    cartCountEl.innerHTML = cartItemCount;
}
function addToCart(el, name, id, price) {
    cartItems.push({ name, id, price })
    updateCartCount()
    el.disabled = true
    el.style.backgroundColor = 'lightblue'
    el.style.textDecoration = 'line-through'
}

function closeCart() {
    const modal = document.getElementById('cart_modal');
    modal.style.display = "none"
}

function updateCartTotalPrice() {
    const cartTotalEl = document.querySelector('#cart_total');
    let total = 0
    for (const item of cartItems) {
        total += parseFloat(item.price)
    }
    cartTotalEl.innerHTML = '$' +total;
}

function openCart() {
    const modal = document.getElementById('cart_modal');
    modal.style.display = "block"
    const modalContentEl = document.querySelector('#modal_content')
    let contentHtml = ''
    for (const item of cartItems) {
        contentHtml += `
        <div class="cart_item">
                <p>${item.name}</p>
                <p>$${item.price} <span onclick="deleteCartItem(${item.id})"><i class="fa-solid fa-trash-can"></i></p>
            </div>`
    }
    modalContentEl.innerHTML = contentHtml;
    updateCartTotalPrice()
}

function deleteCartItem(id) {
    cartItems = cartItems.filter(i => i.id != id);
    updateCartCount()
    openCart()
}