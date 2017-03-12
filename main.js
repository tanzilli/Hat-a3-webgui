
/*var slides = [
    { type: "image", file: "sabato_aperti.gif" }, 
    { type: "image", file: "nome_negozio.gif" },
    { type: "image", file: "foto_negozio.gif" },
    { type: "image", file: "vernici_colori.gif" },
    { type: "image", file: "duplicazione_chiavi.gif" },
    { type: "image", file: "orario.gif" },
];*/

var slides = [];

// Rigenera il palinsesto a partire da un Array
function showPalimpsest() {
	$("#sortable").text("");

	slides.forEach(function(entry,index) {
		$("#sortable").append("	\
			<div class='slides alert alert-info' index='" + index + "'> \
				<img src='" + entry["file"] + "' width='256px'> \
				<button id='duplicate_button_" + index +"'  index='" + index + "' type='button' class='btn btn-primary'><span class='glyphicon glyphicon-duplicate' aria-hidden='true'></span> Duplicate</button> \
				<button id='remove_button_" + index +"' index='" + index + "' type='button' class='btn btn-danger'><span class='glyphicon glyphicon-trash' aria-hidden='true'></span> Remove</button> \
			</div> \
		");		
	});
	updateEvents();
}

// Carica il palinsesto corrente dal pannello
function loadPalimpsest() {
	$.ajax({
		dataType: "json",
		url: "slides.json",
		success: function(data) {
			data.forEach(function(entry,index) {
				slides.push(entry);
			});
			showPalimpsest();
		}
	});
}


// Rigenera l'array a partire dal palinsesto
// e ridisegna il palinsesto
function updateArray() {
    var slides_copy=[];

	$(".slides" ).each(function(index) {
		//console.log("A- " + index + " : " + slides[$(this).attr("index")]["file"]);
		slides_copy.push(slides[$(this).attr("index")]);
	});	

    slides=[];

	slides_copy.forEach(function(entry,index) {
		//console.log("B- " + index + " : " + entry["file"]);
		slides.push(entry);
	});

	showPalimpsest();
}

function updateEvents() {
	$(".btn").on("click",function(){
		if ($(this).html().search("Duplicate")>-1) {
			slides.push(slides[$(this).attr("index")]);			
			showPalimpsest();
		}

		if ($(this).html().search("Remove")>-1) {
			slides.splice($(this).attr("index"),1);			
			showPalimpsest();
		}
	});
}

function warning(text) {
	$("#warning").text(text);
}

$(document).ready(function() {
	// Clear della console Javascript
	console.API;
	if (typeof console._commandLineAPI !== 'undefined') {
	    console.API = console._commandLineAPI; //chrome
	} else if (typeof console._inspectorCommandLineAPI !== 'undefined') {
	    console.API = console._inspectorCommandLineAPI; //Safari
	} else if (typeof console.clear !== 'undefined') {
	    console.API = console;
	}
	console.API.clear();

	console.log("Start");
	
	//console.log(JSON.stringify(slides));
	
	loadPalimpsest();

	$( "#sortable" ).sortable();
	$( "#sortable" ).disableSelection();
	
	$("#sortable").on("sortupdate",function(event,ui) {
		updateArray();
	});
	
	
	// Gestione tasto Play	
	$("#play").on("click",function(){
		// Invia a play.php il contenuto da salvare nel file slides.env
		slide_list="";
		slides.forEach(function(entry,index) {
			slide_list+=entry["file"] + " ";
		});
		
		$.ajax({
			method : 'POST',
			url : 'play.php',
			data : { 
				cmd: "play", 
				value: "SLIDE_LIST='" + slide_list + "'", 
				data: JSON.stringify(slides) 
			},
			success : function(data) {
				warning("Play success");
			}
		});		
	});

	// Gestione tasto Stop	
	$("#stop").on("click",function(){
		$.ajax({
			method : 'POST',
			url : 'play.php',
			data : { 
				cmd: "stop" 
			},
			success : function(data) {
				warning("Stop success");
			}
		});		
	});

	// Gestisce il pulsante Upload di un file
	$("#upload_form").submit(function(event) {
		alert( "Handler for .submit() called." );
		event.preventDefault();
	});
	
	//http://stackoverflow.com/questions/2320069/jquery-ajax-file-upload
	// Gestisce la selezione del file da scaricare
	$(':file').change(function(){
		var file = this.files[0];
    	name = file.name;
    	size = file.size;
    	type = file.type;
    	
    	if (file.type!="image/gif") {
			alert( "File type not allowed");
			event.preventDefault();
			return;
    	}
    	if (file.size>2000000) {
			alert( "File type too long (max 2MB)");
			event.preventDefault();
			return;
    	}
    	
		var formData = new FormData();
		formData.append('userfile', file);

		$.ajax({
			url : 'upload.php',
			type : 'POST',
			data : formData,
			processData: false,  // tell jQuery not to process the data
			contentType: false,  // tell jQuery not to set contentType
			success : function(data) {
				warning(data);
				slides.push({"type":"image","file":data});
				showPalimpsest();
			}
		});
	});
		
	
});
	