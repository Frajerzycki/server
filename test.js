const axios = require('axios');
const fs = require('mz/fs');

setInterval(function () {
    let temp = 22
    console.log(temp);
    axios.post("http://localhost:5000/info", {
            temperature: temp.toString()
        }).then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}, 5000);