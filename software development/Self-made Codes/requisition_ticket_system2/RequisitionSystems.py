"""
In this program, a requisition system is made in which all the user information will be gathered and then request will be
marked according to the amount and then request status will be alloted to every requisition and manager will respond to 
pending requisitions and statistics will be showed at the end.

Author: Varinderjit singh  
"""


# requisitionsystem.py


class RequisitionSystem:
    requisition_counter = 10000  # starting value for the unique id
    all_requisitions = []        # all the will be stored here.
    
    def __init__(self):
        self.date = ""
        self.staff_id = ""
        self.name = ""
        self.requisition_id = 0
        self.items = []
        self.total_cost = 0.0
        self.status = "Pending" # default status
        self.ref_number = "Not available" 


    # collecting the information from the user
    def staff_info(self): 
        self.date = input("\n\nEnter today's date (DD/MM/YYYY): ")
        self.staff_id = input("Enter your staff ID: ")
        self.name = input("What is your name: ")

        RequisitionSystem.requisition_counter += 1
        self.requisition_id = RequisitionSystem.requisition_counter


    # getting the items and their prices the user want.
    def requisitions_details(self):
        print("\nEnter the items and their cost. Type 'done' when finished.")
        while True:
            item = input("Item name (or 'done'): ")
            if item.lower() == 'done':
                break
            try:
                price = float(input(f"Enter price for {item}: $ "))
                self.items.append((item, price))
                self.total_cost += price
            except ValueError:
                print("Invalid input. Please enter a numeric value for price.")


    # giving the status to the requisitions.
    def requisition_approval(self):  
        if 0 < self.total_cost < 500:
            self.status = "Approved"
            self.ref_number = self.staff_id.upper() + str(self.requisition_id)[-3:]
        elif self.total_cost >= 500:
            self.status = "Pending"


    # responding to the pending requisitions.
    def respond_requisition(self, new_status): 
        if self.status == "Pending" and new_status in ["Approved", "Not approved"]:
            self.status = new_status
            if new_status == "\033[1;32m Approved \033[0m":
                self.ref_number = self.staff_id.upper() + str(self.requisition_id)[-3:]
            else:
                self.ref_number = "Not available"


    # dispalying the requisitions with all the information like unique id, status, reference number.
    def display_requisition(self): 
        print(f"\nDate: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.name}")
        print(f"Total: ${self.total_cost:.2f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.ref_number}")


    # providing the statistics.
    def requisition_statistics(self): 
        total = len(RequisitionSystem.all_requisitions)
        approved = sum(1 for r in RequisitionSystem.all_requisitions if r.status == "Approved")
        pending = sum(1 for r in RequisitionSystem.all_requisitions if r.status == "Pending")
        not_approved = sum(1 for r in RequisitionSystem.all_requisitions if r.status == "Not approved")

        print("\n\nStatistics:")
        print("Displaying the Requisition Statistics")
        print(f"\nThe total number of requisitions submitted: {total}")
        print(f"The total number of \033[1;32mapproved\033[0m requisitions: {approved}")
        print(f"The total number of \033[1;33mpending\033[0m requisitions: {pending}")
        print(f"The total number of \033[1;31mnot approved\033[0m requisitions: {not_approved}")



# output section:

if __name__ == "__main__":
    # asking the user that how many times they want to enter requisitions.
    while True:
        try:
            count = int(input("\nHow many requisitions would you like to enter? "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


    print("\n\033[0;35m============= Requisition System =============\033[0m")

    # Getting input from the user for the specified number of times.
    for _ in range(count):
        requisition = RequisitionSystem()
        requisition.staff_info()
        requisition.requisitions_details()
        requisition.requisition_approval()
        RequisitionSystem.all_requisitions.append(requisition)
        # here, we have called all the functions, we made to gather user information.

    # dispalying the requisition after alloting status.
    print("\n\n\033[0;35m============ All Requisitions ==========\033[0m") 
    for req in RequisitionSystem.all_requisitions:
        req.display_requisition()

    # manager will updates the pending requests.
    for req in RequisitionSystem.all_requisitions: 
        if req.status == "Pending":
            print(f"\n\033[0;31mRequisition {req.requisition_id} is pending.\033[0m Respond to it.")
            decision = input("Approve or Not approve? (Enter 'Approved', 'Not approved' , or leave blank to skip): ")
            if decision in ["Approved", "Not approved"]:
                req.respond_requisition(decision)

    # dispalying the requisitions after the updates by manager.
    print("\n\n\033[1;33m=========== All Requisitions ===========\033[0m")
    for req in RequisitionSystem.all_requisitions:
        req.display_requisition()
        

    # getting the statistics.
    if RequisitionSystem.all_requisitions:
        RequisitionSystem.all_requisitions[0].requisition_statistics()