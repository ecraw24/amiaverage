DROP TABLE skillsinfo;
--DROP TABLE suggestions;



CREATE TABLE skillsinfo
	(
		id int,
		skill_name varchar(50) NOT NULL,
		skill_verb varchar(30),
		skill_metric varchar(30),
		unit_of_measurement varchar(30),
		picture varchar(255),
		descrip varchar(255),
		level1 numeric,
		level2 numeric,
		level3 numeric,
		level4 numeric,
		level5 numeric,
		CONSTRAINT skill_pk PRIMARY KEY (id)
	);

--CREATE TABLE suggestions
--	(
--		requestid int,
--		skill_name varchar(50) NOT NULL,
--		skill_verb varchar(30),
--		skill_metric varchar(30),
--		unit_of_measurement varchar(30),
--		descrip varchar(255),
--		CONSTRAINT request_id PRIMARY KEY (requestid)
--	);



-- "http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg"
-- DO THINGS HERE

-- Inserts for skills detail
--INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, descrip)
--VALUES ('1', 'Fishing', 'fish', 'catch', '', 'Fishing is the activity of using a rod and bait to catch aquatic life');
--INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, descrip)
--VALUES ('2', 'Hot Dog Eating', 'hot dogs in an hour', 'eat', '', 'Hot Dog Eating is a competitive sport in which people try to consume as many hot dogs as possible');
--INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, descrip)
--VALUES ('3', 'IQ', 'IQ', 'perform tests for a', '', 'Intelligence Quotient (IQ) is a standard measure of intellect');
--INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, descrip)
--VALUES ('4', 'Bench Press', 'bench', 'lbs for 3 reps', 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg', 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.');
--INSERT INTO skillsdetail (skillid, skill_name, skill_metric, skill_verb, picture, descrip)
--VALUES ('5', 'Run a Mile', 'run a', 'minute mile', 'http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg', 'Running is the activity of moving fast on foot, especially as a sport. The 1-mile run is a common measurement of aerobic fitness.');
-- inserts for skillsinfo
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('1', 'Fishing', 'catch',  'fish', 'pounds', '', 'Fishing is the activity of using a rod and bait to catch aquatic life.', '5', '10', '15', '20', '25');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('2', 'Hot Dog Eating', 'eat', 'hot dogs in an hour', 'Hot Dogs', '', 'Hot Dog Eating is a competitive sport in which people try to consume as many hot dogs as possible.', '1', '3', '6', '9', '12');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('3', 'IQ', 'perform tests for a', 'IQ', 'Points', '', 'Intelligence Quotient (IQ) is a standard measure of intellect.', '85', '115', '130', '145', '159');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('4', 'Bench Press', 'bench', 'lbs for 3 reps', 'Pounds', 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg', 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.', '70', '110', '170', '220', '250');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('5', 'Run a Mile', 'run a', 'minute mile', 'Minutes', 'http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg', 'Running is the activity of moving fast on foot, especially as a sport. The 1-mile run is a common measurement of aerobic fitness.', '12','10','8','6','5');
