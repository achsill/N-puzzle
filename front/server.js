const express = require('express')
const path = require('path')
const app = express()

app.use(express.static(path.join(__dirname + '/public')));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/public/base.html'));
})

app.get('/newSqr', function (req, res) {
	//doit launch generate .py
  res.sendFile(path.join(__dirname + '/newSqr.json'));
})

app.get('/solve', function (req, res) {
	//sera du POST car conf de resolution a passer
	//doit launch solve .py avec newSqr.json en param
	// -> genere un solved .json -> renvoie
  res.sendFile(path.join(__dirname + '/solved.json'));
})

app.listen(3000);
