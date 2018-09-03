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
	return file_to_list(list_to_string(filename))

def sha256hash(data):
	return hashlib.sha256(data.encode()).hexdigest()
	

if __name__ == "__main__":
	block1 = file_to_list("exampleblock1.txt")
	block2 = [sha256hash(list_to_string(block1))] + file_to_list("exampleblock2.txt")
	block3 = [sha256hash(list_to_string(block2))] + file_to_list("exampleblock3.txt")

	blockchain = [block1, block2, block3]

	for block in blockchain:
		for transaction in block:
			print(transaction)
		print('')
