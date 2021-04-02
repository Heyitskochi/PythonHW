import os
import csv

poll_csv = os.path.join( "Resources", "PyPoll_Resources_election_data.csv")

with open(poll_csv) as csvfile:
	canidate = dict()
	totalvotes=0
	#caclulates number of votes
	csvreader = csv.reader(csvfile, delimiter= ",")
	next(csvreader, None)
	for line in csvreader:
		#uses dictionary to store the voters with the canidate name as the key
		canidatename = (line[2])
		voterid = (line[0])
		if canidatename not in canidate:
			#checks if caniate is new
			canidate[canidatename] = voterid
		elif (type(canidate[canidatename])) == list:
			#prevents recursion of keys
			canidate[canidatename].append(voterid)
		else:
			canidate[canidatename] = [canidate[canidatename], voterid]
		totalvotes += 1

canidatelist = list(canidate.keys())


maxvotes = 0
maxcanidate = ""

analysispath = os.path.join( "Analysis", "PyPollAnalysis.txt")
PyPollAnalysis = open(analysispath, "w")

############# Printing Answers #############

print(f"Election Results \n------------------------ \nTotal Votes: {totalvotes}\n")
PyPollAnalysis.write(f"Election Results \n------------------------ \nTotal Votes: {totalvotes}\n")

for x in range(len(canidatelist)):
	#prints out all the canidates
	numberofvotes = len(canidate[canidatelist[x]])
	percentvote = "{0:.3%}".format(round((numberofvotes / totalvotes), 3))
	canidatenamefinal = (str([canidatelist[x]])).strip("[]")

	print (f"{canidatenamefinal}: {percentvote}% ({numberofvotes})")
	PyPollAnalysis.write(f"{canidatenamefinal}: {percentvote}% ({numberofvotes})\n")

	if (numberofvotes > maxvotes):
		#calculates who won
		maxvotes = numberofvotes
		maxcanidate = canidatenamefinal
	else:
		continue
print(f"------------------------- \n Winner: {maxcanidate} \n-------------------------")
PyPollAnalysis.write(f"------------------------- \n Winner: {maxcanidate} \n-------------------------\n")
PyPollAnalysis.close()