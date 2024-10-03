var productModal = $("#productModal");
    $(function () {

        //JSON data by API call
        $.get(productListApiUrl, function (response) {
            if(response) {
                var table = '';
                $.each(response, function(index , products) {
                    table += '<tr data-id="'+ products.Product_ID +'" data-name="'+ products.Product_Name +'" data-unit="'+ products.UOM_ID +'" data-price="'+ products.Price_Per_Unit +'">' +
                        '<td>'+ products.Product_Name +'</td>'+
                        '<td>'+ products.UOM_ID +'</td>'+
                        '<td>'+ products.Price_Per_Unit +'</td>'+
                        '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
                });
                $("table").find('tbody').empty().html(table);
            }
        });
    });

    // Save Product
    $("#saveProduct").on("click", function () {
        // If we found id value in form then update product detail
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            Product_Name: null,
            UOM_ID: null,
            Price_Per_Unit: null
        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'name':
                    requestPayload.Product_Name = element.value;
                    break;
                case 'uoms':
                    requestPayload.UOM_ID = element.value;
                    break;
                case 'price':
                    requestPayload.Price_Per_Unit = element.value;
                    break;
            }
        }
        callApi("POST", productSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });

    $(document).on("click", ".delete-product", function (){
        var tr = $(this).closest('tr');
        var data = {
            Product_ID : tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete " + tr.data('name') +" item?");
        if (isDelete) {
            callApi("POST", productDeleteApiUrl, data);
        }
    });

    productModal.on('hide.bs.modal', function(){
        $("#id").val('0');
        $("#name, #unit, #price").val('');
        productModal.find('.modal-title').text('Add New Product');
    });

    productModal.on('show.bs.modal', function(){
        //JSON data by API call
        $.get(uomListApiUrl, function (response) {
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, uom) {
                    options += '<option value="'+ uom.UOM_ID +'">'+ uom.UOM_Name +'</option>';
                });
                $("#uoms").empty().html(options);
            }
        });
    });