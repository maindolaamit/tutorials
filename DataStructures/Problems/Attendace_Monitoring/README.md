# Problem Statement
In an attendance monitoring system, the unique integer ID number of every employee is noted
whenever the employee swipes his card in the office. First time an employee enters into the office,
the attendance counter is set to 1. From then onwards, each time an employee leaves the office
premises for tea break or lunch break the counter is incremented, and incremented again when he
enters back. If the counter is odd on a day, it means the employee is in the office premises and if
the counter is even, it means he is out of the premises.
The organization uses this data to perform the following analytics:
1. How many employees came today?
2. Did a particular employee come today?
3. How often did an employee enter into the office?
4. Which employee moves out of office the greatest number of times?
5. Which employee ids within a range of IDs attended office, the attendance counter for them, and
whether they are inside or outside office?
Asks:
1. Implement the above problem statement in Python using BINARY TREE ADT.
2. Perform an analysis for the questions above and give the running time in terms of input
size: n.
The basic structure of the employee node will be:

## Asks:
1. Implement the above problem statement in Python using BINARY TREE ADT.
2. Perform an analysis for the questions above and give the running time in terms of input
size: n.

## Operations:
**1. def _readEmployeesRec(self, eNode, Eid):** This function reads from the inputPS1.txt file the
ids of employees entering and leaving the organization premises. One employee id should be
populated per line (in the input text file) indicating their swipe (entry or exit). The input data is
used to populate the tree. If the employee id is already added to the tree, then the attendance
counter is incremented for every subsequent occurrence of that employee id in the input file. Use
a trigger function to call this recursive function from the root node.
**2. Def _getHeadcountRec(self, eNode):** This function counts the number of unique IDs stored in
the tree and prints the employee headcount for the day into the output.txt file as shown below.
Total number of employees today: xx
Use a trigger function to call this recursive function from the root node.
**3. def _searchIDRec(self, eNode, eId):** This function searches whether a particular employee has
attended today or not. The function reads the search id from the file promptsPS1.txt where the
search id is mentioned with the tag as shown below.
searchID:23
searchID:22
searchID:11
The search function is called for every searchID tag the program finds in the promptsPS1.txt file.
If the employee id is found it outputs the below string into the outputPS1.txt file
Employee id xx is present today.
If the employee id is not found it outputs the below string into the outputPS1.txt file
Employee id xx is absent today.
Use a trigger function to call this recursive function from the root node.
**4. def _howOften_Rec(self, eNode, EId):** This function counts the number of times a particular
employee swiped today and if the employee is currently in the office or outside.
The function reads the id from the file promptsPS1.txt where the search id is mentioned with
the tag as shown below.
howOften:12
howOften:22
howOften:11
The search function is called for every howOften tag the program finds in the promptsPS1.txt
file.
If the employee id is found with an odd attendance count the below string is output into the
outputPS1.txt file
Employee id xx swiped yy times today and is currently in officeIf the employee id is found with an even attendance count the below string is output into the
outputPS1.txt file
Employee id xx swiped yy times today and is currently outside office
If the employee id is not found it outputs the below string into the outputPS1.txt file
Employee id xx did not swipe today.
Use a trigger function to call this recursive function from the root node.
5. def _frequentVisitorRec(self, eNode): This function searches for the employee who has
swiped the most number of times and outputs the below string into the outputPS1.txt file.
Employee id xx swiped the most number of times today with a count of yy
Use a trigger function to call this recursive function from the root node. For the sake of the
assignment, you need to display any one of the employee ids if there are more than one
employee who have entered maximum number of times. For example, if employee id 22 and 23
have both visited 3 times, the output should show either 22 or 23.
6. def printRangePresent(self, StartId, EndId): This function prints the employee ids in the range
StartId to EndId and how often they have entered the organization in a file name outputPS1.txt.
The input should be read from the promptsPS1.txt file where the range is mentioned with the
tag as shown below.
range:23:125
If Input range is given as 23 to 125 the output file should show:
Range: 23 to 125
Employee attendance:
23, 1, in
41, 3, in
121, 2, out
For this purpose, the tree needs to be inorder traversed and the id and frequency of the
employees in the range must be printed into the file. If the Id is found in the BT, its frequency
cannot be zero as the person had entered the organization at least once.
2. Sample file formats
Sample Input file
Each row will have one employee id indicating a single swipe for that employee. The input file
name must be called inputPS1.txt.
Sample inputPS1.txt
23
22
41
121
41
2241
121
Sample promptsPS1.txt
searchID:22
searchID:120
howOften:41
howOften:12
range:23:125
Sample outputPS1.txt
Total number of employees today: 4
Employee id 22 is present today.
Employee id 120 is absent today.
Employee id 41 swiped 3 times today and is currently in office
Employee id 12 did not swipe today.
Employee id 41 swiped the most number of times today with a count of 3
Range: 23 to 125
Employee attendance:
23, 1, in
41, 3, in
121, 2, out
