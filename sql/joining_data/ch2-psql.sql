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

