zoo = ["lion", "elephant", "monkey"]
number = 15

with open("output.txt", 'a') as f:
    f.write('\n' + ' and '.join(zoo))# Write a new line symbol into a file, along with all elements from the zoo list, joined by " and "
    f.write('\n'+ str(number))# Write a new line symbol and the value of the number variable into a file


