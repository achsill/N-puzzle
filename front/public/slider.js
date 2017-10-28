
function initiateSquare(array){
	current = array;
	array.forEach(line => {
		line.forEach(boxNb => {
			let box = document.createElement("div");
			if (boxNb !== 0)
				box.className = "tile";
			else
				box.className = "tile empty";
			box.innerHTML = boxNb;

			document
				.getElementById('puzzle')
				.appendChild(box);
		})
	})
}

function swapBoxes(change){
	console.log(`change is at ${change}`);
	var allBoxes = document.getElementsByClassName("tile");
	for (var i = 0; i < allBoxes.length; i++)
	{
		if (allBoxes[i].innerHTML == 0)
		{
			allBoxes[i].className = "tile";
			allBoxes[i].innerHTML = change;
		}
		else if (allBoxes[i].innerHTML == change)
		{
			allBoxes[i].className = "tile empty";
			allBoxes[i].innerHTML = 0;
		}
	}
}

function newSquare(array){

	console.log(`this is arr received ${array}`);
	for (var i = 0; i < 3; i++)
	{
		for (var j = 0; j < 3; j++)
		{
			if (array[i][j] !== current[i][j])
			{
				var change = array[i][j] === 0 ?
					current[i][j] :
					array[i][j];
			}
		}
	}
	swapBoxes(change);
	current = array;
}

function showSteps(steps, i){
	console.log(`steps recevied - ${steps}`);
	if (i === steps.length)
		return ;
	
	setTimeout(function () {
		newSquare(steps[i]);
		showSteps(steps, i + 1);
	}, 1000);
}


function all(){
	document.getElementById("generate").onclick = () => {

		var request = new XMLHttpRequest();
		request.open('GET', '/newSqr', true);
		
		request.onload = function() {
		  if (request.status >= 200 && request.status < 400) {
			var newSqr = JSON.parse(request.responseText);
			initiateSquare(newSqr.sqr);
		  } else {
			console.log('PB lol', request);
		  }
		};
		request.onerror = function() {
			console.log('real error');
		};
		
		request.send();
	};

	document.getElementById("solve").onclick = () => {

		var request = new XMLHttpRequest();
		request.open('GET', '/solve', true);
		
		request.onload = function() {
		  if (request.status >= 200 && request.status < 400) {
			var solution = JSON.parse(request.responseText);
			showSteps(solution.steps, 1);
		  } else {
			console.log('PB lol', request);
		  }
		};
		request.onerror = function() {
			console.log('real error');
		};
		
		request.send();
	};
}

function ready(all) {
	if (document.attachEvent ? document.readyState === "complete" : document.readyState !== "loading"){
		all();
	} else {
		document.addEventListener('DOMContentLoaded', all);
	}
}
