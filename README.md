# PythonHW



## PyBank

### Total Number of Months

* I used the length of "allmonths" to calculate the number of months

###  Net Total Amount of "Profit/Losses" 

* I declared a variable called "totalamount" and added the amount of the current month to it 

* I used a for loop to go through all the months

### Average in Changes

* I declared a variable called "changeamounts" which will hold the sum of the changes

* Inside the for loop, I declared two variables, "currentmonth and "nextmonth"

* To find the change I subtracted the "nextmonth[1]" by  "currentmonth[1]" then added that amount to "changeamounts"

* I then divided "changeamounts" by "numberofmonths" -1 to calculate the average
* To handle the index error for the final element in the list I used an "Except IndexError"

### Greatest Increase & Greatest Decrease

* Declared 4 empty variables to hold the amount and month for the greatest increase and decrease

* Inside the for loop I compared the change variable with the variables that held the greatest increase and decrease amounts

* If the current month's change was greater or smaller than these values I replaced them with the next month's change and month name



## PyPoll

### Total Number of Votes Cast

* Inside the for loop for csvreader I added one to a counter called "totalvotes"

### List of Candidates

* I stored each candidate's names as key inside a dictionary called candidate
* Inside the for loop iterating through the candidate keys I just stripped the "[]" from the key and stored it in a variable called "canidatenamefinal"

### Percentage of Votes

* Inside the for loop iterating through the candidate keys I found the number of votes each candidate got by getting the length of each element in the dictionary
* I then divided that number by the total number of votes, formatted it and stored it inside a variable named "percentvote"

### Total Number of Votes Each Candidate Won

* Inside the for loop iterating through the candidate keys I found the number of votes each candidate got by getting the length of each element in the dictionary and stored this number in a variable called "numberofvotes"

### Winner by Popular Vote

* Inside the for loop iterating through the candidate keys I found the number of votes each candidate got by getting the length of each element in the dictionary
* I compared this number of votes to a variable called "maxvotes", if the number of votes a candidate got was more than the "maxvotes" I redefined the "maxvotes" and "maxcandidate" variables







