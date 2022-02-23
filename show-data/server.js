const express = require('express');
const mogoose = require('mongoose');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const request = require('request-promise');



function checkauth(username, password){
    var login_info = {'username': username, 'password': password};
    var clientServerOptions = {
        uri: 'http://auth:5000/',
        body: login_info,
        method: 'POST',
        json: true
    }
    var sendrequest = await request(options)
  
        // The parsedBody contains the data
        // sent back from the Flask server 
        .then(function (parsedBody) {
            console.log(parsedBody);
              
            // You can do something with
            // returned data
            let result;
            result = parsedBody['result'];
            console.log("auth function returned: ", result);
            return result;
        })
        .catch(function (err) {
            console.log(err);
        });
    // return 1;

}

app.use(bodyParser.urlencoded({ extended: false }));

app.get('/login', (req,res) => res.sendFile(path.join(__dirname + '/views/login.html')));

app.get('/show', (req,res) => res.sendFile(path.join(__dirname + '/views/output.html')))

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

