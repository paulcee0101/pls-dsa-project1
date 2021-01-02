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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Assumptions:
1. All telephone numbers found within calls.csv is from Bangalore
2. Area codes can be any numbers as long it starts with 0 and it is
  encapsulated within "()"
3. Mobile Prefixes can start with either "7", "8", or "9"; they are
  first 4 digits long
4. Telemarketers are not being requested by the question and thus have
  been omitted from the answer
"""

""" PART A """
def getAreaCode(num):
    """
    Function to retrieve Area Codes of Fixed Telephone Lines
    Run Time Analysis = O(3) -> O(1)
    """
    tmp_idx = (num.index("("), num.index(")"))
    area_code = num[tmp_idx[0] : tmp_idx[-1] + 1]

    return area_code

def getMobilePrefix(num):
    """
    Function to retrieve Mobile Prefixes from Mobile Numbers
    Run Time Analysis = O(1)
    """
    return num[:5]

def flatten(l):
    """
    Function to extract only valid telephone entries from records provided as list
    Run Time Analysis = O(n^2)
    """
    flat_list = [j for i in l for idx, j in enumerate(i) if idx in (0,1)]

    return flat_list

def partA():
    """
    Run Time Analysis = O(2 + n^2 + 5n + 3 + 1 + 2 + 1 + 2n + 2n) -> O(n^2 + 9n + 9) -> O(n^2)
    """
    area_codes = []
    mobile_prefixes = []

    flat_list = flatten(calls)

    for num in flat_list:
        if num.startswith("("):
            area_codes.append(getAreaCode(num))
        elif num.startswith("7") or num.startswith("8") or num.startswith("9"):
            mobile_prefixes.append(getMobilePrefix(num))
        else:
            continue

    area_codes = sorted(set(area_codes))
    mobile_prefixes = sorted(set(mobile_prefixes))

    print("The numbers called by people in Bangalore have codes:")
    for num in area_codes:
      print(num)
    for num in mobile_prefixes:
      print(num)

    return None

""" PART B """

def partB():
    """
    Run Time Analysis = O(n^2 + 4 + 5n + 3) -> O(n^2 + 5n + 7) -> O(n^2)
    """
    flat_list = flatten(calls)
    caller_list = flat_list[0::2]
    receiver_list = flat_list[1::2]

    total_calls = len(calls)
    count = 0

    for caller, receiver in zip(caller_list, receiver_list):
        if caller.startswith("(") and receiver.startswith("("):
            count += 1
        else:
            continue

    percentage = (count / total_calls) * 100
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."\
      .format(percentage))

    return None

if __name__ == "__main__":
    partA()
    partB()

