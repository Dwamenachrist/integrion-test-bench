const { exec } = require('child_process');
const express = require('express');
const app = express();

app.get('/ping', (req, res) => {
    const target = req.query.target;
    // CRITICAL: Shell Injection vulnerability
    exec(`ping -c 1 ${target}`, (error, stdout, stderr) => {
        if (error) {
            res.status(500).send(stderr);
            return;
        }
        res.send(stdout);
    });
});

// Intentional style noise: unused variables and messy indentation
var x = 10;
  var  y   =   20;

app.listen(3000, () => console.log('Server running on port 3000'));
