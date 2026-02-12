# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    total_tickets = 0

    number_of_movies = int(input("How many movies would you like to enter? "))

    for i in range(number_of_movies):
        movie_name = input("\nEnter the name of the movie: ")
        tickets = int(input(f"How many tickets for '{movie_name}'? "))
        total_tickets += tickets

    print("\n------------------------------")
    print(f"Total tickets desired: {total_tickets}")
    print("------------------------------")
    ######################


if __name__ == '__main__':
    main()
