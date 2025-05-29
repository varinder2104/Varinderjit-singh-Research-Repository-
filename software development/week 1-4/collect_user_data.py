def collect_user_data(id_counter):
    unique_id = id_counter + 1

    # input user data
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter Email address: ")

    # display the collected user data
    print(f"\nUser Information: ")
    print(f"\n\nNmae: {name}")
    print(f"\nAge: {age}")
    print(f"\nEmail Address: {email}")
    print(f"unique ID: {unique_id}")

    # return the unique_id
    return unique_id


def main():
    id_counter = 5000
    users = []

    while True:
        # collecting user information and the unique id
        unique_id = collect_user_data(id_counter)

        # update the id counter
        id_counter += 1

        # store the unique id and collected user data into an empty array/list
        users.append(unique_id)

        continue_input = input("\nDo you want to enter another user? (yes/no):")

        if continue_input != "yes":
            break

    # print all collected unique IDs
    print ("\nAll collected user IDs:")
    for uid in users:
        print(f"Unique ID: {uid}")

main()