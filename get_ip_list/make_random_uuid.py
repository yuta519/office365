import random
import string

def create_uuid4():
	x = lambda: string.hexdigits[random.randint(0, 15)]
	h = lambda digits: ''.join([x() for _ in range(0, digits)])
	return h(8) + '-' + h(4) + '-' + h(4) + '-' + h(4) + '-' + h(12)

if __name__ == '__main__':
	for i in range(10):
		print(create_uuid4())