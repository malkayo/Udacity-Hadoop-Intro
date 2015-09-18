#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if not line: continue
	if len(line) !=19: continue #should be of length==19	
	post_id, title, tagnames, author_id, body, node_type, parent_id = line[0:7]	
	abs_parent_id, added_at,score, state_string, last_edited_id = line[7:12]
	
	if node_type == "question": 
		#return the question id, "question" and post length
		writer.writerow((post_id,node_type,len(body)))
	elif node_type == "answer":
		#return the relaetd question id, "answer" and post length
		writer.writerow((parent_id,node_type,len(body)))
	

	
