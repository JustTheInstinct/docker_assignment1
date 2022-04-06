const express = require('express');
const mysql = require('mysql');
const app = express();
const path = require('path');
const request = require('request');
const bodyParser = require('body-parser');

const database = mysql.createConnection({
    host: 'mysql',
    port: '3306',
    user: 'root',
    password: 'P@ssw0rd',
    database: 'data'
});

// setTimeout(checkauth, 4000);
//  function checkauth(username, password){
    // var login_info_uri = 'http://auth:5000/?username='+username+'&password='+password;

//      request(login_info_uri, function (error, response, body) {
//         console.error('error:', error);
//         console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
//         console.log('body:', body); 
//     });
//     return result;
//  }



app.use(bodyParser.urlencoded({ extended: false }));

app.get('/login', (req,res) => res.sendFile(path.join(__dirname + '/views/login.html')));

app.get('/input', (req,res) => res.sendFile(path.join(__dirname + '/views/input.html')))

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

app.post('/input', (req,res) => {
    let age = req.body.age;

    database.connect(function(err) {
        if (err) throw err;

        console.log("Connected!");
        var sql = "INSERT INTO info (words) VALUES (" + age +")";

        database.query(sql, function (err, result) {
          if (err) throw err;
          console.log("1 record inserted");
        });
      });

    res.redirect('/input');
})
app.listen(8000, () => {
    console.log("app running on port 8000");
})

