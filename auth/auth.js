const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: false }));

app.post('/check', async (req, res) =>{
    console.log(req)
    let username = req.body.username;
    let password = req.body.password;
    console.log(username);
    console.log(password);

    if(username == 'Jaspreet' && password == 'Password'){
        res.json({result: 1});
    }
    else{
        res.json({result: 0});
    }
});

app.listen(5000, () => {
    console.log("app running on port 5000");
})