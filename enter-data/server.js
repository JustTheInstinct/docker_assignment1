const express = require('express');
const mysql = require('mysql');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const request = require('request');
// const database = mysql.createConnection({
//     host: 'mysql',
//     port: '3306',
//     user: 'root',
//     password: 'P@ssw0rd',
//     database: 'data'
// });

// database.connect()
function checkauth(username, password){
    var clientServerOptions = {
        uri: 'http://auth:5000',
        body: {'username': username, 'password': password},
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    }
    request(clientServerOptions, function (error, response) {
        console.log(error,response.body);
        return ;
    });

}

app.use(bodyParser.urlencoded({ extended: false }));

app.get('/login', (req,res) => res.sendFile(path.join(__dirname + '/views/login.html')));

app.get('/input', (req,res) => res.sendFile(path.join(__dirname + '/views/input.html')))
app.post('/login', async (req, res) =>{
    let username = req.body.username;
    let password = req.body.password;
    if(checkauth(username,password) == 1){
        res.redirect('/input');
    }
})

app.post('/input', (req,res) => {
    let age = req.body.age;
    res.send(age);
})
app.listen(8000, () => {
    console.log("app running on port 8000");
})

