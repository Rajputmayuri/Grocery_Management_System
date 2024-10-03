// Define your api here
var productListApiUrl = 'http://127.0.0.1:5000/getproducts';
var uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var orderListApiUrl = 'http://127.0.0.1:5000/getAllOrders';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

// For product drop in order
var productsApiUrl = 'https://fakestoreapi.com/products';

function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    });
}

function calculateValue() {
    var total = 0;
    $(".product-item").each(function( index ) {
        var qty = parseFloat($(this).find('.product-qty').val());
        var price = parseFloat($(this).find('#product_price').val());
        price = price*qty;
        $(this).find('#item_total').val(price.toFixed(2));
        total += price;
    });
    $("#Total").val(total.toFixed(2));
}

function orderParser(orders) { 
    return {
        id : orders.id,
        date : orders.employee_name,
        orderNo : orders.employee_name,
        Customer_Name : orders.employee_name,
        cost : parseInt(orders.employee_salary)
    }
}

function productParser(products) {
    return {
        id : products.id,
        name : products.employee_name,
        unit : products.employee_name,
        price : products.employee_name
    }
}

function productDropParser(products) {
    return {
        id : product.id,
        name : product.title
    }
}

//To enable bootstrap tooltip globally
// $(function () {
//     $('[data-toggle="tooltip"]').tooltip()
// });