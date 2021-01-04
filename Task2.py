"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

"""
Method:
1. Construct list containing tuple of each phone calls
    as individual elements -> (calling, receiving)
2. Construct list containing duration of each phone calls
3. Construct dictionary that keeps unique telephone numbers as keys
4. For each iteration of call records, compute summation of individual
    phone numbers and the duration in that call
5. Extract Maximum duration from max() of dict.values() and conditioning
    to retrieve telephone number that corresponds to max duration
"""

def task2():

    telephone_numbers = dict()

    for record in calls:
        telephone_numbers[record[0]] = telephone_numbers.get(record[0], 0) + int(record[-1])
        telephone_numbers[record[1]] = telephone_numbers.get(record[1], 0) + int(record[-1])
    num_with_max_call = max(telephone_numbers, key=lambda x: telephone_numbers[x])
    print("{} spent the longest time, {} seconds, on the phone during September 2016."\
        .format(num_with_max_call, telephone_numbers[num_with_max_call]))

    return None

if __name__ == "__main__":
    task2()
