"""
In this program, we will import the functions from other programs and display the output of all the programs together here.

Author: Varinderjit singh
"""


from task1_requisition import staff_info
from task2_total import requisitions_total
from task3_approval import requisition_approval
# here, we are using from/import option to import functions from other programs.

def display_requisitions():
    id_counter = 10000
    
    id_counter, requisition_id, date, name, staff_id = staff_info(id_counter)
    option, total_cost = requisitions_total()
    status, ref_number = requisition_approval(total_cost, requisition_id, staff_id)
# here, we call out the variables from the called functions.

    print("\n\nPrinting Requisitions")
    print(f"\n\nDate: {date}")
    print(f"\nRequisition_id: {requisition_id}")
    print(f"\nStaff ID: {staff_id}")
    print(f"\nStaff Name: {name}")
    
    print(f"\nTotal cost: ${total_cost:.2f}") #here, we use .2f for getting the output in two decimal places after the decimal.
    print(f"\nStatus: {status}")
    if status == "Approved": 
        print(f"\nApproval Reference Number: {ref_number}")
# we use if for the status conditions that if approved print this, if not print nothing.

def main():
    display_requisitions()

if __name__ == "__main__":
    main()