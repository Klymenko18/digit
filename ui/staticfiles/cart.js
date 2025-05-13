document.addEventListener("DOMContentLoaded", () => {
    const cartItemsContainer = document.getElementById("cart-items");
    const totalPriceElement = document.getElementById("total-price");

    function loadCartItems() {
        fetch('/api/cart/')
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to fetch cart items");
                }
                return response.json();
            })
            .then(data => {
                console.log("Cart data:", data);
                cartItemsContainer.innerHTML = '';
                let totalPrice = 0;

                data.cart_items.forEach(item => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${item.product.name}</td>
                        <td>$${item.product.price}</td>
                        <td>
                            <input type="number" min="1" value="${item.quantity}" data-id="${item.id}" class="quantity-input">
                        </td>
                        <td>$${(item.product.price * item.quantity).toFixed(2)}</td>
                        <td>
                            <button class="remove-btn" data-id="${item.id}">Remove</button>
                        </td>
                    `;
                    cartItemsContainer.appendChild(row);
                    totalPrice += item.product.price * item.quantity;
                });

                totalPriceElement.textContent = `$${totalPrice.toFixed(2)}`;
            })
            .catch(error => console.error("Error loading cart items:", error));
    }

    document.body.addEventListener("click", (event) => {
        if (event.target.classList.contains("add-to-cart-btn")) {
            const productId = event.target.dataset.id;

            fetch('/api/cart/add/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ product_id: productId, quantity: 1 }),
            })
                .then(response => {
                    if (response.ok) {
                        alert("Product added to cart!");
                        loadCartItems();
                    } else {
                        return response.json().then(data => {
                            alert(data.error || "Failed to add product.");
                        });
                    }
                })
                .catch(error => console.error("Error adding product to cart:", error));
        }
    });

    document.body.addEventListener("change", (event) => {
        if (event.target.classList.contains("quantity-input")) {
            const itemId = event.target.dataset.id;
            const newQuantity = event.target.value;

            fetch('/api/cart/update/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ product_id: itemId, quantity: newQuantity }),
            })
                .then(response => {
                    if (response.ok) {
                        loadCartItems();
                    } else {
                        return response.json().then(data => {
                            alert(data.error || "Failed to update quantity.");
                        });
                    }
                })
                .catch(error => console.error("Error updating item quantity:", error));
        }
    });

    document.body.addEventListener("click", (event) => {
        if (event.target.classList.contains("remove-btn")) {
            const itemId = event.target.dataset.id;

            fetch('/api/cart/remove/', {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ product_id: itemId }),
            })
                .then(response => {
                    if (response.ok) {
                        loadCartItems();
                    } else {
                        alert("Failed to remove item.");
                    }
                })
                .catch(error => console.error("Error removing item:", error));
        }
    });

    loadCartItems();
});