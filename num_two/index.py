import sys
import re
import csv

file = sys.argv[1]

fh = open(file)
outfile = open('output.csv', 'w')


# regex patterns
line_pattern = "^UVM_INFO|^UVM_WARNING|^UVM_ERROR"
message_type_pattern = "UVM_INFO|UVM_WARNING|UVM_ERROR"
path_pattern = r"(\/.*?\.[\w:]+)"
line_number_pattern = r'\([0123456789]+\)'
time_pattern = '[0123456789]+[a-z]+:'
timeunit_pattern = '[0123456789][a-z]+:'
hlocation_pattern = r':\s.\S+\s'
message_pattern = ''


# loop through lines
for line in fh.readlines():
	# detect if line has specified pattern
	message_type = ''
	filelocation = ''
	filename = ''
	line_number = ''
	time = ''
	timeunit = ''
	hlocation = ''
	message = ''

	if re.search(line_pattern, line):
		match = re.search(path_pattern, line)
		if match:
			path = line[match.start():match.end()]
			filename = path.split('/')[-1]
		
		match = re.search(line_number_pattern, line)
		if match:
			line_number = line[match.start()+1:match.end()-1]

		match = re.search(time_pattern, line)
		if match:
			time = line[match.start():match.end()]

		match = re.search(timeunit_pattern, line)
		if match:
			timeunit = line[match.start()+1:match.end()-1]
		
		match = re.search(hlocation_pattern, line)
		if match:
			hlocation = line[match.start()+2:match.end()-1]
			message = line[match.start()+2:].replace(hlocation, '')
		
		message_type = line.split(' ')[0]

		row = [message_type, filename, line_number, time, timeunit, hlocation, message]

		print(row)