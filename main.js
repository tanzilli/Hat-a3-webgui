
/*var slides = [
    { type: "image", file: "sabato_aperti.png" }, 
    { type: "time",  file: "clock.png" },
];*/

var slides = [];
var image_w = 64
var slides_path="slides/"

// Inject in the DOM the palimpsest starting from a array
function showPalimpsest() {
	$("#sortable").text("");

	slides.forEach(function(entry,index) {
	
		if (entry["type"]=="video/mp4") {
			dummy="<video controls='true'><source src='" + slides_path + entry["file"] + "'></video>";
			$("#sortable").append("	\
				<div class='slides alert alert-info' index='" + index + "'> \
					" + dummy + " \
					<p>" + entry["file"] + "<p> \
					<button id='duplicate_button_" + index +"'  index='" + index + "' type='button' class='btn btn-primary'><span class='glyphicon glyphicon-duplicate' aria-hidden='true'></span> Duplicate</button> \
					<button id='remove_button_" + index +"' index='" + index + "' type='button' class='btn btn-danger'><span class='glyphicon glyphicon-trash' aria-hidden='true'></span> Remove</button> \
				</div> \
			");		
		} 
		
		if (entry["type"]=="image/png" || entry["type"]=="image/jpeg" || entry["type"]=="image/gif") {
			dummy="<img src='" + slides_path + entry["file"] + "' width='" + image_w + "px'>";
			$("#sortable").append("	\
				<div class='slides alert alert-info' index='" + index + "'> \
					" + dummy + " \
					<p>" + entry["file"] + "<p> \
					<button id='duplicate_button_" + index +"'  index='" + index + "' type='button' class='btn btn-primary'><span class='glyphicon glyphicon-duplicate' aria-hidden='true'></span> Duplicate</button> \
					<button id='remove_button_" + index +"' index='" + index + "' type='button' class='btn btn-danger'><span class='glyphicon glyphicon-trash' aria-hidden='true'></span> Remove</button> \
				</div> \
			");		
		}

		if (entry["type"]=="text") {
			$("#sortable").append("	\
				<div class='slides alert alert-info' index='" + index + "'> \
					Text: \
					<input class='textvalues' index='" + index +  "' type='text' value='" + entry["value"] + "'> \
					<button id='duplicate_button_" + index +"'  index='" + index + "' type='button' class='btn btn-primary'><span class='glyphicon glyphicon-duplicate' aria-hidden='true'></span> Duplicate</button> \
					<button id='remove_button_" + index +"' index='" + index + "' type='button' class='btn btn-danger'><span class='glyphicon glyphicon-trash' aria-hidden='true'></span> Remove</button> \
				</div> \
			");		
		}
	
	});
	updateEvents();
}

// Load the palimpsest from json file
function loadPalimpsest() {
	$.ajax({
		dataType: "json",
		url: "slides.json",
		success: function(data) {
			data.forEach(function(entry,index) {
				slides.push(entry);
				console.log(entry);
			});
			showPalimpsest();
		}
	});
}

// Create the array from palimpsest inside the DOM and redraw the DOM
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
			if (confirm("Are you sure to remove this file ?") == true) {
				slides.splice($(this).attr("index"),1);			
				showPalimpsest();
			} 
		}
	});

	// Update slides on text input change	
	$(".textvalues").on("change",function(){
		//slides.splice(0,0,{"type":"ptime","file":"icons/ptime.png"});			
		//showPalimpsest();
		//slides[parseInt($(this).attr("index"))]["value"]=$(this).val();
		slides[$(this).attr("index")]["value"]=$(this).val();
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
	
	
	// Save button	
	$("#save").on("click",function(){
		// Aggiorna i campi text nell'array slides con i valori correnti dal DOM

		/*slides.forEach(function(entry,index) {
			slide_list+=entry["file"] + " ";
		});*/
		
		$.ajax({
			method : 'POST',
			url : 'play.php',
			data : { 
				cmd: "save", 
				data: JSON.stringify(slides) 
			},
			success : function(data) {
				warning(data);
			}
		});		
	});

	// Start button	
	$("#play").on("click",function(){
		$.ajax({
			method : 'POST',
			url : 'play.php',
			data : { 
				cmd: "play" 
			},
			success : function(data) {
				warning(data);
			}
		});		
	});

	// Stop button	
	$("#stop").on("click",function(){
		$.ajax({
			method : 'POST',
			url : 'play.php',
			data : { 
				cmd: "stop" 
			},
			success : function(data) {
				warning(data);
			}
		});		
	});

	// Add time button	
	$("#add_ptime").on("click",function(){
		slides.splice(0,0,{"type":"ptime","file":"icons/ptime.png"});			
		showPalimpsest();
	});

	// Add weather button	
	$("#add_pweather").on("click",function(){
		slides.splice(0,0,{"type":"pweather","file":"icons/pweather.png"});			
		showPalimpsest();
	});

	// Add text button	
	$("#add_text").on("click",function(){
		slides.splice(0,0,{"type":"text","value":"Shifting text"});			
		showPalimpsest();
	});

	// File upload
	$("#upload_form").submit(function(event) {
		alert( "Handler for .submit() called." );
		event.preventDefault();
	});
	
	// http://stackoverflow.com/questions/2320069/jquery-ajax-file-upload
	// File to upload selection
	$(':file').change(function(){
		var file = this.files[0];
    	name = file.name;
    	size = file.size;
    	type = file.type;
 		
    	if (!(file.type!="image/gif" || file.type!="image/png" || file.type!="image/jpeg" || file.type!="video/mp4"))  {
			alert( "File type not allowed");
			event.preventDefault();
			return;
    	}
    	if (file.size>20000000) {
			alert( "File type too long (max 20MB)");
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
				info=data.split(",");
				slides.splice(0,0,{"type":info[1],"file":info[0]});
				showPalimpsest();
			}
		});
	});
		
	
});
	