import grSimRemote
import tkinter as tk
from tkinter import N, S, E, W
import referee


class controls(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.title = "Referee"
        self.parent = parent
        self.initialize()
        self.show_scoreboard()
        self.parent.after(1000, self.update)

    def show_scoreboard(self):
        self.newWindow = tk.Toplevel(self.parent)
        self.newWindow.title('Scoreboard')
        self.newWindow.geometry("800x200+25+25")
        self.scoreboard = scoreboard(self.newWindow)

    def update(self):
        result = referee.update_ball()
        if result:
            if result == "out":
                self.scoreboard.out()
            elif result == "blue":
                self.scoreboard.score_blue()
            elif result == "yellow":
                self.scoreboard.score_yellow()
            self.parent.after(2000, self.reset_and_update)
        else:
            self.parent.after(100, self.update)

    def reset_and_update(self):
        referee.reset()
        self.update()

    def initialize(self):
        action_list = []
        action_list.append({"text": "Kickoff",
                            "command": grSimRemote.move_to_kickoff})
        for action in action_list:
            button = tk.Button(self, **action)
            button.grid(column=0, row=0, pady=20)
        self.grid()
        self.grid_columnconfigure(0, pad=20)


class scoreboard(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.blue_score = 0
        self.yellow_score = 0

    def initialize(self):
        score_font = ("Impact", 96)
        message_font = ("Impact", 56)
        tk.Label(self, text="Yellow").grid(row=0, column=0, sticky=N+S+W+E)
        tk.Label(self, text="Score").grid(row=0, column=1, sticky=N+E+S+W)
        tk.Label(self, text="Blue").grid(row=0, column=2, sticky=N+E+W+S)
        self.yellow_score_label = tk.Label(self, text="0",
                                           fg="yellow", font=score_font)
        self.yellow_score_label.grid(row=1, column=0, sticky=N+S+W+E)
        self.message_label = tk.Label(self, font=message_font)
        self.message_label.grid(row=1, column=1, sticky=N+S+E+W)
        self.blue_score_label = tk.Label(self, text="0",
                                         fg="blue", font=score_font)
        self.blue_score_label.grid(row=1, column=2, sticky=N+S+E+W)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.pack(fill=tk.BOTH, expand=True)

    def out(self):
        self.show_message("Out!!!")

    def score_blue(self):
        self.show_message("Blue Score!!!")
        self.blue_score += 1
        self.blue_score_label.config(text=self.blue_score)

    def score_yellow(self):
        self.show_message("Yellow Score!!!")
        self.yellow_score += 1
        self.yellow_score_label.config(text=self.yellow_score)

    def show_message(self, message):
        self.message_label.config(text=message)
        self.after(3000, self.clear_message)

    def clear_message(self):
        self.message_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    win_controls = controls(root)
    root.mainloop()
