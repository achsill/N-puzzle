
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

function getSwapDir(pos){
	if (pos.from.x !== pos.to.x)
		return pos.from.x < pos.to.x ? "swap_right" : "swap_left";
	else
		return pos.from.y < pos.to.y ? "swap_down" : "swap_up";
}

function getOpposedSwapDir(swap){
	if (swap === "swap_right")
		return "swap_left";
	if (swap === "swap_left")
		return "swap_right";
	if (swap === "swap_up")
		return "swap_down";
	if (swap === "swap_down")
		return "swap_up";
}

function swapBoxes(change, pos){
	console.log(`change is at ${change}`);
	var allBoxes = document.getElementsByClassName("tile");
	var swap = getSwapDir(pos);
	var opposedSwap = getOpposedSwapDir(swap);
	for (var i = 0; i < allBoxes.length; i++)
	{
		if (allBoxes[i].innerHTML == 0)
		{
			allBoxes[i].className = `tile `;//add opposedSwap
			allBoxes[i].innerHTML = change;
		}
		else if (allBoxes[i].innerHTML == change)
		{
			allBoxes[i].className = `tile empty ${swap}`;
			allBoxes[i].innerHTML = 0;
		}
	}
	console.log(`empty is moving ${swap}`);
}

function newSquare(newArray){

	var pos = {};
	console.log(`this is arr received ${newArray}`);
	for (var y = 0; y < 3; y++)
	{
		for (var x = 0; x < 3; x++)
		{
			if (newArray[y][x] !== current[y][x])
			{
					if (newArray[y][x] === 0) {
						var change = current[y][x];
						pos.to = {y, x};
					} else {
						var change = newArray[y][x];
						pos.from = {y, x};
					}
			}
		}
	}
	swapBoxes(change, pos);
	current = newArray;
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
