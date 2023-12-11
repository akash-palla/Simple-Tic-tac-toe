import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_gui()

    def create_gui(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=20, height=10, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                self.show_winner_message()
            elif self.is_board_full():
                self.show_draw_message()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(cell != "" for row in self.board for cell in row)

    def show_winner_message(self):
        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.window.quit()

    def show_draw_message(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.window.quit()

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()