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

CREATE TABLE skillsdetail
	(
		skillid int,
		skill_name varchar(50) NOT NULL,
		skill_metric varchar(30),
		skill_verb varchar(30),
		picture varchar(255),
		description varchar(255),
		CONSTRAINT skill_pk PRIMARY KEY (skillid)
	);


-- "http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg"
-- DO THINGS HERE

-- Inserts for skills detail
INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, description)
VALUES ('1', 'Fishing', 'fish', 'catch', '', 'Fishing is the activity of using a rod and bait to catch aquatic life');
INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, description)
VALUES ('2', 'Hot Dog Eating', 'hot dogs in an hour', 'eat', '', 'Hot Dog Eating is a competitive sport in which people try to consume as many hot dogs as possible');
INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, description)
VALUES ('3', 'IQ', 'IQ', 'perform tests for a', '', 'Intelligence Quotient (IQ) is a standard measure of intellect');
INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, description)
VALUES ('4', 'Bench Press', 'bench', 'lbs for 3 reps', 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg', 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.');
INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, description)
VALUES ('5', 'Run a Mile', 'run a', 'minute mile', 'http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg', 'Running is the activity of moving fast on foot, especially as a sport. The 1-mile run is a common measurement of aerobic fitness.');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
-- Inserts for skillinfo
VALUES ('1', 'Fishing', 'Fish',  'Fish Weight', 'pounds', '5', '10', '15', '20', '25');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('2', 'Hot Dog Eating', 'Eat', 'Hot Dogs in 1 Minute', 'Hot Dogs', '1', '3', '6', '9', '12');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('3', 'IQ', 'Think as good as', 'IQ Points', 'Points', '85', '115', '130', '145', '159');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('4', 'Bench Press', 'Press', 'Bench Weight', 'Pounds', '70', '110', '170', '220', '250');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5)
VALUES ('5', 'Run a Mile', 'Run a mile in', 'Minutes', 'Minutes', '12','10','8','6','5');
