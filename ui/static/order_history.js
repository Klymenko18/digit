document.addEventListener("DOMContentLoaded", () => {
      const orderList = document.getElementById("order-list");
  
      fetch('/api/orders/')
          .then((response) => response.json())
          .then((data) => {
              data.forEach((order) => {
                  const listItem = document.createElement("li");
                  listItem.innerHTML = `
                      <p><strong>Order ID:</strong> ${order.id}</p>
                      <p><strong>Total Price:</strong> $${order.total_price}</p>
                      <p><strong>Delivery Address:</strong> ${order.delivery_address}</p>
                      <p><strong>Status:</strong> ${order.order_status ? "Completed" : "Pending"}</p>
                      <hr>
                  `;
                  orderList.appendChild(listItem);
              });
          })
          .catch((error) => console.error("Error fetching order history:", error));
  });
  