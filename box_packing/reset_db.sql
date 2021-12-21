-- sqlite

DROP table if exists boxes;
DROP table if exists items;

CREATE TABLE IF NOT EXISTS boxes (
id integer PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
size TEXT NOT NULL,
liquid boolean DEFAULT FALSE,
warm boolean DEFAULT FALSE,
essential boolean DEFAULT FALSE);

CREATE TABLE IF NOT EXISTS items (
id integer PRIMARY KEY,
box_id integer NOT NULL,
name TEXT,
warm boolean DEFAULT FALSE,
FOREIGN KEY (box_id) REFERENCES boxes(id));

insert into boxes (name, size, liquid, warm, essential)
values 
('Computers', 'medium', False, True, False),
('Monitors and Clock', 'xlarge', False, True, False);

