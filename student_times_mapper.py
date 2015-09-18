#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if not line: continue
	if len(line) !=19: continue 
	post_id, title, tagnames, author_id, body, node_type, parent_id = line[0:7]	
	abs_parent_id, added_at,score, state_string, last_edited_id = line[7:12]	
	if len(added_at)>=13: #check if date has correct length
		hour = int(added_at[11:13]) #extract hour
		writer.writerow((author_id,hour))

