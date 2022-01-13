import sys

inputs = sys.argv
inputs.pop(0)

for index,i in enumerate(inputs):
    num = int(sys.argv[index])
    if(num%3==0 and num%5==0):
        print("fizzbuzz")
    elif(num%5==0):
        print("buzz")
    elif(num%3==0):
        print("fizz")
    else:
        print(num)