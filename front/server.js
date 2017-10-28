const express = require('express')
const path = require('path')
const app = express()

app.use(express.static(path.join(__dirname + '/public')));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/public/base.html'));
})

app.get('/newSqr', function (req, res) {
  res.sendFile(path.join(__dirname + '/newSqr.json'));
})

app.get('/solve', function (req, res) {
  res.sendFile(path.join(__dirname + '/solved.json'));
})

app.listen(3000);
