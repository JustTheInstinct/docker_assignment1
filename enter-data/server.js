const express = require('express');
const mysql = require('mysql');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
// const database = mysql.createConnection({
//     host: 'mysql',
//     port: '3306',
//     user: 'root',
//     password: 'P@ssw0rd',
//     database: 'data'
// });

// database.connect()

app.use(bodyParser.json())

app.get('/login', (req,res) => res.sendFile(path.join(__dirname + '/views/login.html')));

app.post('/login', async (req, res) =>{
    console.log(req.body);
    res.json({ status: 'ok' })
})

app.listen(8000, () => {
    console.log("app running on port 8000");
})

