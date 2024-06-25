
import tkinter as tk
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import pong.pong as pong
import cardodge.cardodge as cardodge
import flappy_bird.flappy_bird as flappy_bird

class FullScreenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Move Master")
        self.root.attributes("-fullscreen", True)

       
        self.bg_image = Image.open("image.jpg")
        self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)

      
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        
        self.canvas.create_text(self.root.winfo_screenwidth() // 2, 50, text="Welcome to Move Master App", font=("Helvetica", 36, "bold"), fill="#E0FFFF")

        
        self.create_buttons()

    def create_buttons(self):
        button_font = font.Font(family='Helvetica', size=20, weight='bold')
        
        self.frame = tk.Frame(self.canvas,bg='#CC99FF')
       
        self.frame.place(relx=0.5, rely=0.5, anchor="n")

        
        
        self.button_frame = tk.Frame(self.frame,bg='#CC99FF')
        self.button_frame.pack(pady=20)

        
        self.button1 = tk.Button(self.button_frame, text="Cardodge",font=button_font,command=self.button1_action,bg='#ADD8E6',padx=25,pady=20)
        self.button1.pack(side="left", padx=10)

        self.button2 = tk.Button(self.button_frame, text="Ping Pong",font=button_font,command=self.button2_action,bg='#ADD8E6',padx=25,pady=20)
        self.button2.pack(side="left", padx=10)

        self.button3 = tk.Button(self.button_frame, text="Flappybird",font=button_font,command=self.button3_action,bg='#ADD8E6',padx=25,pady=20)
        self.button3.pack(side="left", padx=10)
        
        self.close_button = tk.Button(self.root, text="X",command=root.destroy,bg='white',padx=10,pady=3,fg='black',font=('arial',10,'bold'))
        self.close_button.place(relx=1.0, rely=0.0, anchor="ne")

        
    def button1_action(self):
        cardodge.start()

    def button2_action(self):
        pong.start()

    def button3_action(self):
        flappy_bird.start()
    

if __name__ == "__main__":
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
