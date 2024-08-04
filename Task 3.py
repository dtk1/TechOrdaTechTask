class Cinema:
    
    def __init__(self):
        self.users = []
        self.movies = []
        self.tickets = []
        self.next_idMovies = 0
        self.next_idUsers = 0
        self.next_idTicket = 0

    def add_Movies(self, movie_title):
        self.movies.append(movie_title)
        movie_id = self.next_idMovies
        self.movies[movie_id] = movie_title
        self.next_idMovies += 1
        print(f"Movie was successfully added the ID is {movie_id}")  
     
    def show_Movies(self):
        k = 0
        for i in self.movies:
            print(f"{k}.{i}")
            k+=1
    def show_Users(self):
        j = 0
        for i in self.users:
            print(f"{j}.{i}")
            j+=1
    def add_Users(self, user_name):
         self.users.append(user_name)
         user_id = self.next_idUsers
         self.users[user_id] = user_name
         self.next_idUsers += 1
         print(f"User was successfully added the ID is {user_id}")

    def buy_Tickets(self, userId, movieId):
         self.tickets.append((userId, movieId))
         ticket_id = self.next_idTicket
         self.tickets[ticket_id] = (userId, movieId)
         self.next_idTicket += 1
         if (0 <= int(userId) < len(self.users)) and (0 <= int(movieId) < len(self.movies)):
              print(f"Ticket was bought by person under ID {userId} for movie with ID {movieId}")
         else:
              print("The input id is not exist in our database")

    def cancel_Tickets(self, ticket_id):
        if 0 <= int(ticket_id) < len(self.tickets):
            del self.tickets[int(ticket_id)]
            print(f"Ticket with ID {ticket_id} was successfuly cancelled")
            print("The current tickets")
            print(self.tickets)
        else:
            print(f"Ticket with ID {ticket_id} is not found")

def displayMenu():
        print("1. Добавить новый фильм ")
        print("2. Показать все доступные фильмы ")
        print("3. Добавить нового пользователя ")
        print("4. Показать всех доступных пользователей ")
        print("5. Купить билет ")
        print("6. Отменить покупку билета ")

my_cinema = Cinema()
while True:
    print()
    displayMenu()
    choice = input("Выберите действие: ")
    print()
    if choice == "1":
         addname = input("Input name of the movie: ")
         my_cinema.add_Movies(addname)
    if choice == "2":
         my_cinema.show_Movies()
    if choice == "3":
         addname = input("Input name of the user: ")
         my_cinema.add_Users(addname)
    if choice == "4":
         my_cinema.show_Users()
    if choice == "5":
         addIdUser = input("Input id of the user: ")
         addId = input("Input id of the film: ")
         my_cinema.buy_Tickets(addIdUser, addId)
    if choice == "6":
         ticketid = input("Input ticketid you want to cancel: ")
         my_cinema.cancel_Tickets(ticketid)
    
    