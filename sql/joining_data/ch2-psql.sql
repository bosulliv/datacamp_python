-- currencies city table
drop table IF EXISTS currencies;
create table currencies(
    "curr_id" int primary key,
    "code" text,
    "basic_unit" text,
    "curr_code" text,
    "frac_unit" text,
    "frac_perbasic" int
);

-- import data
\copy currencies from 'currencies.csv' DELIMITER ',' CSV HEADER;


-- create table economies2010
drop table IF EXISTS economies2010;
create table economies2010(
    "code" text primary key,
    "year" int,
    "income_group" text,
    "gross_savings" float
);

-- import economies
\copy economies2010 from 'economies2010.csv' DELIMITER ',' CSV HEADER;

-- create table economies2015
drop table IF EXISTS economies2015;
create table economies2015(
    "code" text primary key,
    "year" int,
    "income_group" text,
    "gross_savings" float
);

-- import economies
\copy economies2015 from 'economies2015.csv' DELIMITER ',' CSV HEADER;

