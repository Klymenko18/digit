// Функція для видалення товару зі списку бажань
function removeFromWishlist(itemId) {
      // Виконуємо запит до сервера для видалення товару з бажаного списку
      fetch(`/api/wishlist/${itemId}/`, {
          method: 'DELETE',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCookie('csrftoken'),
          },
      })
      .then(response => {
          if (response.ok) {
              alert('Product removed from wishlist');
              location.reload();  // Перезавантажуємо сторінку, щоб відобразити оновлений список
          } else {
              alert('Error removing product');
          }
      })
      .catch(error => {
          alert('An error occurred');
      });
  }
  
  // Функція для отримання CSRF токену з cookie
  function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  