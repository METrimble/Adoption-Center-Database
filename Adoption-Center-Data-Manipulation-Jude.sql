--Data Manipulation for Adoption Center
--Animal
--Add Animal
insert into `animal` (`location_id`, `foster_parent_id`, `animal_name`, `animal_species`, `animal_breed`, `animal_weight`, `birthdate`, `spayed/neutered`, `description`)
values (:location_id, :foster_parent_id, :animal_namein, :animal_speciesin, :animal_breedin, :animal_weightin, :birthdatein, :spayed/neuteredin, :descriptionin);

--Delete Animal
delete * from `animal` where 'id' = :animal_idin;

--View bt name
select * from `animal` where 'animal_name' = :animal_namein;

--Filter by Species
select * from `animal` where 'animal_species' = :animal_speciesin;

--Show Animal Table
select * from `animal`

---------------------------------------
--Location
--Add Location
insert into `location` (`address`, `city`, `zip_code`, `state`, `sq_ft`, `animal_in_rate`)
values (:addressin, :city_in, :zip_codein, :statein, :sq_ftin, :animal_in_ratein);


--Show Location Table
select * from `location`;

---------------------------------------