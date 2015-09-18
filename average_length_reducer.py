#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

old_post=None
question_length=0
answer_number=0
length_sum=0

for line in reader:
	if len(line)!=3:continue
	this_post, this_type, this_length = line
	if not this_type or not this_length: continue

	#when the key changes
	if old_post and old_post != this_post:
		if answer_number ==0:
			print "{0}\t{1}\t{2}".format(old_post,question_length,"0")
		else:		
			avgLength = length_sum/answer_number
			print "{0}\t{1}\t{2}".format(old_post, question_length,avgLength)	
		question_length=0
		answer_number=0
		length_sum=0
		old_post=this_post
	
	#when the key does not change	
	if this_type == "question":
		#save the question length
		question_length=this_length
	elif this_type == "answer":
		#updated the answer count and sum of answer length 
		answer_number += 1
		length_sum += float(this_length) 
	old_post=this_post
#Last Post
if old_post:
	if answer_number ==0:
		print "{0}\t{1}\t{2}".format(old_post,question_length,"0")
	else:		
		avgLength = length_sum/answer_number
		print "{0}\t{1}\t{2}".format(old_post, question_length,avgLength)	
	
