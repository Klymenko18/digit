document.addEventListener("DOMContentLoaded", () => {
      const orderForm = document.getElementById("order-form");
  
      orderForm.addEventListener("submit", (event) => {
          event.preventDefault();
  
          const deliveryAddress = document.getElementById("delivery-address").value;
  
          fetch('/api/orders/', {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: JSON.stringify({
                  delivery_address: deliveryAddress,
                  products: [],  // Можна динамічно отримати з кошика
              }),
          })
              .then((response) => response.json())
              .then((data) => {
                  alert("Order placed successfully!");
                  window.location.href = "/orders/";
              })
              .catch((error) => console.error("Error placing order:", error));
      });
  });
  