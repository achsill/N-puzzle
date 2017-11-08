const express = require('express')
const path = require('path')
const app = express()
const spawn = require("child_process").spawn;
var fs = require('fs');

app.use(express.static(path.join(__dirname + '/front/public')));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/front/public/base.html'));
})

app.get('/newSqr', function (req, res) {
  fs.unlinkSync("./front/newSqr.txt");
  fs.unlinkSync("./front/newSqr.json");
  //doit launch generate .py
  const process = spawn('python',["./puzzle_gen.py", "-s", "3"]);
  process.on('close', () => {

    const process2 = spawn('python',["./npuzzle.py", "-iw"]);
    process2.on('close', () => {
      res.sendFile(path.join(__dirname + '/front/newSqr.json'));
    })

    process2.stdout.on('data',function(chunk){

      var textChunk = chunk.toString('utf8');// buffer to string
      fs.appendFile("./front/newSqr.json", textChunk, function(err) {
        if(err) {
          return console.log(err);
        }
        console.log("The file was saved!");
      }); 
    });
  })

  process.stdout.on('data',function(chunk){

    console.log("oijoijoij saved!");
    var textChunk = chunk.toString('utf8');// buffer to string
    fs.appendFile("./front/newSqr.txt", textChunk, function(err) {
      if(err) {
        return console.log(err);
      }
      console.log("The file was saved!");
    }); 
  });
})

app.get('/solve', function (req, res) {
  console.log('recevied', req.query.heuristic);

  let heur = req.query.heuristic;
  if (heur === "m" || heur === "ml" || heur === "mt")
  {
    const process = spawn('python',["./npuzzle.py", "./front/newSqr.json", `-w`, `-${heur}`]);

    process.stdout.on('data',function(chunk){

      var textChunk = chunk.toString('utf8');// buffer to string
      fs.appendFile("./front/solved.json", textChunk, function(err) {
        if(err) {
          return console.log(err);
        }
      }); 
    });
    process.on('close', () => {
      res.sendFile(path.join(__dirname + '/front/solved.json'));
    })
  } else {
    res.send("lol");
  }

})

app.listen(3000);
