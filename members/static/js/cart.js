function addToCart(...params) {
    console.log(params);
}

function closeCart() {
    const modal = document.getElementById('cart_modal');
    modal.style.display = "none"
}

function openCart() {
    const modal = document.getElementById('cart_modal');
    modal.style.display = "block"
}