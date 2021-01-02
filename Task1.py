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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
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
    By storing flattened list in a single lis tand converting to set to retrieve unique counts
    Run Time Analysis = O(n^2 + n^2 + 4) -> O(2n^2 + 4) -> O(n^2)
    """
    tmp_text = flatten(texts)
    tmp_call = flatten(calls)
    num_records = tmp_text + tmp_call
    count = len(set(num_records))
    print("There are {} different telephone numbers in the records."\
        .format(count))

    return None

if __name__ == "__main__":
    test()
