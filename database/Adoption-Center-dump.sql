--Dump for Adoption Center Database 
--Create for Employee
drop table if exists `employee`;
create table `employee`(
    `id` int(11) auto_increment,
    `first_name` varchar(255) not null,
    `last_name` varchar(255) not null, 
    `type` enum('Volunteer', 'Part-time', 'Full-Time', 'Salaried') not null,
    `pay_rate` int(11), not null default 0,
    `SSN` int(9),
    `email` varchar(254),
    `phone` int(15) not null,
    `hours_worked` int(11) not null default 0,
    `hiring_date` date not null, 
    primary key (`id`), 
    unique key `full_name` (`first_name`, `last_name`)
);

--Create for Location
drop table if exists `location`;
create table `location`(
    `id` int(11) not null auto_increment,
    `address` varchar(35) not null,
    `city` varchar(28) not null,
    `zip_code` varchar(10) not null,
    `state` varchar(2) not null,
    `sq_ft` int(11) not null,
    `animal_in_rate` int(11) default 0,
    PRIMARY KEY (`id`),
    unique key `full_address` (`address`, `city`, `zip_code`)
);

--Create for Foster Parent 
drop table if exists `foster_parent`;
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
    unique key `full_name` (`first_name`, `last_name`)
);

--Create for Animal
drop table if exists `animal`;
create table `animal` (
    `id` int(11) auto_increment,
    `location_id` int(11) not null,
    `foster_parent_id` int(11), 
    `animal_name`varchar(50),
    `animal_species`enum('dog', 'cat', 'other') not null,
    `animal_sex`enum('male', 'female', 'other') not null,
    `animal_breed` varchar(45),
    `animal_weight` decimal(6,4) not null,
    `birthdate` date,
    `spayed/neutered` tinyint not null default 0,
    `description` varchar(1000),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`location_id`) REFERENCES `location` (`id`),
    FOREIGN KEY (`foster_parent_id`) REFERENCES `foster_parent` (`id`),
    unique key `name_birthdate` (`animal_name`, `birthdate`)
);

--Create for Employee Animal
drop table if exists `employee_animal`;
create table `employee_animal`(
    `employee_id` int(11),
    `animal_id` int(11),
    primary key (`employee_id`, `animal_id`),
    foreign key (`employee_id`) references `employee` (`id`),
    foreign key (`animal_id`) references `animal` (`id`)
);

--Create for Employee Location
drop table if exists `employee_location`;
create table `employee_location` (
    `employee_id` int(11),
    `location_id` int(11),
    primary key (`employee_id`, `location_id`),
    foreign key (`employee_id`) references `employee` (`id`),
    foreign key (`location_id`) references `location` (`id`)
);

--Sample Data for Employee
insert into `employee` 
(`first_name`, `last_name`, `type`, `pay_rate`, `SSN`, `email`, `phone`, `hours_worked`, `hiring_date`) 
values ('George', 'Bart', 'Volunteer', '0', '563889670', 'georgeb@gmail.com', '5097869123', '40', '2020-12-04');

--Sample Data for Location
insert into `location` 
(`address`, `city`, `zip_code`, `state`, `sq_ft`, `animal_in_rate`)
values ('6785 SE Valley st', 'Portville', '87666', 'OR', '1500', '132');

--Sample Data for Foster Parent 
insert into `foster_parent`
(`first_name`, `last_name`, `location_id`, `address`, `city`, `zip_code`, `state`)
values ('Barbra', 'Stevens', 1, '2435 NE Treetop Lane', 'Eugene', '97450', 'OR');

--Sample Data for animal
insert into `animal`
(`location_id`, `foster_parent_id`, `animal_name`, `animal_species`, `animal_sex`, `animal_breed`, `animal_weight`, `birthdate`, `spayed/neutered`, `description`)
values (1, 1, 'Spoon', 'cat', 'male', 'Tabby', '10', '2020-04-15', '1', 'sweet boy');

--Sample Data for employee-animal
insert into `employee_animal`
(`employee_id`, `animal_id`)
values ((select `id` from `employee` where `first_name` = 'George' and `last_name` = 'Bart'), 1);

--Sample Data for employee_location
insert into `employee_location`
(`employee_id`, `location_id`)
values ((select `id` from `employee` where `first_name` = 'George' and `last_name` = 'Bart'), 1);


