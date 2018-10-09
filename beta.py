import random

print("\nBeta Stage\n")
food= open ("foods.txt", mode ="wt", encoding="utf-8")
food.write('sandwich \n')
food.write('dal \n')
food.write('beans \n')
food.write('cheese\n')
food.write('milk\n')
food.close()

file =open("foods.txt", "r")
print(file.read())
file.close

file1=open("foods.txt", 'r')
lines=list(file1)
value=random.choices(lines)
print(type(value))
print(value)
print("====")
print(lines)
file1.close()

print(', '.join(value))

#line=open(file).read().splitlines()
#print(line)
