import hashlib

def file_hash(filename):
	"""Takes a string representing a file an input and returns the 256bit hash 
	of that file"""

	file_string = ''
	fin = open(filename)
	for line in fin:
		file_string += line.strip()
	return hashlib.sha256(file_string.encode()).hexdigest()


if __name__ == "__main__":
	flag = False
	current_hash = ''
	current_input = ''
	input_length = 0
	while not flag:

		print("Input what you would like to hash. Type 0 to end")
		print('')
		current_input = input()
		input_length = len(current_input)
		if current_input[input_length - 3:input_length] == 'txt':
			print(file_hash(current_input))
			print('')
		elif input == 0:
			flag = True
		else:
			print(hashlib.sha256(current_input.encode()).hexdigest())
			print('')