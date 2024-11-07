$(document).ready(function(){
	$('td.editable-col').on('focusout', function() {
		data = {};
		data['val'] = $(this).text();
		data['id'] = $(this).parent('tr').attr('data-row-id');
		data['col'] = $(this).attr('col-name');
		if($(this).attr('oldVal') === data['val'])
		return false;
		
		$.ajax({   
			type: "POST",  
			url: "update-event.php",  
			cache:false,  
			data: data,
			dataType: "json",       
			success: function(response) {
				if(response.status) {
					$("#msg").removeClass('alert-danger');
					$("#msg").addClass('alert-success').html(response.msg);
				} else {
					$("#msg").removeClass('alert-success');
					$("#msg").addClass('alert-danger').html(response.msg);
				}
			}   
		});
	});
  
	$('#add-event').on('click', function() {
		data = {};
		$.ajax( {   
			type: "POST",  
			url: "insert-event.php",  
			cache:false,         
			dataType: "json",
			success: function(response) {   
				if(response.status) {
					$("#msg").removeClass('alert-danger');
					$("#msg").addClass('alert-success').html(response.msg);
					var table = $('#_editable_table');
					var row = table.lastElementChild; 
					table.append('<tr data-row-id="' + response.id + '"></tr>');
					var clone = table.lastElementChild;
					clone.setAttribute("data-row-id", response.id);

					row.children.forEach(function(item) {
						clone.append('<td></td>')
						clone.lastElementChild.html = "";
						clone.lastElementChild.setAttribute("oldval", "");
						clone.lastElementChild.setAttribute("class", "editable-col");
						clone.lastElementChild.setAttribute("contenteditable", "true");
						clone.lastElementChild.setAttribute("col-name", item.getAttribute("col_name"));
					});
					clone.firstElementChild.setAttribute("oldval", response.datum);
					clone.firstElementChild.html = response.datum;
					data['id'] = response.id;
				} else {
					$("#msg").removeClass('alert-success');
					$("#msg").addClass('alert-danger').html(response.msg);
				}
			}   
		});
	});
  
	$('img.remove-event').on('click', function() {
		if (window.confirm("Biztosan törölni szeretnéd?")) {
			data = {};
			data['id'] = $(this).attr('data-row-id');
			$.ajax( {   
				type: "POST",
				url: "remove-event.php",
				cache: false,
				data: data,
				dataType: "json",
				success: function(response) {
					if(response.status) {
						$("#msg").removeClass('alert-danger');
						$("#msg").addClass('alert-success').html(response.msg);
						$("#data-row-" + data['id']).remove();
					} else {
						$("#msg").removeClass('alert-success');
						$("#msg").addClass('alert-danger').html(response.msg);
					}
				}
			});
		}
	});
});