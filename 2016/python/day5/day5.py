import hashlib

doorId = "uqwqemis"
# password = ""

# for x in range(20000000):
# 	keyToHash = doorId + str(x)
# 	m = hashlib.md5(keyToHash)
# 	hashedDoor = m.hexdigest()
# 	if hashedDoor[:5] == "00000":
# 		password += hashedDoor[5]
# 		if len(password) == 8:
# 			break

# print password

# 1a3099aa

password = {}

for x in range(40000000):
	keyToHash = doorId + str(x)
	m = hashlib.md5(keyToHash)
	hashedDoor = m.hexdigest()
	if hashedDoor[:5] == "00000" and hashedDoor[5].isdigit() and int(hashedDoor[5]) < 8:
		if int(hashedDoor[5]) not in password:
			password[int(hashedDoor[5])] = hashedDoor[6]
			if len(password) == 8:
				break
print password

# 694190cd