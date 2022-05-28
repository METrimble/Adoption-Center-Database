#This file is broadly adapted from the CS340_starter_flask_app that was provided to us
#employee
    #insert
    #update
    #delete
#foster_parent
    #insert
    #update
    #delete
#animal
    #insert
    #update
    #delete
#location
    #insert
    #update
    #delete

from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#here's a basic function for understanding how flask works
@webapp.route('/test')                                      #This part means when the webpage is routed to a page (in this case /test), we'll do whatever is under this
def hello():                                                #This defines the function that we'll be doing (mostly a cosmetic thing)
    print("/test activated...")                             #print statement so that you can look in the terminal for debugging
    db_connection = connect_to_database()                   #set the variable db_connection to output from connect_to_database() function (we need this for later functions)
    query = "SHOW TABLES;"                                  #set our query to whatever we want it to be
    result = execute_query(db_connection, query).fetchall() #Get our result from the execute_query() function, using our db_connection and query vars, use fetchall()
    print(result)                                           #print result to terminal for debugging
    return render_template('test.html', rows=result)        #return render_template((page you want), rows=result) to render the page

@webapp.route('/homepage')
def homepage():
    return render_template('homepage.html')

#main employees page
@webapp.route('/employees')
def disp_employees():
    print("/employees activated...")
    db_connection = connect_to_database()
    query = "select * from `employee`;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('Employee.html', rows=result)

#main foster parents page
@webapp.route('/parents')
def disp_parents():
    print("/parents activated...")
    db_connection = connect_to_database()
    query = "select * from `foster_parent`;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('Foster_Parent.html', rows=result)

#main animals page
@webapp.route('/animals')
def disp_animals():
    print("/animals activated...")
    db_connection = connect_to_database()
    query = "select * from `animal`;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('Animal.html', rows=result) 

#main locations page
@webapp.route('/locations')
def disp_locations():
    print("/locations activated...")
    db_connection = connect_to_database()
    query = "select * from `location`;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('Location.html', rows=result) 

