
import os

for root, dirs, files in os.walk("../src/"):
	for file in files:
		if file.endswith("."): # You should change the file's extension here
			print(os.path.join(root, file))