#This file is broadly adapted from the CS340_starter_flask_app that was provided to us

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

#This just routes the user from the root page to homepage
@webapp.route('/')
def index():
    return redirect("/homepage")

#This is the routing and function for displaying the homepage.
#It takes no input, has no forms, and simply displays the homepage.
@webapp.route('/homepage')
def homepage():
    return render_template('homepage.html')

#This is the routing and function for displaying the employees page and table.
#It will display the contents of the employee, employee_animal, and employee_location tables.
@webapp.route('/employees')
def disp_employees():
    print("/employees activated...")
    db_connection = connect_to_database()
    query_e = "select * from `employee`;"                           #Get employee table
    result_e = execute_query(db_connection, query_e).fetchall()
    query_ea = "select * from `employee_animal`;"                   #Get employee_animal table
    result_ea = execute_query(db_connection, query_ea).fetchall()
    query_al = "select * from `employee_location`;"                 #Get employee_location table
    result_al = execute_query(db_connection, query_al).fetchall()
    return render_template('Employee.html', rows=result_e, arows=result_ea, lrows=result_al)

#This is the routing and function for displaying the parents page and table.
#It will display the contents of the parents table. 
@webapp.route('/parents')
def disp_parents():
    print("/parents activated...")
    db_connection = connect_to_database()
    query = "select * from `foster_parent`;"                        #Get parents table
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('Foster_Parent.html', rows=result)

#This is the routing and function for displaying the animals page and table.
#When the method is 'GET', it will display the animals table with no filtering.
#When the method is 'POST', it will display the animals table with filtering based on species, as entered by the user.
@webapp.route('/animals', methods=['POST', 'GET'])
def disp_animals():
    db_connection = connect_to_database()
    if request.method == 'GET':                                     #If GET
        print("/animals activated...")
        query = "select * from `animal`;"                           #Get animals table
        result = execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('Animal.html', rows=result)
    elif request.method == 'POST':                                  #If POST
        species = request.form['species']                           #Get contents of inputted form
        query = "select * from `animal` where animal_species = %s"  #Get filtered animals table
        data = (species, )
        result_a = execute_query(db_connection, query, data)
        return render_template('Animal.html', rows=result_a)

#This is the routing and function for displaying the locations page and table.
#It will display the contents of the locations table.
@webapp.route('/locations')
def disp_locations():
    print("/locations activated...")
    db_connection = connect_to_database()
    query = "select * from `location`;"                             #Get locations table
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('Location.html', rows=result) 

