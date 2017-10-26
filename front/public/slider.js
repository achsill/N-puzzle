var current = [];

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

	var allBoxes = document.getElementsByClassName("tile");
	for (var i = 0; i < allBoxes.length; i++)
	{
		console.log(allBoxes[i].innerHTML);
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
	
	for (var i = 0; i < 3; i++)
	{
		for (var j = 0; j < 3; j++)
		{
			if (array[i][j] !== current[i][j])
			{
				var change = array[i][j] == 0 ?
					current[i][j] :
					array[i][j];
			}
		}
	}
	swapBoxes(change);

}
