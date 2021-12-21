-- sqlite

DROP table if exists boxes;
DROP table if exists items;

CREATE TABLE IF NOT EXISTS boxes (
id integer PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
size TEXT NOT NULL,
essential boolean DEFAULT FALSE,
warm boolean DEFAULT FALSE,
liquid boolean DEFAULT FALSE);

CREATE TABLE IF NOT EXISTS items (
id integer PRIMARY KEY,
box_id integer NOT NULL,
name TEXT,
essential boolean DEFAULT FALSE,
warm boolean DEFAULT FALSE,
liquid boolean DEFAULT FALSE,
FOREIGN KEY (box_id) REFERENCES boxes(id));

