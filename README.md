# PythonHW



## PyBank

### Total Number of Months

* I used the length of "allmonths" to calculate the number of months

###  Net Total Amount of "Profit/Losses" 

* I declared a variable called totalamount and added the amount of the current month to it 

* I used a for loop to go through all the months

### Average in Changes

* I declared a variable called "changeamounts" which will hold the sum of the changes

* Inside the for loop, I declared two variables, "currentmonth" and "nextmonth"

* To find the change I subtracted the "nextmonth[1]" by  "currentmonth[1]" then added that amount to "changeamounts"

* I then divided "changeamounts" by "numberofmonths" -1 to calculate the average
* To handle the index error for the final element in the list I used an "Except IndexError"

### Greatest Increase & Greatest Decrease

* Declared 4 empty variables to hold the amount and month for the greatest increase and decrease

* Inside the for loop I compared the change varaible with the variables that held the greatest increase and decrease amounts

* If the current month's change was greater or smaller than these values I replaced them with the nextmonth's change and month name



## PyPoll

### Total Number of Votes Cast

### List of Canidates

### Percentage of Votes

### Total Number of Votes Each Canidate Won

### Winner by Popular Vote



## Other

### Printing

### Exporting File





