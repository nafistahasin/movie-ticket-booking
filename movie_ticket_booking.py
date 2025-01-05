from tkinter import *
from tkinter import messagebox

class MovieTicketBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Ticket Booking")
        self.root.geometry("500x400")


        self.movies = ["Pirates of The Carribean", "Spider-Man: No Way Home", "Avengers: Endgame"]
        self.movie_var = StringVar()
        self.movie_var.set(self.movies[0])

        self.times = ["10:00 AM", "12:00 PM", "2:00 PM", "4:00 PM", "6:00 PM", "8:00 PM"]
        self.time_var = StringVar()
        self.time_var.set(self.times[0])

        self.seats = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.seat_var = StringVar()
        self.seat_var.set(self.seats[0])

        self.prices = {
            "Pirates of The Carribean": 100,
            "Spider-Man: No Way Home": 120,
            "Avengers: Endgame": 150
        }

        movie_label = Label(self.root, text="Select Movie:")
        movie_label.grid(row=0, column=0, padx=10, pady=10)
        movie_dropdown = OptionMenu(self.root, self.movie_var, *self.movies)
        movie_dropdown.grid(row=0, column=1, padx=10, pady=10)

        time_label = Label(self.root, text="Select Time:")
        time_label.grid(row=1, column=0, padx=10, pady=10)
        time_dropdown = OptionMenu(self.root, self.time_var, *self.times)
        time_dropdown.grid(row=1, column=1, padx=10, pady=10)

        seat_label = Label(self.root, text="Select Seat:")
        seat_label.grid(row=2, column=0, padx=10, pady=10)
        seat_dropdown = OptionMenu(self.root, self.seat_var, *self.seats)
        seat_dropdown.grid(row=2, column=1, padx=10, pady=10)

        book_button = Button(self.root, text="Book Ticket", command=self.book_ticket)
        book_button.grid(row=3, column=0, columnspan=2, pady=20)

    def book_ticket(self):
        movie_name = self.movie_var.get()
        show_time = self.time_var.get()
        selected_seat = self.seat_var.get()
        price = self.prices[movie_name]

        ticket_message = f"""
        Movie: {movie_name}
        Time: {show_time}
        Seat: {selected_seat}
        Price: ${price}
        """

        messagebox.showinfo("Ticket Details", ticket_message)

if __name__ == "__main__":
    root = Tk()
    app = MovieTicketBooking(root)
    root.mainloop()
