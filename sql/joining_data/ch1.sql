-- create city table
drop table IF EXISTS cities;
create table cities(
    "name" text primary key,
    "country_code" text,
    "city_proper_pop" int,
    "metroarea_pop" int,
    "urbanarea_pop" int
);

-- import data
.mode csv
.import cities.csv cities
delete from cities where name = 'name';

-- create countries table
drop table IF EXISTS countries;
create table countries(
    "code" text primary key,
    "name" text,
    "continent" text,
    "region" text,
    "surface_area" int,
    "indep_year" int,
    "local_name" text,
    "gov_form" text,
    "capital" text,
    "cap_long" float,
    "cap_lat" float
);

-- create countries_plus table
drop table IF EXISTS countries_plus;
create table countries_plus(
    "name" text,
    "continent" text,
    "code" text primary key,
    "surface_area" int,
    "geosize_group" text
);

-- import countries
.mode csv
.import countries.csv countries
delete from countries where code = 'code';


-- create table economies
drop table IF EXISTS economies;
create table economies(
    "econ_id" int primary key,
    "code" text,
    "year" int,
    "income_group" text,
    "gdp_percapita" float,
    "gross_savings" float,
    "inflation_rate" float,
    "total_investment" float,
    "unemployment_rate" float,
    "exports" float,
    "imports" float
);

-- import economies
.mode csv
.import economies.csv economies

-- delete header row
delete from economies where econ_id = 'econ_id';


-- create table populations
drop table IF EXISTS populations;
create table populations(
    "pop_id" int primary key,
    "country_code" text,
    "year" int,
    "fertility_rate" float,
    "life_expectancy" float,
    "size" int
);

drop table IF EXISTS pop_plus;
create table pop_plus(
    "country_code" text primary key,
    "size" int,
    'popsize_group' text
);

-- import populations
.mode csv
.import populations.csv populations

-- delete header row
delete from populations where pop_id = 'pop_id';


-- create table languages
drop table IF EXISTS languages;
create table languages(
    "lang_id" int primary key,
    "code" text,
    "name" text,
    "percent" float,
    "official" bool
);

-- import languages
.mode csv
.import languages.csv languages

-- delete header row
delete from languages where lang_id = 'lang_id';

