$(document).foundation()

$(document).ready(function(){
    $('#add_medicine_to_table').click(function(){
        var item_id = $('#id_item').val();
        alert(item_id);
    });

    $('#id_item').change(function(){
        get_medicine_details_and_calculate($(this).val())
    });
});

function get_medicine_details_and_calculate(recieved_item_id){
    $.ajax({
        type:'get',
        url:'pharmacy/ajax/get_medicine_info/',
        data:{
            'medicine_item_id': recieved_item_id
        },
        success:function(e){
          alert("worked");
        },
        error:function(){
          alert(';error');
        }
    });
}