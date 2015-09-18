#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')
id_list=[]
old_post = None


for line in reader:
	if len(line)!=2:
		continue
	this_post,this_id= line
	if not this_post or not this_id: continue
	this_id = int(this_id)
	#when the key changes	
	if old_post and old_post != this_post:
		writer.writerow((old_post,id_list))		
		id_list=[]
		old_post=this_post
	#when the key does not change
	id_list.append(this_id)	#add the user_id of the post 
	old_post=this_post
#Last post
if old_post:
	writer.writerow((old_post,id_list))


