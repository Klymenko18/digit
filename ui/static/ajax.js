document.addEventListener('DOMContentLoaded', function () {
    const productList = document.getElementById('product-list');
    const addProductBtn = document.getElementById('add-product-btn');

    // Завантаження продуктів
    function loadProducts() {
        fetch('/api/products/')
            .then(response => response.json())
            .then(data => {
                productList.innerHTML = '';
                data.forEach(product => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        ${product.name} - $${product.price}
                        <button onclick="editProduct(${product.id})">Edit</button>
                        <button onclick="deleteProduct(${product.id})">Delete</button>
                    `;
                    productList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }

    // Додавання нового продукту
    addProductBtn.addEventListener('click', function () {
        const productName = prompt('Enter product name:');
        const productPrice = prompt('Enter product price:');
        fetch('/api/products/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: productName,
                price: productPrice,
            }),
        })
            .then(response => {
                if (response.ok) {
                    loadProducts();
                } else {
                    alert('Failed to add product');
                }
            })
            .catch(error => console.error('Error:', error));
    });

    // Редагування продукту
    window.editProduct = function (id) {
        const productName = prompt('Enter new product name:');
        const productPrice = prompt('Enter new product price:');
        fetch(`/api/products/${id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: productName,
                price: productPrice,
            }),
        })
            .then(response => {
                if (response.ok) {
                    loadProducts();
                } else {
                    alert('Failed to edit product');
                }
            })
            .catch(error => console.error('Error:', error));
    };

    // Видалення продукту
    window.deleteProduct = function (id) {
        fetch(`/api/products/${id}/`, {
            method: 'DELETE',
        })
            .then(response => {
                if (response.ok) {
                    loadProducts();
                } else {
                    alert('Failed to delete product');
                }
            })
            .catch(error => console.error('Error:', error));
    };

    // Завантажити продукти після завантаження сторінки
    loadProducts();
});
