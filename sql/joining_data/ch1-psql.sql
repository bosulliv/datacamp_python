-- create city table
drop table IF EXISTS cities;
create table cities(
    "name" text primary key,
    "country_code" text,
    "city_proper_pop" float,
    "metroarea_pop" float,
    "urbanarea_pop" float
);

-- import data
\copy cities from 'cities.csv' DELIMITER ',' CSV HEADER;


-- create countries table
drop table IF EXISTS countries;
create table countries(
    "code" text primary key,
    "name" text,
    "continent" text,
    "region" text,
    "surface_area" float,
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
    "surface_area" float,
    "geosize_group" text
);

-- import data
\copy countries from 'countries.csv' DELIMITER ',' CSV HEADER;


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
\copy economies from 'economies.csv' DELIMITER ',' CSV HEADER;


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
    "popsize_group" text
);

-- import populations
\copy populations from 'populations.csv' DELIMITER ',' CSV HEADER;


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
\copy languages from 'languages.csv' DELIMITER ',' CSV HEADER;
