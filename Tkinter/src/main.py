import tkinter as tk
class HelloCore2webApp:
    def __init__(self):
        self.root = tk.Tk()
       
        self.root.title("Hello Core2web")
        self.root.configure(bg ="grey")


        self.root.geometry("300x200")
        self.label=tk.Label(self.root,text =" ",fg="red")
        self.label.pack(pady=10)

        self.hello_button = tk.Button(self.root,text="Click ME",fg="blue",command=self.display_messege)
        self.hello_button.pack(pady=10)
       
    def display_messege(self):
        self.label.config(text="Hello,Core2Web!")

    def run(self):
        #Run the tkinter event loop
        self.root.mainloop()
        
if __name__ == '__main__':
    app=HelloCore2webApp()
    app.run()