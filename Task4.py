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

def flatten(l):
    """
    Function to extract only valid telephone entries from records provided as list
    Run Time Analysis = O(n^2)
    """
    flat_list = [j for i in l for idx, j in enumerate(i) if idx in (0,1)]

    return flat_list

def test():
    """
    Run Time Analysis = O(1 + n^2 + 2 + 8n + 2 + 2n + 1) - > O(n^2 + 10n + 6) -> O(n^2)
    """
    telemarketer_list = []

    text_list = flatten(texts)
    call_list = flatten(calls)
    caller_list = call_list[0::2]
    receiver_list = call_list[1::2]

    for num in caller_list:
        if num not in text_list:
            if num not in receiver_list:
                telemarketer_list.append(num)
            else:
                continue
        else:
            continue

    telemarketer_list = sorted(set(telemarketer_list))

    print("These numbers could be telemarketers: ")
    for num in telemarketer_list:
        print(num)

    return None

if __name__ == "__main__":
    test()
