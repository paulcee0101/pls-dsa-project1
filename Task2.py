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

def maxCall(l):
    '''
    Function to segregate caller, receiver and duration of calls in each records
    Run Time Analysis = O(n^2 + n + 5 + 3n + 1 + n + 1) -> O(n^2 + 5n + 7) -> O(n^2)
    '''
    tmp_list = [j for i in l for idx, j in enumerate(i) if idx in (0, 1, 3)]
    num_list = [j for idx, j in enumerate(tmp_list) if idx % 3 != 2]
    unique_num_list = set(num_list)
    caller_list = num_list[0::2]
    receiver_list = num_list[1::2]
    duration_list = tmp_list[2::3]

    telephone_dict = dict.fromkeys(unique_num_list, 0)

    for caller, receiver, duration in zip(caller_list, receiver_list, duration_list):
        telephone_dict[caller] += int(duration)
        telephone_dict[receiver] += int(duration)

    max_duration = max(telephone_dict.values())
    max_telephone = [num for num, duration in telephone_dict.items() if duration == max_duration]

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_telephone[0], max_duration))

    return None

if __name__ == "__main__":
    maxCall(calls)
