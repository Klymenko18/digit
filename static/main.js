// Функція для отримання списку продуктів
function fetchProducts() {
    fetch('/api/products/')
        .then(response => response.json())
        .then(data => {
            let productsList = document.getElementById('products-list');
            productsList.innerHTML = '';
            data.forEach(product => {
                productsList.innerHTML += `
                    <li>
                        ${product.name} - $${product.price}
                        <button onclick="deleteProduct(${product.id})">Delete</button>
                        <a href="/products/${product.id}/edit/">Edit</a>
                    </li>`;
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

// Функція для створення нового продукту
function createProduct() {
    let productName = document.getElementById('product-name').value;
    let productPrice = document.getElementById('product-price').value;

    fetch('/api/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: productName, price: productPrice }),
    })
        .then(response => {
            if (response.ok) {
                fetchProducts(); // Оновлюємо список після створення
            } else {
                console.error('Error creating product:', response.statusText);
            }
        });
}

// Функція для видалення продукту
function deleteProduct(productId) {
    fetch(`/api/products/${productId}/`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                fetchProducts(); // Оновлюємо список після видалення
            } else {
                console.error('Error deleting product:', response.statusText);
            }
        });
}
// Функція для отримання списку продуктів
function fetchProducts() {
    fetch('/api/products/')
        .then(response => response.json())
        .then(data => {
            let productsList = document.getElementById('products-list');
            productsList.innerHTML = '';
            data.forEach(product => {
                productsList.innerHTML += `
                    <li>
                        ${product.name} - $${product.price}
                        <button onclick="deleteProduct(${product.id})">Delete</button>
                        <a href="/products/${product.id}/edit/">Edit</a>
                    </li>`;
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

// Функція для створення нового продукту
function createProduct() {
    let productName = document.getElementById('product-name').value;
    let productPrice = document.getElementById('product-price').value;

    fetch('/api/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: productName, price: productPrice }),
    })
        .then(response => {
            if (response.ok) {
                fetchProducts(); // Оновлюємо список після створення
            } else {
                console.error('Error creating product:', response.statusText);
            }
        });
}

// Функція для видалення продукту
function deleteProduct(productId) {
    fetch(`/api/products/${productId}/`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                fetchProducts(); // Оновлюємо список після видалення
            } else {
                console.error('Error deleting product:', response.statusText);
            }
        });
}
// Функція для отримання списку продуктів
function fetchProducts() {
    fetch('/api/products/')
        .then(response => response.json())
        .then(data => {
            let productsList = document.getElementById('products-list');
            productsList.innerHTML = '';
            data.forEach(product => {
                productsList.innerHTML += `
                    <li>
                        ${product.name} - $${product.price}
                        <button onclick="deleteProduct(${product.id})">Delete</button>
                        <a href="/products/${product.id}/edit/">Edit</a>
                    </li>`;
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

// Функція для створення нового продукту
function createProduct() {
    let productName = document.getElementById('product-name').value;
    let productPrice = document.getElementById('product-price').value;

    fetch('/api/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: productName, price: productPrice }),
    })
        .then(response => {
            if (response.ok) {
                fetchProducts(); // Оновлюємо список після створення
            } else {
                console.error('Error creating product:', response.statusText);
            }
        });
}

// Функція для видалення продукту
function deleteProduct(productId) {
    fetch(`/api/products/${productId}/`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                fetchProducts(); // Оновлюємо список після видалення
            } else {
                console.error('Error deleting product:', response.statusText);
            }
        });
}
// Функція для отримання списку продуктів
function fetchProducts() {
    fetch('/api/products/')
        .then(response => response.json())
        .then(data => {
            let productsList = document.getElementById('products-list');
            productsList.innerHTML = '';
            data.forEach(product => {
                productsList.innerHTML += `
                    <li>
                        ${product.name} - $${product.price}
                        <button onclick="deleteProduct(${product.id})">Delete</button>
                        <a href="/products/${product.id}/edit/">Edit</a>
                    </li>`;
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

// Функція для створення нового продукту
function createProduct() {
    let productName = document.getElementById('product-name').value;
    let productPrice = document.getElementById('product-price').value;

    fetch('/api/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: productName, price: productPrice }),
    })
        .then(response => {
            if (response.ok) {
                fetchProducts(); // Оновлюємо список після створення
            } else {
                console.error('Error creating product:', response.statusText);
            }
        });
}

// Функція для видалення продукту
function deleteProduct(productId) {
    fetch(`/api/products/${productId}/`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                fetchProducts(); // Оновлюємо список після видалення
            } else {
                console.error('Error deleting product:', response.statusText);
            }
        });
}
// Функція для отримання списку продуктів
function fetchProducts() {
      fetch('/api/products/')
          .then(response => response.json())
          .then(data => {
              let productsList = document.getElementById('products-list');
              productsList.innerHTML = '';
              data.forEach(product => {
                  productsList.innerHTML += `
                      <li>
                          ${product.name} - $${product.price}
                          <button onclick="deleteProduct(${product.id})">Delete</button>
                          <a href="/products/${product.id}/edit/">Edit</a>
                      </li>`;
              });
          })
          .catch(error => console.error('Error fetching products:', error));
  }
  
  // Функція для створення нового продукту
  function createProduct() {
      let productName = document.getElementById('product-name').value;
      let productPrice = document.getElementById('product-price').value;
  
      fetch('/api/products/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ name: productName, price: productPrice }),
      })
          .then(response => {
              if (response.ok) {
                  fetchProducts(); // Оновлюємо список після створення
              } else {
                  console.error('Error creating product:', response.statusText);
              }
          });
  }
  
  // Функція для видалення продукту
  function deleteProduct(productId) {
      fetch(`/api/products/${productId}/`, {
          method: 'DELETE',
      })
          .then(response => {
              if (response.ok) {
                  fetchProducts(); // Оновлюємо список після видалення
              } else {
                  console.error('Error deleting product:', response.statusText);
              }
          });
  }
  