def select_tickets_and_addons():
    options = []
    total_cost = 0

    print("\nTICKET TYPES & ADD_ONS")
    while True:
        name= input("Enter ticket type/add-on (e.g., VIP, Standard, Lightstick, Album) or 'done' to finish: ")
        if name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter the price for '{name}': $"))
            options.append((name, price))
            total_cost += price
        except ValueError:
            print("Invalid price, please enter a numeric value.")
    
    return options, total_cost