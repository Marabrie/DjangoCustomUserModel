console.log('linked')

let shoppingCart = (function()
{
cart = [];

//constructor
function Item(name, price, count) {
    this.name = name;
    this.price = price;
    this.count = count;
}
// Save cart
function saveCart() {

sessionStorage.setItem('shoppingCart',
JSON.stringify(cart));
console.log(sessionStorage['shoppingCart'])
  }

  //Load cart
  function loadCart(){
      cart =
JSON.parse(sessionStorage.getItem('shoppingCart'));
  }
  if (sessionStorage.getItem("shoppingCart") !=null) {
      loadCart();
  }

  let obj = {};

  //Add to cart
  obj.addItemToCart =
  function(name, price, count) {
      for(let item in cart) {
          if(cart[item].name == name) {
              cart[item].count ++;
              saveCart();
              return;
          }
        }
        let item = new Item(name, price, count);
        cart.push(item);
        console.log(name, price)
        saveCart();
    }
    
    //Set count from item
    obj.setCountForItem =
    function(name, count) {
        for(let i in cart) {
            if (cart[i].name === name) {
                cart[i].count = count;
                break;
              }
            }
          };
//Remove item from cart
obj.removeItemFromCart = 
function(name) {
    for(let item in cart) {
        if(cart[item].name === name) {
            if(cart[item].count === 0) {
                cart.splice(item, 1);  
        }
        break;
      }
    }
    saveCart();
    }

    //Remove all items from cart
    obj.removeItemFromCartAll = function(name) {
      console.log('remove all')
        for(let item in cart) {
            if(cart[item].name === name) {
                cart.splice(item, 1);
                break;
              }
            }
            saveCart();
          }

          //Clear Cart
          obj.clearCart = function() {
              cart = [];
              saveCart();
          }

          // //Count cart
          // obj.totalCount = function()
          // {
          //   let totalCount = 0;
          //   for(let item in cart) {
          //       totalCount +=
          // cart[item].count;
          //   } 
          //   return totalCount; 
          // } 

 //Total cart
 obj.totalCart = function() {
    let totalCart = 0;
    for(let item in cart) {
        totalCart += 
    cart[item].price *
    cart[item].count;
        }
        console.log(totalCart)
        return Number(totalCart.toFixed(2));
      } 
//List cart
obj.listCart = function() {
    let cartCopy = [];
    for(i in cart) {
        item = cart[i];
        itemCopy = {};
        for(p in item) {
            itemCopy[p] = item[p];

        }
        itemCopy.total =
Number(item.price * item.count).toFixed(2);
        cartCopy.push(itemCopy)
    }
    return cartCopy;
}

// cart : Array
// Item : Object/Class
// addItemToCart : Function
// removeItemFromCart : Function
// removeItemFromCartAll : Function
// clearCart : Function
// countCart : Function
// totalCart : Function
// listCart : Function
// saveCart : Function
// loadCart : Function
return obj;
})();

//Triggers / Events


//Add item
$('.add-to-cart').click(function(event) {
    event.preventDefault();
    let name =
$(this).data('name');
    let price =
Number($(this).data('price'));
console.log(price)

shoppingCart.addItemToCart(name, price, 1);
    displayCart();
});




function displayCart() {
  console.log('displayCart')
    let cartArray =
    shoppingCart.listCart();
    console.log(cartArray)
    var output = "";
    for(var i in cartArray) {
      output += "<tr>"
        + "<td>" + cartArray[i].name + "</td>" 
        + "<td>(" + cartArray[i].price + ")</td>"
        
        + " = " 
        + "<td>" + cartArray[i].total + "</td>" 
        +  "</tr>"
        
    }
    output += "<tr><th>total</th><td class='total-cart'></td></tr>"
    console.log(output)
    $('.show-cart').html(output);
    console.log(shoppingCart.totalCart())
    $('.total-cart').html(shoppingCart.totalCart());
   
 
  }
   // Clear items
  $('.clear-cart').click(function () {
    shoppingCart.clearCart();
    displayCart();
  });
  
  // Delete item button
  
  $('.show-cart').on("click", ".delete-item", function(event) {
    console.log('delete')
    var name = $(this).data('name')
    shoppingCart.removeItemFromCartAll(name);
    displayCart();
  })
  
  
  // -1
  $('.show-cart').on("click", ".minus-item", function(event) {
    var name = $(this).data('name')
    shoppingCart.removeItemFromCart(name);
    displayCart();
  })
  // +1
  $('.show-cart').on("click", ".plus-item", function(event) {
    var name = $(this).data('name')
    shoppingCart.addItemToCart(name);
    displayCart();
  })
  
  // Item count input
  $('.show-cart').on("change", ".item-count", function(event) {
     var name = $(this).data('name');
     var count = Number($(this).val());
    shoppingCart.setCountForItem(name, count);
    displayCart();
  });
  
  displayCart();
  
