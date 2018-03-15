import hashlib

def file_hash(filename):
	"""Takes a string representing a file an input and returns the 256bit hash 
	of that file"""

	file_string = ''
	fin = open(filename)
	for line in fin:
		file_string += line.strip()
	return hashlib.sha256(file_string.encode()).hexdigest()

def file_to_list(filename):
	fin = open(filename)
	return_list = []
	for line in fin:
		return_list.append(line.strip())
	return return_list

def list_to_string(l):
	return_string = ''
	for item in l:
		return_string += item
	return return_string

def file_to_string(filename):
	return list_to_string(file_to_list(filename))

def sha256hash(data):
	return hashlib.sha256(data.encode()).hexdigest()

def mining(data):
	"""Takes in a string as inputn prompts the user to enter a difficulty,
	then mines for the correct hash"""
	current_hash = ''
	print('')
	print("Enter difficulty")
	difficulty = int(input())
	current_difficulty = 0
	print('')
	nonce = 0
	while current_hash[0:difficulty] != '0'*difficulty:
		nonce += 1
		current_guess = data + str(nonce)
		current_hash = hashlib.sha256(current_guess.encode()).hexdigest()
		print("Proof of Work", nonce, current_hash)
		
	return str(nonce)


if __name__ == "__main__":
	print('')

	print("Starting Block 1")
	block1 = file_to_list("exampleblock1.txt")
	block1.append("Proof of Work: " + mining(file_to_string("exampleblock1.txt")))

	print("Starting Block 2")
	block2 = [sha256hash(list_to_string(block1))] + file_to_list("exampleblock2.txt")
	block2.append("Proof of Work: " + mining(file_to_string("exampleblock2.txt")))

	print("Starting Block 3")
	block3 = [sha256hash(list_to_string(block2))] + file_to_list("exampleblock3.txt")
	block3.append("Proof of Work: " + mining(file_to_string("exampleblock3.txt")))

	blockchain = [block1, block2, block3]

	for block in blockchain:
		for transaction in block:
			print(transaction)
		print('')


