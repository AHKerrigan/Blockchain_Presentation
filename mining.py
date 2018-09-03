import hashlib


if __name__ == "__main__":
	flag = False
	while not flag:
		current_hash = ''
		print('')
		print("Enter data")
		current_data = input()
		print('')
		print("Enter difficulty")
		difficulty = int(input())
		current_difficulty = 0
		print('')
		nonce = 0
		while current_hash[0:difficulty] != '0'*difficulty:
			current_guess = current_data + str(nonce)
			current_hash = hashlib.sha256(current_guess.encode()).hexdigest()
			print(current_data, nonce, current_hash)
			nonce += 1






