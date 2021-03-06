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
--		skill_name varchar(50) NOT NULL,
--		skill_verb varchar(30),
--		skill_metric varchar(30),
--		unit_of_measurement varchar(30),
--		descrip varchar(255)
--	);



-- "http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg"
-- DO THINGS HERE

-- for skillsinfo
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('1', 'Fishing', 'catch',  'fish', 'pounds', 'https://www.takemefishing.org/getmedia/02981128-b7e1-4ea0-adbd-75bc5b2c7ba0/homehero_woman.jpg', 'Fishing is the activity of using a rod and bait to catch aquatic life.', '5', '10', '15', '20', '25');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('2', 'Hot Dog Eating', 'eat', 'hot dogs in an hour', 'Hot Dogs', 'https://www.denverpost.com/wp-content/uploads/2018/07/14a8dd5c2499465e933a5bb07c1c2704.jpg', 'Hot Dog Eating is a competitive sport in which people try to consume as many hot dogs as possible.', '1', '3', '6', '9', '12');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('3', 'IQ', 'perform tests for a', 'IQ', 'Points', 'https://caltech-prod.s3.amazonaws.com/main/images/CT_Quartz-IQ_SPOTLIGHT.original.jpg', 'Intelligence Quotient (IQ) is a standard measure of intellect.', '85', '115', '130', '145', '159');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('4', 'Bench Press', 'bench', 'lbs for 3 reps', 'Pounds', 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg', 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.', '70', '110', '170', '220', '250');
INSERT INTO skillsinfo (id, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5)
VALUES ('5', 'Weekly Miles', 'run', 'Weekly Miles', 'Miles', 'http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg', 'Running is the activity of moving fast on foot, especially as a sport. Running throughout the week is an important part of aerobic fitness.', '2','5','10','20','26');