#This is the routing and function for displaying the add_parents page.
#When the method is 'GET', it will display the form to get user input.
#When the method is 'POST', it will add the inputted info to the db under the foster_parent table.
@webapp.route('/add_parent', methods=['POST','GET'])
def add_parent():
    print("/add_parent activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':                                     #If GET
        query = "select * from `location`;"                         #Get location table for dropdown menu
        result = execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('Add_Foster_Parent.html', location = result)

    elif request.method == 'POST':                                  #If POST
        print("...Adding new parent")                               #Get contents from form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        location = request.form['location']
        address = request.form['address']
        city = request.form['city']
        zip_code = request.form['zip_code']
        state = request.form['state']                                               #Create query
        query = 'insert into `foster_parent` (`first_name`, `last_name`, `location_id`, `address`, `city`, `zip_code`, `state`) values (%s, %s, %s, %s, %s, %s, %s);'
        data = (first_name, last_name, location, address, city, zip_code, state)    #Assemble data
        execute_query(db_connection, query, data)                                   #Add to table
        return redirect('/parents')                                                 #Redirect to /parents page, which should have the added entry.

#This is the routing and function for displaying the add_animal page.
#When the method is 'GET', it will display the form to get user input.
#When the method is 'POST', it will add the inputted info to the db under the animals table.
@webapp.route('/add_animal', methods=['POST', 'GET'])
def add_animal():
    print("/add_animal activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':                                     #If GET
        query_l = "select * from `location`;"                       #Get contents of location for dropdown
        local = execute_query(db_connection, query_l).fetchall()
        query_p = "select * from `foster_parent`;"                  #Get contents of fp for dropdown
        fp = execute_query(db_connection, query_p).fetchall()
        return render_template('Add_Animal.html', location = local, foster_parent = fp)
    elif request.method == 'POST':                                  #IF POST
        print("...Adding new animal")                               #Get contents of form
        location = request.form['location']
        foster_parent = request.form['foster_parent']
        name = request.form['animal_name']
        species = request.form['species']
        sex = request.form['sex']
        breed = request.form['breed']
        weight = request.form['weight']
        birthdate = request.form['Birthdate']
        s_p = request.form['Spayed/Neutered']
        desc = request.form['Description']                          #Make query
        query = 'insert into `animal` (`location_id`, `foster_parent_id`, `animal_name`, `animal_species`, `animal_sex`, `animal_breed`, `animal_weight`, `birthdate`, `spayed/neutered`, `description`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        data = (location, foster_parent, name, species, sex, breed, weight, birthdate, s_p, desc)   #Assemble data
        execute_query(db_connection, query, data)                   #Add to table
        return redirect('/animals')                                 #Redirect to animals page, which should have the added entry.

#This is the routing and function for displaying the add_location page.
#When the method is 'GET', it will display the form to get user input.
#When the method is 'POST', it will add the inputted info to the db under the location table.
@webapp.route('/add_location', methods=['POST', 'GET'])
def add_local():
    print("/add_location activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':                                     #If GET
        name = None                                                 #No prefilled data to get, so we just display the page
        return render_template('Add_Location.html', name = name)
    elif request.method == 'POST':
        print("...Adding new location")
        address = request.form['address']                           #Get contents from form
        city = request.form['city']
        zipcode = request.form['zip-code']
        state = request.form['state']
        sq_ft = request.form['sq_ft']
        animal_in_rate = request.form['animal_in_rate']                 #Make query
        query = 'insert into `location` (`address`, `city`, `zip_code`, `state`, `sq_ft`, `animal_in_rate`) values (%s, %s, %s, %s, %s, %s);'
        data = (address, city, zipcode, state, sq_ft, animal_in_rate)   #Assemble data
        execute_query(db_connection, query, data)                       #Execute and add the data to the table
        return redirect('/locations')                                   #Redirect to /locations which should have the added entry
    
#This is the routing and function for displaying the add_employee page.
#When the method is 'GET', it will display the form to get user input.
#When the method is 'POST', it will add the inputted info to the db under the employee table.
@webapp.route('/add_employee', methods=['POST', 'GET'])
def add_emp():
    print("/add_employee activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':                                     #If GET
        name = None                                                 #No prefilled data to get, so we just display the page
        return render_template('Add_Employee.html', name = name)
    elif request.method == 'POST':
        print("...Adding new employee")
        fname = request.form['first_name']                          #Get contents from form
        lname = request.form['last_name']
        type = request.form['type']
        p_rate = request.form['pay_rate']
        ssn = request.form['SSN']
        email = request.form['email']
        phone = request.form['phone']
        hours = request.form['hours_worked']
        hired = request.form['hiring_date']                                     #Make query
        query = 'insert into `employee` (`first_name`, `last_name`, `type`, `pay_rate`, `SSN`, `email`, `phone`, `hours_worked`, `hiring_date`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
        data = (fname, lname, type, p_rate, ssn, email, phone, hours, hired)    #Assemble data
        execute_query(db_connection, query, data)                               #Execute and add data to table
        return redirect('/employees')                                           #Redirect to /employees where the added entry should be

#This is the routing and function for displaying the add_emp_animal page.
#When the method is 'GET', it will display the form to get user input.
#When the method is 'POST', it will add the inputted info to the db under the employee_animal table.
@webapp.route('/add_emp_animal', methods=['POST', 'GET'])
def emp_animal():
    print("/add_emp_animal activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':                                     #If GET
        query_e = "select * from employee;"                         #Get data from employee
        emp_result = execute_query(db_connection, query_e)
        query_a = "select * from animal;"                           #Get data from animal
        ani_result = execute_query(db_connection, query_a)
        return render_template('Add_Employee_Animal.html', animal = ani_result, employee = emp_result)
    elif request.method == 'POST':                                  #If POST
        print("...Associating emp + animal")
        emp_id = request.form['employee']                           #Get data
        ani_id = request.form['animal']                             #Make query
        query = "insert into `employee_animal` (`employee_id`, `animal_id`) values (%s, %s);"
        data = (emp_id, ani_id)                                     #Assemble data
        execute_query(db_connection, query, data)                   #Execute and add entry to table
        return redirect('/employees')                               #Redirect to employees where added entry should be

#This is the routing and function for displaying the add_emp_local page.
#When the method is 'GET', it will display the form to get user input.
#When the method is 'POST', it will add the inputted info to the db under the employee_location table.
@webapp.route('/add_emp_local', methods=['POST', 'GET'])
def emp_local():
    print("/add_emp_local activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':                                     #If GET
        query_e = "select * from employee;"                         #Get data from employee
        emp_result = execute_query(db_connection, query_e)  
        query_l = "select * from location;"                         #Get data from location
        locate_result = execute_query(db_connection, query_l)
        return render_template('Add_Employee_Location.html', location = locate_result, employee = emp_result)
    elif request.method == 'POST':                                  #If POST
        print("...Associating emp + location")
        emp_id = request.form['employee']                           #Get content from form                  
        loc_id = request.form['location']                           #Make query
        query = "insert into `employee_location` (`employee_id`, `location_id`) values (%s, %s);"
        data = (emp_id, loc_id)                                     #Assemble data
        execute_query(db_connection, query, data)                   #Execute query and add to table
        return redirect('/employees')                               #Redirect to employees where added entry should be

#This is the routing and function for displaying the update_employee page.
#When the method is 'GET', it will display the form to get updated input.
#When the method is 'POST', it will update the info in the db under the entry in the employee table.
@webapp.route('/update_employee/<int:id>', methods=['POST', 'GET'])
def update_emp(id):
    print("/update_employee activated...")
    db_connection = connect_to_database()
    if request.method == 'GET':                                     #If GET
        query = "select * from employee where id = %s;"             #Get the employee we're updating
        data = (id,)
        result = execute_query(db_connection, query, data)
        return render_template('Update_Employee.html', default = result)
    elif request.method == 'POST':                                  #If POST
        print("...Updating employee")
        fname = request.form['first_name']                          #Get contents from the form
        lname = request.form['last_name']
        type = request.form['type']
        p_rate = request.form['pay_rate']
        ssn = request.form['SSN']
        email = request.form['email']
        phone = request.form['phone']
        hours = request.form['hours_worked']
        hired = request.form['hiring_date']                                         #Make wuery
        query = 'update `employee` set `first_name` = %s, `last_name` = %s, `type` = %s, `pay_rate` = %s, `SSN` = %s, `email` = %s, `phone` = %s, `hours_worked` = %s, `hiring_date` = %s where `id` = %s;'
        data = (fname, lname, type, p_rate, ssn, email, phone, hours, hired, id)    #Assemble data
        execute_query(db_connection, query, data)                                   #Execute query 
        return redirect('/employees')                                               #Redirect to employees, where the updated entry should be

#This is the routing and function for deleting an animal entry
@webapp.route('/delete_animal/<int:id>')
def delete_animal(id):
    db_connection = connect_to_database()
    query = "delete from employee_animal where animal_id = %s"      #Make query to delete from employee_animal
    data = (id,)
    result = execute_query(db_connection, query, data)              #Delete from animal from employee_animal

    query = "delete from animal where id = %s"                      #Make query to delete from animal
    result = execute_query(db_connection, query, data)              #Delete from animal
    return (str(result.rowcount) + "row deleted")