# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 02:36:27 2022

@author: Jony
"""

from datetime import datetime
'''
This task is to fix this code to write out a simple monthly report. The report 
should look professional.
The aim of the exercise is to:
- Ensure that the code works as specified including date formats
- Make sure the code will work correctly for any month
- Make sure the code is efficient
- Ensure adherence to PEP-8 and good coding standards for readability
- No need to add comments unless you wish to
- No need to add features to improve the output, but it should be sensible 
given the constraints of the exercise.
Code should display a dummy sales report
'''
# Do not change anything in the section below, it is just setting up some 
# sample data
# test_data is a dictionary keyed on day number containing the date and sales 
# figures for that day
month = "02"
test_data = {f"{x}": {"date": datetime.strptime(f"2021{month}{x:02d}", 
                                                "%Y%m%d"),
                      'sales': float(x ** 2 / 7)} for x in range(1, 29)}
# Do not change anything in the section above, it is just setting up some 
# sample data
start = test_data['1'].copy()
end = test_data['28'].copy()


def DateToDisplayDate(date):
    # E.g. Monday 8th February, 2021
    a = date.strftime("%A")
    b = date.strftime("%d")
    c = date.strftime("%B")
    d = date.strftime("%Y")
    return (f"""{a} {b}th {c}, {d}""")
            
start["date"] = DateToDisplayDate(start["date"])
end["date"] = DateToDisplayDate(end["date"])
print("Sales Report\nReport start date: " + start["date"] + " starting value: " 
      + str(start["sales"]) + "\n" + "Report end date: " + end["date"] + 
      " total sales: " + str(end["sales"]) + "\n")
total = 0
for k, v in test_data.items():
    print("Date                                Sales    Month to Date  ")
    if month == "02" and k == "29":
        print("Leap year")  # Must be displayed if data is for a leap year
    print(f"{DateToDisplayDate(v['date'])} {v['sales']} ${total}")
    total += v['sales']
    print(f"Total sales for the month ${total}")