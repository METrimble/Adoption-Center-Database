module.exports = function(){
    var express = require('express');
    var router = express.Router();

    function getEmployee(res, mysql, context, complete){
        mysql.pool.query("select * from employee", function(error, results, fields){
            if(error){
                res.write(JSON.stringify(error));
                res.end();
            }
            context.employee = results;
            complete();
        });
    }

    function getAnimal(res, mysql, context, complete){
        mysql.pool.query("select id from animal", function(error, results, fields){
            if(error){
                res.write(JSON.stringify(error));
                res.end();
            }
            context.animal = results;
            complete();
        });
    }

    function getLocation(res, mysql, context, complete){
        mysql.pool.query("select id from location", function(error, results, fields){
            if(error){
                res.write(JSON.stringify(error));
                res.end();
            }
            context.location = results;
            complete();
        })
    }

    //getEmployee_Animal

    //getEmployee_Location

    router.get('/', function(req, res){
        var callbackCount = 0;
        var context = {};
        var mysql = req.app.get('mysql');
        getEmployee(res, mysql, context, complete);
        function complete(){
            callbackCount++;
            if(callbackCount >= 2){
                res.render('employee', context);
            }
        }
    });

    return router;
}();