#add parents page
@webapp.route('/add_parent', methods=['POST','GET'])
def add_parent():
    print("/add_parent activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = "select * from `location`;"
        result = execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('Add_Foster_Parent.html', location = result)

    elif request.method == 'POST':
        print("...Adding new parent")
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        location = request.form['location']
        address = request.form['address']
        city = request.form['city']
        zip_code = request.form['zip_code']
        state = request.form['state']
        query = 'insert into `foster_parent` (`first_name`, `last_name`, `location_id`, `address`, `city`, `zip_code`, `state`) values (%s, %s, %s, %s, %s, %s, %s);'
        data = (first_name, last_name, location, address, city, zip_code, state)
        execute_query(db_connection, query, data)
        return redirect('/parents')

@webapp.route('/add_animal', methods=['POST', 'GET'])
def add_animal():
    print("/add_animal activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':
        query_l = "select * from `location`;"
        local = execute_query(db_connection, query_l).fetchall()
        query_p = "select * from `foster_parent`;"
        fp = execute_query(db_connection, query_p).fetchall()
        return render_template('Add_Animal.html', location = local, foster_parent = fp)
    elif request.method == 'POST':
        print("...Adding new animal")
        location = request.form['location']
        foster_parent = request.form['foster_parent']
        name = request.form['name']
        species = request.form['species']
        sex = request.form['sex']
        breed = request.form['breed']
        weight = request.form['weight']
        birthdate = request.form['birthdate']
        s_p = request.form['Spayed/Neutered']
        desc = request.form['Description']
        query = 'insert into `animal` (`location_id`, `foster_parent_id`, `animal_name`, `animal_species`, `animal_breed`, `animal_weight`, `birthdate`, `spayed/neutered`, `description`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
        data = (location, foster_parent, name, species, sex, breed, weight, birthdate, s_p, desc)
        execute_query(db_connection, query, data)
        return redirect('/animals')

@webapp.route('/add_location', methods=['POST', 'GET'])
def add_local():
    print("/add_location activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':
        name = None
        return render_template('Add_Location.html', name = name)
    elif request.method == 'POST':
        print("...Adding new location")
        address = request.form['address']
        city = request.form['city']
        zipcode = request.form['zipcode']
        state = request.form['state']
        sq_ft = request.form['sq_ft']
        animal_in_rate = request.form['animal_in_rate']
        query = 'insert into `location` (`address`, `city`, `zip_code`, `state`, `sq_ft`, `animal_in_rate`) values (%s, %s, %s, %s, %s, %s);'
        data = (address, city, zipcode, state, sq_ft, animal_in_rate)
        execute_query(db_connection, query, data)
        return redirect('/locations')
    

@webapp.route('/add_employee', methods=['POST', 'GET'])
def add_emp():
    print("/add_employee activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':
        name = None
        return render_template('Add_Employee.html', name = name)
    elif request.method == 'POST':
        print("...Adding new employee")
        fname = request.form['first_name']
        lname = request.form['last_name']
        type = request.form['type']
        p_rate = request.form['pay_rate']
        ssn = request.form['SSN']
        email = request.form['email']
        phone = request.form['phone']
        hours = request.form['hours_worked']
        hired = request.form['hiring_date']
        query = 'insert into `employee` (`first_name`, `last_name`, `type`, `pay_rate`, `SSN`, `email`, `phone`, `hours_worked`, `hiring_date`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
        data = (fname, lname, type, p_rate, ssn, email, phone, hours, hired)
        execute_query(db_connection, query, data)
        return redirect('/employees')
    



#EVERYTHING AFTER THIS IS EXAMPLE CODE TO LOOK AT 
@webapp.route('/add_new_people', methods=['POST','GET'])
def add_new_people():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT id, name from bsg_planets'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('people_add_new.html', planets = result)
    elif request.method == 'POST':
        print("Add new people!")
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = 'INSERT INTO bsg_people (fname, lname, age, homeworld) VALUES (%s,%s,%s,%s)'
        data = (fname, lname, age, homeworld)
        execute_query(db_connection, query, data)
        return ('Person added!')

@webapp.route('/')
def index():
    return "<p>Are you looking for /db_test or /hello or <a href='/browse_bsg_people'>/browse_bsg_people</a> or /add_new_people or /update_people/id or /delete_people/id </p>"

@webapp.route('/home')
def home():
    db_connection = connect_to_database()
    query = "DROP TABLE IF EXISTS diagnostic;"
    execute_query(db_connection, query)
    query = "CREATE TABLE diagnostic(id INT PRIMARY KEY, text VARCHAR(255) NOT NULL);"
    execute_query(db_connection, query)
    query = "INSERT INTO diagnostic (text) VALUES ('MySQL is working');"
    execute_query(db_connection, query)
    query = "SELECT * from diagnostic;"
    result = execute_query(db_connection, query)
    for r in result:
        print(f"{r[0]}, {r[1]}")
    return render_template('home.html', result = result)

@webapp.route('/db_test')
def test_database_connection():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * FROM `location`;"
    result = execute_query(db_connection, query)
    return render_template('db_test.html', rows=result)

#display update form and process any updates, using the same function
@webapp.route('/update_people/<int:id>', methods=['POST','GET'])
def update_people(id):
    print('In the function')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        people_query = 'SELECT id, fname, lname, homeworld, age from bsg_people WHERE id = %s'  % (id)
        people_result = execute_query(db_connection, people_query).fetchone()

        if people_result == None:
            return "No such person found!"

        planets_query = 'SELECT id, name from bsg_planets'
        planets_results = execute_query(db_connection, planets_query).fetchall()

        print('Returning')
        return render_template('people_update.html', planets = planets_results, person = people_result)
    elif request.method == 'POST':
        print('The POST request')
        character_id = request.form['character_id']
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = "UPDATE bsg_people SET fname = %s, lname = %s, age = %s, homeworld = %s WHERE id = %s"
        data = (fname, lname, age, homeworld, character_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_bsg_people')

@webapp.route('/delete_people/<int:id>')
def delete_people(id):
    '''deletes a person with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM bsg_people WHERE id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")
