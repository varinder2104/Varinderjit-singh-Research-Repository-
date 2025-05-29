class Member:
    def __init__(self):
        self.total_members = 0
        self.diploma_count = 0
        self.bachelor_count = 0 
        self.withdrawn_count = 0
        self.member_list = []

    def register_member(self):
        """
        Register a new member and updates the member list and the ststistics
        """
        print("\n Enter member Information: ")
        student_id = input("Student ID: ")
        last_name = input("Last Name: ")
        programme = input("Programme (Diploma/Bachelor): ")

        self.total_members += 1
        membership_id = self.total_members # Auto-generate membership ID

        # Track programme count
        if programme.lower() == "diploma":
            self.diploma_count += 1
        elif programme.lower() == "bachelor":
            self.bachelor_count += 1
        else:
            print("Invalid input. Please choose the right programme")


        member = {
            "membership_id": membership_id,
            "student_id": student_id,
            "last_name": last_name,
            "programme": programme
        }
        self.member_list.append(member)
        print("Member registered successfully!")

    def withdraw_member(self):
        """
        Withdraws a member and updates the member list and statistics
        """
        print("\nWithdraw a Member")
        membership_id = int(input("Enter Membership ID: "))
        last_name = input("Enter Last name: ")

        for member in self.member_list:
            if member["membership_id"] == membership_id and member["last_name"].lower() == last_name.lower():
                self.member_list.remove(member)
                self.withdrawn_count += 1
                self.total_members -= 1

                # Adjust programme count
                if member["programme"].lower() == "diploma":
                    self.diploma_count -= 1
                elif member["programme"].lower() == "bachelor":
                    self.bachelor_count -= 1

                print(f"Membership ID: {membeeship_id} has been withdrrawn.")
                return
        print("Member not found or incorrect details provided.")

    def display_members(self):
        """
        Displays all members and statistics
        """
        print("\nRegistered Members: ")
        for member in self.member_list:
            print(f"Membership ID: {member['membership_id']}")
            print(f"Student ID: {member['student_id']}")
            print(f"Last Name: {member['last_name']}")
            print(f"Programme: {member['programme']}")

        print("Statistics")
        print(f"Total Registered Members: {self.total_members}")
        print(f"Diploma Students: {self.diploma_count}")
        print(f"Bachelor student: {self.bachelor_count}")
        print(f"Withdrawn members: {self.withdrawn_count}\n")

    def show_members_details(self):
        """
        Displays details of a specific member by membership ID.
        """
        print("\n Show Member Details: ")
        membership_id = int(input("Enter Membership ID: "))

        for member in self.member_list:
            if member["membership_id"] == membership_id:
                print(f"Membeeship ID: {member['membership_id']}")
                print(f"Student ID: {member['student_id']}")
                print(f"Last Name: {member['last_name']}")
                print(f"Programme: {member['programme']}")
                return
        print("Member not found with that Membership ID.")

    
    def main_menu(self):
        """
        Displays the main menu and handle user choices
        """
        
        while True:
            print("\n \033[43m ======= Membership Registration System ======= \033[0m \n")
            print("1. Register a New Member ")
            print("2. Withdraw a Member ")
            print("3. Display all members and statistics ")
            print("4. Show specific Member Details ")
            print("0. \033[31m Quit \033[0m")
            choice = input("\nEnter your choice (0-4): ")

            if choice == "1":
                self.register_member()
            elif choice == "2":
                self.withdraw_member()
            elif choice == "3":
                self.display_members()
            elif choice == "4":
                self.show_members_details()
            elif choice == "0":
                print("Existing the Membership system......")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 4.")


# Run the program
if __name__ == "__main__":
    member_system = Member()
    member_system.main_menu()