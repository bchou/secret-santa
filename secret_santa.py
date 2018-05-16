##################################################################################
##################################################################################
# Program: Secret santa generator
#
# Purpose: Randomly draw names without drawing previously drawn names from current year or any other year
#
# Inputs:
#			user_id = refer to block comment below for user_id
#			secret_santa_year = 3,4,5,...,n (this next year will be 4)
#
# Outputs: Name
#
# Usage: python secret_santa.py <user_id> <secret_santa_year>
#
# Dependencies: secret_santa_data.txt
#
# Notes:
#			-when running from the start, make sure the already_picked.txt file does not exist
#			-if output returns NULL, run again
#			-secret_santa_data.txt will have to be appended manually
##################################################################################
##################################################################################


##################################################################################
# ID - Names
# 0 - The Brain
# 1 - Cristine
# 2 - Pinky
# 3 - Dabrina
# 4 - Michelle
# 5 - Ken
# 6 - Mickey
# 7 - Kendal
# 8 - Quesadilla
# 9 - Brando
# 10 - Van Christopher
##################################################################################

import random
import sys
import os    

user_id = int(sys.argv[1])
num_years = int(sys.argv[2])
names = ['The Brain','TinayXD','Pinky','Dabrina','Michelle','Ken','Mickey','Kendal','Quesadiila','Brando','Van Christopher']
flag = 1

list = []
with open('secret_santa_data.txt') as fid:
	for line in fid:
		data = line.split()
		list.append(data)
fid.close()
list[user_id].pop(0)
exclude = map(int,list[user_id])

list = []
if os.path.isfile('already_picked.txt'):
	with open('already_picked.txt') as fid:
		for line in fid:
			data = line.split()
			list.append(data)
	exclude = exclude + map(int,list[0])
fid.close()

while flag:
	pick = random.randint(0,10)
	if pick not in exclude:
		if os.path.isfile('already_picked.txt'):
			fid = open('already_picked.txt','a')
			fid.write(' ' + str(pick))
			fid.close()
		else:
			fid = open('already_picked.txt','w+')
			fid.write(' ' + str(pick))
			fid.close()
		print ''
		print 'You got ' + names[pick] + '!'
		flag = 0
	elif len(exclude) == 11:
		print ''
		print 'No more people to pick sucka!'
		flag = 0