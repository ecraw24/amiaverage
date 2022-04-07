CREATE TABLE skillsinfo
	(
		id int,
		skill_name varchar(50) NOT NULL,
		skill_verb varchar(30),
		skill_metric varchar(30),
		unit_of_measurement varchar(30),
		level1 numeric,
		level2 numeric,
		level3 numeric,
		level4 numeric,
		level5 numeric,
		CONSTRAINT skill_pk PRIMARY KEY (id)
	);
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('1', 'Fishing', 'Fish',  'Fish Weight', 'pounds', '5', '10', '15', '20', '25');

