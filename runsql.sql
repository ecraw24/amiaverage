DROP TABLE skillsinfo;



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



-- DO THINGS HERE
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('1', 'Fishing', 'Fish',  'Fish Weight', 'pounds', '5', '10', '15', '20', '25');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('2', 'Hot Dog Eating', 'Eat', 'Hot Dogs in 1 Minute', 'Hot Dogs', '1', '3', '6', '9', '12');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('3', 'IQ', 'Think as good as', 'IQ Points', 'Points', '85', '115', '130', '145', '159');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('4', 'Bench Press', 'Press', 'Bench Weight', 'Pounds', '70', '110', '170', '220', '250');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('5', 'Run a Mile', 'Run a mile in', 'Minutes', 'Minutes', '12','10','8','6','5');
