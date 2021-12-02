input_file = open('input.txt', 'r')
lines = input_file.readlines()

sum_of_increases = 0
sum_of_decreases = 0

for i in range(0, len(lines)):
    if i == 0:
        print(lines[i].rstrip(), "N/A")
        continue
    if int(lines[i].strip()) > int(lines[i-1].strip()):
        sum_of_increases += 1
        print(lines[i].rstrip(), "Increased!")
    else:
        sum_of_decreases += 1
        print(lines[i].rstrip(), "Decreased!")

print("\n\n\n\nResults:")
print("Sum of incereases:", sum_of_increases)
print("Sum of decreases:", sum_of_decreases)
input_file.close()
