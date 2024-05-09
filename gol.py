import tkinter as tk
import numpy as np
import time

# Taille de la grille
N = 50

class GameOfLife:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de la Vie")

        self.canvas = tk.Canvas(master, width=N*10, height=N*10, bg='white')
        self.canvas.pack()

        self.grid = np.random.choice([0, 1], size=(N, N), p=[0.5, 0.5])

        self.draw_grid()

        self.quit_button = tk.Button(master, text="Quitter", command=self.quit_game)
        self.quit_button.pack(side=tk.LEFT)

        self.restart_button = tk.Button(master, text="Relancer", command=self.restart_game)
        self.restart_button.pack(side=tk.RIGHT)

        self.running = False

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(N):
            for j in range(N):
                if self.grid[i][j] == 1:
                    self.canvas.create_rectangle(j*10, i*10, (j+1)*10, (i+1)*10, fill='black')

    def count_neighbors(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (0 <= x + i < N) and (0 <= y + j < N):
                    count += self.grid[x + i, y + j]
        return count

    def update_grid(self):
        new_grid = np.copy(self.grid)
        for i in range(N):
            for j in range(N):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i, j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i, j] = 0
                else:
                    if neighbors == 3:
                        new_grid[i, j] = 1
        self.grid = new_grid

    def start_game(self):
        self.running = True
        while self.running:
            self.update_grid()
            self.draw_grid()
            self.master.update()
            time.sleep(0.1)

    def quit_game(self):
        self.running = False
        self.master.quit()

    def restart_game(self):
        self.grid = np.random.choice([0, 1], size=(N, N), p=[0.5, 0.5])
        self.draw_grid()

root = tk.Tk()
game = GameOfLife(root)
game.start_game()
root.mainloop()
