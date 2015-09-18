#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if not line: continue
	if len(line) !=19: continue 
	post_id, title, tagnames, author_id, body, node_type, parent_id = line[0:7]	
	abs_parent_id, added_at,score, state_string, last_edited_id = line[7:12]
	if node_type == "question":	
		if post_id and author_id:
			writer.writerow((post_id,author_id))
	if node_type == "answer" or node_type == "comment":
		#use the abs_parent to track what was the original question
		if author_id and abs_parent_id:
			writer.writerow((abs_parent_id,author_id))
