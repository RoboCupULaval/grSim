import grSimRemote
import tkinter


class simpleapp_tk(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        action_list = []
        action_list.append({"text": "Kickoff",
                            "command": grSimRemote.move_to_kickoff})
        for action in action_list:
            button = tkinter.Button(self, **action)
            button.grid(column=0, row=0, pady=20)
        self.grid()
        self.grid_columnconfigure(0, pad=20)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
