from tkinter import Tk, Label


class Window:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Krappy")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

    def run(self) -> None: self.root.mainloop()


if __name__ == "__main__": Window().run()
