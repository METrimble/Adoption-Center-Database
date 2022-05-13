--Dump for Adoption Center Database 
--Create for Employee
drop table if exists `employee`
create table `employee`(
    `id` int(11) auto_increment,
    `first_name` varchar(255) not null,
    `last_name` varchar(255) not null, 
    `type` enum('volunteer', 'part-time', 'full-time', 'salaried') not null
    `pay_rate` int(11),
    `SSN` int(9),
    `email` varchar(254),
    `phone` int(15) not null,
    `hours_worked` int(11) not null default 0,
    `hiring_date` date not null, 
    primary key (`id`), 
    unique key full_name (`first_name`, `last_name`)
);

--Create for Employee Animal
drop table if exists `employee_animl`
create table `employee_animal`(
    `employee_id` int(11),
    `animal_id` int(11),
    primary key (`employee_id`, `animal_id`),
    foreign key (`employee_id`) references `employee` (`id`),
    foreign key (`animal_id`) references `animal` (`id`)
);

--Create for Employee Location


--Create for Animal


--Create for Location


--Create for Foster Parent 
drop table if exists `foster_parent`
create table `foster_parent`(
    `id` int(11) auto_increment,
    `first_name` varchar(255) not null, 
    `last_name` varchar(255) not null,
    `location_id` int(11) not null, 
    `address` varchar(35) not null,
    `city` varchar(28) not null,
    `zip_code` varchar(10) not null, 
    `state` varchar(2) not null,
    primary key (`id`),
    foreign key (`location_id`) references `location` (`id`),
    unique key full_name (`first_name`, `last_name`)
);
