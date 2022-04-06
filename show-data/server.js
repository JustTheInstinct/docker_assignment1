const express = require('express');
// var mongo = require('mongodb');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const request = require('request-promise');

// var MongoClient = require('mongodb').MongoClient;

// var url = "mongodb://mongodb:27017/";

// const content = document.getElementById("content")

// MongoClient.connect(url, function(err, db) {
//     if (err) throw err;
//     var dbo = db.db("data");
//     dbo.collection("info").find({}).toArray(function(err, result) {
//         if (err) throw err;
//         console.log(result);
//         content.innerHTML(result.words)
//         db.close();
//     });
// });

app.use(bodyParser.urlencoded({ extended: false }));

app.get('/login', (req,res) => res.sendFile(path.join(__dirname + '/views/login.html')));

app.get('/show', (req,res) => res.sendFile(path.join(__dirname + '/views/output.html')));

app.post('/login', async (req, res) =>{
    let username = req.body.username;
    let password = req.body.password;
    var login_info_uri = 'http://auth:5000/?username='+username+'&password='+password;

    request(login_info_uri, function (error, response, body) {
        console.error('error:', error);
        console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
        console.log('body:', body); 
        if(body == 1){
            res.redirect('/input');
        }
        else{
            res.redirect('/login');
        }
    });
    
})


app.listen(9000, () => {
    console.log("app running on port 9000");
})

