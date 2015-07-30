function dofind(){
	if ($('#id_ci').val() != ""){
		$.get("/rucs/ruc/"+$('#id_ci').val(),
		    function(data) {
		    	if (data != null){
		    		if (data.name.toString() != "") {
			    		$('#id_name').text(data.name)
			    		$('#id_ruc').text(data.ci+"-"+data.dv)
		    		} else {
		    			$('#id_name').text("No se encontró resultado.")
			    		$('#id_ruc').text("")
		    		}
		    	}
		    }
		);  
	}
}