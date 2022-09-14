import re
source = open('regex_sum_1613394.txt', 'r')
text = ' '

# turn text document data into a string
for x in source:
    text += ' ' + x
#    print(text)
# find all the numbers in a string and put them in a list
for line in text:
    only_numbers = re.findall('\d+', text)

    print(only_numbers)
#    print(total)
    break
# this takes the values in the list of only_numbers and converts them to int then sums them
result = [eval(i) for i in only_numbers]
print(sum(result))
