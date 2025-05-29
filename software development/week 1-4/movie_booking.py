def movie_ticket_booking():
    movies= ["Furiosa","Interstellar","7 Heavens"]
    movie_prices= ["Furiosa":10,"Interstellar":20,"7 Heavens":25]

    while True:
        try:
            tickets=int(input("How many tickets would you like to book? "))
            if tickets <= 0:
                print("You must book at least one ticket.")
                continue
            print("AVAILABLE MOVIES")
            for i, movie in enumerate(movies,1):
                print(f"{i}. {movie}")

            movie_choice= int(input("please select a movie by number: "))
            if movie_choice < 1 or movie_choice > len(movies):
                print("Invalid choice. Please select a valid number.")
                continue
            selected_movie = movies[movie_choice - 1]
            total_price= movie_prices[selected_movie] * tickets
            print(f"\nBooking Summary: {tickets} tickets for '{selected_movie}' at ${movie_prices[selected_movie]} each.")
            print(f)