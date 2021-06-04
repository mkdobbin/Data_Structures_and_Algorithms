# python3

import random 
import sys 
import os

# accept the number of tests as a command line parameter
tests = int(sys.argv[1])

# accept the parameter for the tests as a command line parameter n = int(sys.argv[2])
n = int(sys.argv[2])

for i in range(tests):
    print("”Test #" + str(i))

# run the generator gen.py with parameter n and the seed i
os.system("python3 test_gen_maximum_pairwise_product.py " + str(n) + " " + str(i) + "  > input.txt") 

# run the main solution
os.system("python3 maximum_pairwise_product.py < input.txt > main.txt")

# read the output of the main solution:
with open('main.txt') as f: 
    main = f.read() 
print("Main: ", main)
