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

""" PART A """

def task3partA():

    telephone_codes = set()

    for record in calls:
      if record[0].startswith("(080)"):
          if record[1].startswith("("):
              telephone_codes.add(record[1][record[1].index("(") + 1 : record[1].index(")")])
          elif record[1].startswith("7") or record[1].startswith("8") or record[1].startswith("9"):
              telephone_codes.add(record[1][:4])
          elif record[1].startswith("140"):
              telephone_codes.add("140")
          else:
              pass

    telephone_codes = sorted(telephone_codes)

    print("The numbers called by people in Bangalore have codes:")
    for idx in range(len(telephone_codes)):
        print(telephone_codes[idx])

    return None

""" PART B """

def task3partB():

    count_caller = 0
    count_receiver = 0

    for record in calls:
        if record[0].startswith("(080)"):
            count_caller += 1
            if record[1].startswith("(080)"):
                count_receiver += 1
            else:
                pass
        else:
            continue

    percentage = (count_receiver / count_caller) * 100
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."\
      .format(percentage))

    return None

if __name__ == "__main__":
    task3partA()
    task3partB()

