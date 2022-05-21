// load the "node-ini" module and assign it to variable "ini"
let ini = require('node-ini');

// parse the MySQL client configuration file, ~/.my.cnf 
// and extract the configuration info under the "client" key
var path = require('path');
let mysql_config = ini.parseSync(path.join(__dirname, '../../.my.cnf')).client;

// load the "mysql" module 
let mysql = require('mysql');

// create a MySQL connection pool object using the
// database server hostname, database username, 
// database user password, and database name specified
// in the MySQL client configuration file
let pool = mysql.createPool({
    connectionLimit : 10,
    host            : mysql_config.host,
    user            : mysql_config.user,
    password        : mysql_config.password,
    database        : mysql_config.database});

module.exports.pool = pool;
// load the "express" module
let express = require('express');

var bodyParser = require('body-parser');
const { resourceLimits } = require('worker_threads');

// create the Express application object
let app = express();
var handlebars = require('express-handlebars').create({
    defaultLayout:'main',
    });

// get the TCP port number from the ccommandline
let port = process.argv[2];

app.engine('handlebars', handlebars.engine);
app.use(bodyParser.urlencoded({extended:true}));
app.use('/static', express.static('public')); // configure static routing for the '/static/' subdirectory
app.set('view engine', 'handlebars');
app.use(app.router);
routes.initialize(app);
app.set('mysql', mysql);
app.use('/elayne', require('./elayne.js'));
app.use('/jude', require('./jude.js'));
app.use('/', express.static('public'));

/*
app.get('/', (req, res) => { // the arrow notation means: function(req, res) { ...
    mysql_pool.query('show tables;',   // could opt to use a setting on `app` instead of a module variable
               function(error, results, fields) {
                   if (error) {
                       res.write(JSON.stringify(error));
                       res.end();
                   }
                   let table_names = results.map(obj => Object.keys(obj).map(k => obj[k])[0]);
//                 let table_names = results.map(obj => Object.values(obj)[0]);
                   res.write("<html>\n<body>\n<h1>Tables in my CS340 database:</h1>\n<table border=\"1\">\n");
                   table_names.map(table_name => res.write(`<tr><td>${table_name}</td></tr>\n`));
		      res.write("</table>\n");
                   //res.write("<img src=\"static/logo.png\" />\n</body>\n</html>\n");
		      res.end();
		          });
}); 
*/

// start the Node.js webserver
app.listen(port, () => {
  // note, for a string delimited with backticks, there is variable 
    // interpolation within the string
    let pid = require('process').pid;
    console.log(`Example app listening on port ${port}; PID: ${pid}`);
});

