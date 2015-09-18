#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

old_user=None
counts=[0]*24 #list of the count for each hour

for line in reader:
	if len(line)!=2:
		continue
	this_user, this_hour = line
	if not this_hour: continue
	hour = int(this_hour)
	
	#when the key changes
	if old_user and old_user != this_user:
		max_count = max(counts)
		for i in range(24):
			if counts[i] == max_count:	
				print "{0}\t{1}".format(old_user,i)
		old_user=this_user
		counts=[0]*24	

	#when the key does not change	
	old_user=this_user
	counts[hour] = counts[hour] + 1 #update the count for the hour
 
if old_user:
		max_count = max(counts)
		#print max_count
		for i in range(24):
			if counts[i] == max_count:	
				print "{0}\t{1}".format(this_user,i)
	
