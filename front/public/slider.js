
function initiateSquare(array){
	current = array;
	for (var y = 0; y < array.length; y++)
	{
		for (var x = 0; x < array[y].length; x++)
		{
			let boxNb = array[y][x];
			let box = document.createElement("div");
			if (boxNb !== 0)
				box.className = "tile";
			else
				box.className = "tile empty";
			box.innerHTML = boxNb;
			box.style.left = `${x * 82}px`;
			box.style.top = `${y * 82}px`;

			document
				.getElementById('puzzle')
				.appendChild(box);
		}
	}
}

function getSwapDir(pos){
	var swap = {};
	if (pos.from.x !== pos.to.x)
	{
		swap.dir = "left";
		swap.val =  pos.from.x < pos.to.x ? 82 : -82;
		return swap;
	} else {
		swap.dir = "top";
		swap.val =  pos.from.y < pos.to.y ? 82 : -82;
		return swap;
	}
}

function getOpposedSwapDir(swap){
	var oppposedSwap = {};
	oppposedSwap.dir = swap.dir;
	oppposedSwap.val = -swap.val;
	return oppposedSwap;
}

function swapBoxes(change, pos){
	console.log(`change is at ${change}`);
	var allBoxes = document.getElementsByClassName("tile");
	var swap = getSwapDir(pos);
	var oppposedSwap = getOpposedSwapDir(swap);
	for (var i = 0; i < allBoxes.length; i++)
	{
		if (allBoxes[i].innerHTML == 0)
		{
			let oldValue = parseInt(allBoxes[i].style[swap.dir]);
			allBoxes[i].style[swap.dir] = `${oldValue + swap.val}px`;
		}
		else if (allBoxes[i].innerHTML == change)
		{
			let oldValue = parseInt(allBoxes[i].style[oppposedSwap.dir]);
			allBoxes[i].style[oppposedSwap.dir] = `${oldValue + oppposedSwap.val}px`;
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
	}, 2000);
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
		var e = document.getElementById("heuristicType");
		var heuristic = e.options[e.selectedIndex].value;
		console.log('ready to heur', heuristic);

		var request = new XMLHttpRequest();
		request.open('GET', `/solve?heuristic=${heuristic}`, true);
		
		request.onload = function() {
		  if (request.status >= 200 && request.status < 400) {
			var solution = JSON.parse(request.responseText);
			  showSteps(solution.steps, 1);
        document.getElementById("numberOfMoves").textContent = solution.number_of_moves;
        document.getElementById("complexity").textContent = solution.number_in_openList;
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
