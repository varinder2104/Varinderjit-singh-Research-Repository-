"""
In this program, we will gather the information of the staff member and will issue a unique requisition id.

Author: Varinderjit singh
"""

def staff_info(id_counter):
    # this function will just ask the users to input the required details.
    date = input("Enter today's date in DD/MM/YYYY: ")
    staff_id = input("Enter your staff ID: ")
    name = input("What is your name: ")

    requisition_id = id_counter + 1
    id_counter = requisition_id
    # here, the unique requisition id will be issued.
    return id_counter, requisition_id, date, name, staff_id