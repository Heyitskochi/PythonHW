import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")


with open(bank_csv) as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ",")
	next(csvreader, None)
	
	greatestamount = 0
	smallestamount = 0
	greatestmonth = ""
	smallestmonth = ""
	changeamounts = 0
	totalamounts = 0 
	#Important variables

	allmonths = list(csvreader)
	#turned csvreader to a list so I can index ot
	
	for x in range(len(allmonths)):
		try:
			currentmonth = allmonths[x]
			nextmonth = allmonths[x+1]
			change = (int(nextmonth[1]) - int(currentmonth[1]))
			changeamounts = changeamounts + change
			totalamounts = int(currentmonth[1]) + totalamounts
			if change > greatestamount:
				#finds greatest change
				greatestamount = change
				greatestmonth = nextmonth[0]
			elif change < smallestamount:
				#finds smallest change
				smallestamount = change
				smallestmonth = nextmonth[0]
			else:
				continue
		except IndexError:
			#handles last iteration
			totalamounts = int(currentmonth[1]) + totalamounts
			continue


	numberofmonths = (len(allmonths))
	averagechange = changeamounts / (numberofmonths-1)
	#calculates average cahnge

	analysispath = os.path.join( "Analysis", "PyBankAnalysis.txt")
	PyBankAnalysis = open(analysispath, "w")
	print(f"Financial Analysis \n----------------------------\nTotal Months: {numberofmonths} \nTotal: ${totalamounts} \nAverage Change: ${averagechange}")
	PyBankAnalysis.write(f"Financial Analysis \n----------------------------\nTotal Months: {numberofmonths} \nTotal: ${totalamounts} \nAverage Change: ${averagechange}\n")
	print(f"Greatest Increase in Profits: {greatestmonth} {greatestamount} \nGreatest Decrease in Profits: {smallestmonth} {smallestamount}")
	PyBankAnalysis.write(f"Greatest Increase in Profits: {greatestmonth} {greatestamount} \nGreatest Decrease in Profits: {smallestmonth} {smallestamount}")

