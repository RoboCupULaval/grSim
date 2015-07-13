import grSimRemote
import tkinter as tk
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
            self.parent.after(5, self.update)

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

    def initialize(self):
        self.grid()

    def out(self):
        self.show_message("Out!!!")

    def score_blue(self):
        self.show_message("Blue Score!!!")

    def score_yellow(self):
        self.show_message("Yellow Score!!!")

    def show_message(self, message):
        print(message)


if __name__ == "__main__":
    root = tk.Tk()
    win_controls = controls(root)
    root.mainloop()
