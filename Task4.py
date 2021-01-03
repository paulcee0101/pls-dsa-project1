"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Assuming that telemarketer numbers that start with code "140" is not required by question
"""

def task4():

    caller_numbers = set()
    non_telemarketer_numbers = set()

    for record in texts:
        non_telemarketer_numbers.add(record[0])
        non_telemarketer_numbers.add(record[1])

    for record in calls:
        caller_numbers.add(record[0])
        non_telemarketer_numbers.add(record[1])

    telemarketer_numbers = caller_numbers.difference(non_telemarketer_numbers)
    telemarketer_numbers = sorted(telemarketer_numbers)

    print("These numbers could be telemarketers: ")
    for num in telemarketer_numbers:
        print(num)

    return None

if __name__ == "__main__":
    task4()
