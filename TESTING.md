# Project Title: Am I Average?

## Team Members: Emma Crawford, Michael Kim, Jeffrey Mason, Kevin Vick

############# 
Author: Michael Kim

Use case name: 

	Verify output is correct

Description: 

	Test the function (currently called get_categories()) that should return a list of all categories in
	the database

Pre-conditions: 

	None

Test Steps

	1. Run the get_categories() function, passing the name of the database as string

Expected Result

	Function returns a list with the names of all the available categories

Actual Result

	N/A due to no available database as of yet

Status (Pass/Fail)

	Fail

Notes

	Currently no database to test the function on

Post-conditions

	N/A

#############


#############
Author: Emma Crawford

Use case name

	Verify input is the correct format

Description

	Input should be a number (int, float, long)

Pre-conditions

	None, potentially user knowing the correct format

Test Steps

	1. Navigate to the "Enter results" page
	2. Enter a number into the input field
	3. Click "Am I Average?" button	

Expected Result

	If the input is a number, the page should perform calculations and navigate the user to the results page. 

Actual Result

	...

Status (Pass/Fail)

	Fail

Notes

	Expected fail as of (3/1/22) due to no current data within database to compare to.

Post-conditions

	n/a

#############

############# 
Author: Kevin Vick

Use case name:

	Verify percentile calculations and context tools

Description:

	Test SQL query for returning output and assess whether the results is binned into
	the appropriate category of summary prose.

Pre-conditions:

	DB is properly populated.

Test Steps

	1. Accept input from previous page 
	2. Connect to the DB
	3. Query DB for statistical context of input
	4. Compare own relative score to query result

Expected Result

	Percentile output should map to a qualitative interpretation and visualization

Actual Result

	Pending workflow

Status (Pass/Fail)

	Fail

Notes

	Will reset prose category assertions from edge cases to ranges for better 
	test coverage. 

Post-conditions

	User is presented with a simple prose summary of relative performance and a 
	dynamic graph of standing based on a normal distribution.

#############

#############
Author: Jeffrey Mason

Use case name

	Verify that display list is being correctly populated and updated

Description

	Display list should correctly fill with entries from the skill_list
    When we have displayed all entries we cycle to the beginning

Pre-conditions

	skill_list needs to be correctly filled with information
    

Test Steps

	1. Declare a blank display list
    2. Fill the display list with information
    3. Test the result is correctly populated
    4. Refresh the display list with more information
    5. Test the result is correctly refreshed
    6. Refresh the display list and exhaust it
    7. Test we go back to the start of the elist

Expected Result

    Display list should fill correctly with information

Actual Result

	... Not yet observed

Status (Pass/Fail)

	Fail

Notes

	Failure was expected no test database function isnt finished

Post-conditions

	n/a

#############
