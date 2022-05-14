--Data Manipulation for Adoption Center
--Employee
--Add Employee
insert into `employee` (`first_name`, `last_name`, `type`, `pay_rate`, `SSN`, `email`, `phone`, `hours_worked`, `hiring_date`)
values (:first_namein, :last_namein, :typein, :pay_ratein, :SSNin, :emailin, :phonein, :hours_workedin, :hiring_datein);

--ADD TO HTML PAGE: TEXT FORMS FOR ANIMAL_ID AND lOCATION_ID
insert into `employee_animal` (`employee_id`, `animal_id`) values ((select `id` from `employee` where `first_name` = :first_namein and `last_name` = :last_namein), :animal_idin);

insert into `employee_location` (`employee_id`, `location_id`) values ((select `id` from `employee` where `first_name` = :first_namein and `last_name` = :last_namein), :location_idin)

--Update Emplopyee
--UPDATE bsg_people SET fname = :fnameInput, lname= :lnameInput, homeworld = :homeworld_id_from_dropdown_Input, age= :ageInput WHERE id= :character_ID_from_the_update_form
update `employee` 
set `first_name` = :first_namein, `last_name` = :last_namein, `type` = :typein, 'pay_rate' = :pay_ratein, 'SSN' = :SSNin, 'email' = :emailin, 'phone' = :phonein, 'hours_worked' = :hours_workedin, 'hiring_date' = :hiring_datein
where 'id' = :idin;

--Show Employee Tables
select * from `employee`;
select * from `employee_animal`; 
select * from `employee_location`;

---------------------------------------
--Foster Parent
--Add Foster Parent 
insert into `foster_parent` (`first_name`, `last_name`, `location_id`, `address`, `city`, `zip_code`, `state`)
values (:first_namein, :last_namein, :location_id, :addressin, :cityin, :zip_codein, :statein);

--Show Foster Parent Table
select * from `foster_parent`;