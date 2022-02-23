const express = require('express');
// var mongo = require('mongodb');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');

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


function checkauth(username, password){
    var login_info = {'username': username, 'password': password};
    var options = {
        uri: 'http://auth:5000/',
        body: login_info,
        method: 'POST',
        json: true
    }
  
    var sendrequest =  request(options)
        // The parsedBody contains the data
        // sent back from the Flask server 
        .then(function (parsedBody) {
            console.log(parsedBody);
              
            // You can do something with
            // returned data
            let result;
            result = parsedBody['result'];
            console.log("auth function returned: ", result);
            result = 1;
            return result;
        })
        .catch(function (err) {
            console.log(err);
        });
    return 1;

}

app.use(bodyParser.urlencoded({ extended: false }));

app.get('/login', (req,res) => res.sendFile(path.join(__dirname + '/views/login.html')));

app.get('/show', (req,res) => res.sendFile(path.join(__dirname + '/views/output.html')));

app.post('/login', async (req, res) =>{
    let username = req.body.username;
    let password = req.body.password;

    if(checkauth(username,password) == 1){
        res.redirect('/show');
    }
    else{
        res.redirect('/login');
    }
})



app.listen(9000, () => {
    console.log("app running on port 9000");
})

