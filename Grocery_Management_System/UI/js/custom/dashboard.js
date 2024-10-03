$(function () {
    //Json data by api call for order table
    $.get(orderListApiUrl, function (response) {
        if(response) {
            var table = '';
            var totalCost = 0;
            $.each(response, function(index, orders) {
                totalCost += parseFloat(orders.total);
                table += '<tr>' +
                    '<td>'+ orders.Date_Time +'</td>'+
                    '<td>'+ orders.Order_ID +'</td>'+
                    '<td>'+ orders.Customer_Name +'</td>'+
                    '<td>'+ orders.Total.toFixed(2) +' Rs</td></tr>';
            });
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>'+ totalCost.toFixed(2) +' Rs</b></td></tr>';
            $("table").find('tbody').empty().html(table);
        }
    });
});