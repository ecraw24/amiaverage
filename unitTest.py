### unit tests ###
import sqlite3
import unittest
import os



class Testing(unittest.TestCase):
    
    def test_input(self):
        
        # test if string length of int > 5 raises an error
        assertFalse(verifyInput(1234567890))
        
        # test if input throws error if string
        assertFalse(verifyInput("hippo123"))
        
        # test if input throws error if list
        assertFalse(verifyInput([1, 2, 3]))

class HomePageTesting(unittest.TestCase):
#Testing subclass specific to the homepage and its related functions

	#connects to the database
	def setup(self):
		self.dbname = "AmIAverage"
		self.db = sqlite3.connect(self.dbname)
		self.c = self.db.cursor()

	#since home page will not be altering database, no need to commit any changes to it
	def teardown(self):
		self.db.close()

	#unit test to test the get_categories() function
	def test_get_categories(self):

		#unsure if there is a better way to test, since this is the same query from the function
		cats = self.c.execute("SELECT name FROM Categories;")
		i = 0

		for name in get_categories(self.dbname):
			assertEqual(name, cats[i][0], "Error:\nExpected: {}\nActual: {}".format(cats[i][0], name))

class ResultsPage(unittest.TestCase):
#Testing subclass specific to the presentation of results. Page only reads from DB and calulates results dynamically, as commits to DBwould require updating percentiles for the whole category upon eachinsert..

        #connects to the database
        def setup(self):
            self.dbname = "AmIAverage"
            self.db = sqlite3.connect(self.dbname)
            self.c = self.db.cursor()

        #no need to commit any changes to it
        def teardown(self):
            self.db.close()

        #unit test for test_calc_percentile() function, uses native SQL
        def test_calc_percentile(self, testfile):
            cats = get_categories(testfile)
            for data in cats:
                assertEqual(self.c.execute("SELECT (category), PERECENT_RANK() OVER (ORDER BY (category)) AS Percent_Rank FROM Categories"), data[3])


        #unit test for interpretation of interpret_percentile() function, which outputs a normalized percentile
        def test_interpret_percentile(self):
            self.assertEqual("EXACTLY", interpret_percentile(49))
            self.assertEqual("EXACTLY", interpret_percentile(50))
            self.assertEqual("EXACTLLY", interpret_percentile(51))

            self.assertEqual("ALMOST", interpret_percentile(52))
            self.asssertEqual("ALMOST", interpret_percenile(55))
            self.assertEqual("ALMOST", interpret_percentile(48))
            self.assertEqual("ALMOST", interpret_percentile(45))

            self.assertEqual("SORT OF", interpret_percentile(44))
            self.assertEqual("SORT OF", interpret_percentile(34))
            self.assertEqual("SORT OF", interpret_percentile(56))
            self.assertEqual("SORT OF", interpret_percentile(66))

            self.assertEqual("NOT REALLY", interpret_percentile(33)
            self.assertEqual("NOT REALLY", interpret_percentile(3))
            self.assertEqual("NOT REALLY", interpret_percentile(67)
            self.assertEqual("NOT REALLY", interpret_percentile(97)

            self.assertEqual("ABSOLUTELY NOT", interpret_percentile(2))
            self.assertEqual("ABSOLUTELY NOT", interpret_percentile(0))
            self.assertEqual("ABSOLUTELY NOT", interpret_percentile(98))
            self.assertEqual("ABSOLUTELY NOT", interpret_percentile(100))
			
			
class MySkillsPage(unittest.TestCase):
	@classmethod
	def setupclass(cls):
		print("setup MySkillsPage Test Class")

	def setUp(self):
		print("setup MySkillsPage Test")


	def testSkillListPopulate (self):
		self.dbname = "AmIAverageTest"
		self.db = sqlite3.connect(self.dbname)
		self.c = self.db.cursor()
		print("Testing Skill List Populate")
		skill_list = []
		for row in self.c.execute("SELECT skillname FROM skills CASE WHEN score IS NOT NULL")
			skill_list.append(row[0])

		self.assertEqual(skill_list[0],  'Skill1name', "Test Failed Skill 1 name not populated")
		self.assertEqual(skill_list[1],  'Skill2name', "Test Failed Skill 2 name not populated")
		self.assertEqual(skill_list[2],  'Skill3name', "Test Failed Skill 3 name not populated")
		self.assertEqual(skill_list[3],  'Skill4name', "Test Failed Skill 4 name not populated")
		self.assertEqual(skill_list[4],  'Skill5name', "Test Failed Skill 5 name not populated")
		skill_count = self.c.execute("SELECT count(CASE WHEN score IS NOT NULL")
		self.assertEqual(len(skill_list), skill_count, "Test Failed Not all Skills correctly populated")

	def testDisplayList(self):
		print("Testing Display List")
		self.dbname = "AmIAverageTest"
		self.db = sqlite3.connect(self.dbname)
		self.c = self.db.cursor()
		skill_list = []
		for row in self.c.execute("SELECT skillname FROM skills"):
			skill_list.append(row[0])
		display_list = [0]*4
		curr_skill = 0
		display_list.filldisplay(skill_list, curr_skill, display_list)
		self.assertEqual(skill_list[0:4], display_list , "Initial Display list incorrectly populated")
		display_list.filldisplay(skill_list, curr_skill, display_list)
		self.assertEqual(skill_list[4:8], display_list, "Display list incorrectly refilled")
		display_list.filldisplay(skill_list, curr_skill, display_list)
		self.assertEqual(skill_list[8:11], display_list[0:3], "Display list incorrectly refilled #2")
