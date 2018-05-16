# Program:
	Secret Santa generator

# Purpose: 
	Randomly draw names without drawing previously drawn names from current year or any other year

# Inputs:
	user_id = refer to secret_santa_data.txt for user ID
	secret_santa_year = 3,4,5,...,n (this next year will be 4)

# Outputs: 
	Name

# Usage: 
	python secret_santa.py <user_id> <secret_santa_year>

# Dependencies: 
	secret_santa_data.txt

# Notes:
	-when running from the start, make sure the already_picked.txt file does not exist
	-if output returns NULL, run again
	-secret_santa_data.txt will have to be appended manually
