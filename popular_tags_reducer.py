#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"',quoting=csv.QUOTE_ALL)

# the goal is to keep track of the top 10
# as we are going through the different tags (keys)
 
tag_list=[] #where the tags are stored
count_list=[] #where the related counts are stored
list_size = 0
tag_count=0
old_tag = None


for line in reader:
	if len(line)!=2:
		continue
	this_tag,uno= line
	if not this_tag: continue
	
	#when the key changes	
	if old_tag and old_tag != this_tag:
		if list_size < 10:
			#fill the top 10 list
			tag_list.append(old_tag)		
			count_list.append(tag_count)
			list_size += 1
		elif tag_count > min(count_list):
			#update in place the top 10
			min_index = count_list.index(min(count_list))
			count_list[min_index] = tag_count
			tag_list[min_index] = old_tag
		tag_count=0
		old_tag=this_tag
	
	#when the key does not change
	tag_count += 1	#update the count for the current tag
	old_tag=this_tag

#Last Tag
if old_tag:
		if list_size < 10:
			tag_list.append(old_tag)		
			count_list.append(tag_count)
			list_size += 1
		elif tag_count > min(count_list):
			min_index = count_list.index(min(count_list))
			count_list[min_index] = tag_count
			tag_list[min_index] = old_tag

#Sort tags by count and print
tags=zip(count_list,tag_list)
tags=sorted(tags)
for i in range(10):
	index=len(tags)-i-1
	tup = tags[index]
	writer.writerow((tup[1],tup[0]))
