# importing library for the GUI
import customtkinter as ctk
import tkinter as tk
import sqlite3 as sql
# importing Pillow module for image processing
from PIL import Image

# Hotel Management System
class HMS(ctk.CTk, tk.Tk):
    dialog = None
    def __init__(self):
        super().__init__() # Calling the parent class constructor
        ctk.set_appearance_mode("dark") # Setting the theme mode for window

        self.connect = sql.connect("GUESTS LIST.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS GUESTS_LIST (NAME TEXT , ADDRESS TEXT , P_NUMBER TEXT,ROOM_NO INT,NO_OF_DAYS INT, TYPE_OF_ROOM INT,PAYMENT INT)")

        self.attributes("-fullscreen",True)
        self.title("Hotel Management System")
        self.height = self.winfo_screenheight()
        self.width = self.winfo_screenwidth()
        self.geometry(f"{self.width}x{self.height}")
        self.bind("<Escape>",self.resize)
        self.images = ["bg_image.jpg","bg_image1.jpg","bg_image2.jpg"]
        bg_image = Image.open(self.images[2])
        menu_image = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(self.width-50, self.height-40))
        self.after(2,self.change_bg_image)
        self.frame =  ctk.CTkFrame(master=self, border_width=2, border_color=("orange","#FFCC70"))
        self.frame.pack(padx=(5,15), pady=15, fill="both", expand=True,side = "right")

        self.home = ctk.CTkLabel(
            self,
            image=menu_image,
            fg_color = "#FFCC70",
            corner_radius = 5,
            text="WELCOME",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 70)
        )
        self.home.pack(padx=(15,5), pady=15, fill="both", expand=True)

        user_label = ctk.CTkLabel(
            self.frame,
            fg_color = "transparent",
            corner_radius = 5,
            text="Enter User Name:",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 25)
        )
        user_label.pack(padx=15, pady=(200,5),anchor = "center")

        self.user_entry = ctk.CTkEntry(
            self.frame,
            width=200,
            height=30,
            placeholder_text="Enter User Name",
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            placeholder_text_color=("orange","#FFCC70"),
            border_width=2,
            border_color=("orange","#FFCC70"),
        )
        self.user_entry.pack(pady=10, padx=5,anchor="center")

        user_password_label = ctk.CTkLabel(
            self.frame,
            fg_color = "transparent",
            corner_radius = 5,
            text="Enter Password:",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 25)
        )
        user_password_label.pack(padx=15, pady=(20,5),anchor = "center")


        self.user_password_entry = ctk.CTkEntry(
            self.frame,
            width=200,
            height=30,
            placeholder_text="Enter Password",
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            placeholder_text_color=("orange","#FFCC70"),
            border_width=2,
            border_color=("orange","#FFCC70"),
        )
        self.user_password_entry.pack(pady=10, padx=5,anchor="center")

        password_button = ctk.CTkButton(
            self.frame,
            command = self.user,
            text = "OK",
            font=("times new roman",20),
        )
        password_button.pack(padx=55,pady=15,anchor="center")

    def user(self,event=None):
        if self.user_entry.get() == "mr0039" and self.user_password_entry.get() == "m.rizwan":
            self.menu()
        if self.user_entry.get() != "mr0039":
            self.user_entry.delete("0","end")
            self.user_entry.configure(placeholder_text="!Invalid user name")
        if self.user_password_entry.get() != "m.rizwan":
            self.user_password_entry.delete("0","end")
            self.user_password_entry.configure(placeholder_text="!Invalid password")

    def change_bg_image(self):
        self.images[0],self.images[1]=self.images[1],self.images[0]
        self.images[1],self.images[2]=self.images[2],self.images[1]
        bg_image = Image.open(self.images[0])
        menu_image = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(self.width-50, self.height-40))
        self.home.configure(image = menu_image)
        self.after(15000,self.change_bg_image)

    def menu(self):
        for widget in self.winfo_children():
            widget.pack_forget()

        png_1 = Image.open("check_in.png")
        check_in_icon = ctk.CTkImage(light_image=png_1, dark_image=png_1, size=(50, 50))
        png_2 = Image.open("suitcase.png")
        check_out_icon = ctk.CTkImage(light_image=png_2, dark_image=png_2, size=(40, 40))
        png_3 = Image.open("list.png")
        guest_list_icon = ctk.CTkImage(light_image=png_3, dark_image=png_3, size=(50, 50))
        png_4 = Image.open("info.png")
        guest_info_icon = ctk.CTkImage(light_image=png_4, dark_image=png_4, size=(35, 35))
        png_5 = Image.open("logout.png")
        exit_icon = ctk.CTkImage(light_image=png_5, dark_image=png_5, size=(40, 40))

        self.frame_1 = ctk.CTkFrame(master=self, border_width=2, border_color=("orange","#FFCC70"))
        self.frame_1.pack(padx=15, pady=15, fill="both", expand=True)

        welcome_label = ctk.CTkLabel(
            master=self.frame_1,
            text="WELCOME",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 70),
            fg_color=("transparent"),
        )
        welcome_label.pack(padx=10, pady=10, anchor="center")

        check_in_button = ctk.CTkButton(
            master=self.frame_1,
            command=self.check_in,
            text_color=("black", "white"),
            image=check_in_icon,
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("transparent"),
            hover_color=("orange","#FFCC70"),
            corner_radius=10,
            font=("times new roman", 20),
            text="1.CHECK IN",
            height=103,
            width=556,
        )
        check_in_button.pack(padx=171, pady=4, anchor="center")

        check_out_button = ctk.CTkButton(
            master=self.frame_1,
            command=self.check_out,
            image=check_out_icon,
            text_color=("black", "white"),
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("transparent"),
            hover_color=("orange","#FFCC70"),
            corner_radius=10,
            font=("times new roman", 20),
            text="2.CHECK OUT",
            height=103,
            width=556,
        )
        check_out_button.pack(padx=171, pady=4, anchor="center")

        guest_list_button = ctk.CTkButton(
            master=self.frame_1,
            command=self.guest_list,
            image=guest_list_icon,
            border_color=("orange","#FFCC70"),
            text_color=("black", "white"),
            border_width=2,
            fg_color=("transparent"),
            hover_color=("orange","#FFCC70"),
            corner_radius=10,
            font=("times new roman", 20),
            text="3.GUEST LIST",
            height=103,
            width=556,
        )
        guest_list_button.pack(padx=171, pady=4, anchor="center")

        guest_info_button = ctk.CTkButton(
            master=self.frame_1,
            command=self.password_window,
            image=guest_info_icon,
            border_color=("orange","#FFCC70"),
            text_color=("black", "white"),
            border_width=2,
            fg_color=("transparent"),
            hover_color=("orange","#FFCC70"),
            corner_radius=10,
            font=("times new roman", 20),
            text="4.GUEST INFO",
            height=103,
            width=556,
        )
        guest_info_button.pack(padx=171, pady=4, anchor="center")

        exit_button = ctk.CTkButton(
            master=self.frame_1,
            command=self.exit,
            image=exit_icon,
            text_color=("black", "white"),
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("red"),
            hover_color="darkred",
            corner_radius=10,
            font=("times new roman", 20),
            text="5.EXIT",
            height=103,
            width=556,
        )
        exit_button.pack(padx=171, pady=(4,10), anchor="center")

    def check_in(self):
        for widget in self.winfo_children():
            widget.pack_forget()

        global deluxe_list,general_list,joint_list
        deluxe_list = [1,2,3,4,5,6,7,8,9,10]
        general_list = [21,22,23,24,25,26,27,28,29,30]
        joint_list = [41,42,43,44,45,46,47,48,49,50]

        deluxe_count = self.cursor.execute("SELECT * FROM GUESTS_LIST WHERE TYPE_OF_ROOM = 'DELUXE'")
        for i in deluxe_count:
            deluxe_list.pop(0)

        general_count = self.cursor.execute("SELECT * FROM GUESTS_LIST WHERE TYPE_OF_ROOM = 'GENERAL'")
        for i in general_count:
            general_list.pop(0)

        joint_count = self.cursor.execute("SELECT * FROM GUESTS_LIST WHERE TYPE_OF_ROOM = 'JOINT'")
        for i in joint_count:
            joint_list.pop(0)

        png_1 = Image.open("check_in.png")
        check_in_icon = ctk.CTkImage(light_image=png_1, dark_image=png_1, size=(40, 40))
        png_5 = Image.open("back.png")
        exit_icon = ctk.CTkImage(light_image=png_5, dark_image=png_5, size=(40, 40))

        self.radio_var = ctk.IntVar()
        ctk.set_default_color_theme("green")
        self.grid_rowconfigure((0,1,2,3,4,5,6,7),weight = 1)
        self.grid_columnconfigure((0,1,2,3,4),weight = 1)
        self.frame_2 = ctk.CTkFrame(
            master=self, height=20, border_width=2, border_color=("orange","#FFCC70")
        )
        self.frame_2.grid(row=0, column=0,rowspan = 7,columnspan = 5, padx=15, pady=(15,5), sticky="news")

        return_button = ctk.CTkButton(
            master=self.frame_2,
            command = self.back,
            image=exit_icon,
            text_color=("black", "white"),
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("red"),
            hover_color="darkred",
            corner_radius=0,
            font=("times new roman", 20),
            text="RETURN",
            #height=103,
            width=290,
        )
        return_button.grid(row=0, column=0, pady=0, padx=(0,15),sticky = "ews")

        check_in_label = ctk.CTkLabel(
            master=self.frame_2,
            text="CHECK IN",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 50),
            fg_color=("transparent"),
        )
        check_in_label.grid(row=0, column=2, pady=10, padx=5)

        self.name_entry = ctk.CTkEntry(
            self.frame_2,
            width=450,
            height=50,
            placeholder_text="Enter Guest Name",
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            placeholder_text_color=("orange","#FFCC70"),
            border_width=2,
            border_color=("orange","#FFCC70"),
        )
        self.name_entry.grid(row=1, column=2, pady=10, padx=5)

        self.address_entry = ctk.CTkEntry(
            self.frame_2,
            width=450,
            height=50,
            placeholder_text="Enter Guest Address",
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            placeholder_text_color=("orange","#FFCC70"),
            border_width=2,
            border_color=("orange","#FFCC70"),
        )
        self.address_entry.grid(row=2, column=2, pady=10, padx=5)

        self.phone_entry = ctk.CTkEntry(
            self.frame_2,
            width=450,
            height=50,
            placeholder_text="Enter Guest's Phone No",
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            placeholder_text_color=("orange","#FFCC70"),
            border_width=2,
            border_color=("orange","#FFCC70"),
        )
        self.phone_entry.grid(row=3, column=2, pady=10, padx=5)

        self.days_entry = ctk.CTkEntry(
            self.frame_2,
            width=450,
            height=50,
            placeholder_text="Enter No of days",
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            placeholder_text_color=("orange","#FFCC70"),
            border_width=2,
            border_color=("orange","#FFCC70"),
        )
        self.days_entry.grid(row=4, column=2, pady=10, padx=5)

        rooms_label = ctk.CTkLabel(
            master=self.frame_2,
            text="Choose Room Type:",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 25),
            fg_color=("transparent"),
        )
        rooms_label.grid(row=5, column=0, pady=10, padx=15)

        self.room_1 = ctk.CTkCheckBox(
            self.frame_2,
            text=f"Deluxe Room  ({len(deluxe_list)})",
            onvalue=1,
            offvalue=0,
            #checkbox_height=40,
            #checkbox_width=70,
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            border_color=("orange","#FFCC70"),
        )
        self.room_1.grid(row=5, column=1, padx = 10, pady=10)

        self.room_2 = ctk.CTkCheckBox(
            self.frame_2,
            text=f"General Room ({len(general_list)})",
            onvalue=1,
            offvalue=0,
            #checkbox_height=40,
            #checkbox_width=70,
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            border_color=("orange","#FFCC70"),
        )
        self.room_2.grid(row=5, column=2, padx = 10, pady=10)

        self.room_3 = ctk.CTkCheckBox(
            self.frame_2,
            text=f"Joint Room ({len(joint_list)})",
            onvalue=1,
            offvalue=0,
            #checkbox_height=40,
            #checkbox_width=70,
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            border_color=("orange","#FFCC70"),
        )
        self.room_3.grid(row=5, column=3, padx = 10, pady=10)

        payment_label = ctk.CTkLabel(
            master=self.frame_2,
            text="Choose Payment Method:",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 25),
            fg_color=("transparent"),
        )
        payment_label.grid(row=6, column=0, pady=10, padx=15)

        self.payment_method1 = ctk.CTkRadioButton(
            self.frame_2,
            text = "By cash",
            border_color = ("orange","#FFCC70"),
            text_color = ("orange","#FFCC70"),
            font=("times new roman", 20),
            variable = self.radio_var,
            value = 1
        )
        self.payment_method1.grid(row = 6, column = 1, padx = 10, pady=10)

        self.payment_method1 = ctk.CTkRadioButton(
            self.frame_2,
            text = "By credit card/debit card",
            border_color = ("orange","#FFCC70"),
            text_color = ("orange","#FFCC70"),
            font=("times new roman", 20),
            variable = self.radio_var,
            value = 2
        )
        self.payment_method1.grid(row = 6, column = 2, padx = 10, pady=10)

        submit_button = ctk.CTkButton(
            master=self.frame_2,
            command=self.submit,
            text_color=("black", "white"),
            image=check_in_icon,
            border_color=("orange","#FFCC70"),
            border_width=2,
            #fg_color=("transparent"),
            #hover_color="#FFBF70",
            corner_radius=0,
            font=("times new roman", 20),
            text="SUBMIT",
            #height=20,
            width=180,
            anchor = "w"
        )
        submit_button.grid(row=6, column=4, padx=(30,0), pady=0, sticky="news")

        self.textbox = ctk.CTkTextbox(
            self,
            border_width = 2,
            border_color = ("orange","#FFCC70"),
            text_color = ("orange","#FFCC70"),
            font=("times new roman", 30),
            scrollbar_button_hover_color = ("orange","#FFCC70"),
            wrap = "word",
            state = "disabled"
        )
        self.textbox.grid(row = 8,columnspan = 6,padx = 15,pady = (0,10),sticky = "news")

    def check_out(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        png_1 = Image.open("upload.png")
        check_in_icon = ctk.CTkImage(light_image=png_1, dark_image=png_1, size=(30, 30))
        png_5 = Image.open("back.png")
        exit_icon = ctk.CTkImage(light_image=png_5, dark_image=png_5, size=(40, 40))
        ctk.set_default_color_theme("green")
        self.grid_rowconfigure((0,1,2,3,4,5,6,7),weight = 1)
        self.grid_columnconfigure((0,1,2,3,4),weight = 1)
        self.frame_3 = ctk.CTkFrame(
            master=self, height=20, border_width=2, border_color=("orange","#FFCC70")
        )
        self.frame_3.grid(row=0, column=0,rowspan = 7,columnspan = 5, padx=15, pady=(15,5), sticky="news")

        return_button = ctk.CTkButton(
            master=self.frame_3,
            command = self.back,
            image=exit_icon,
            text_color=("black", "white"),
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("red"),
            hover_color="darkred",
            corner_radius=0,
            font=("times new roman", 20),
            text="RETURN",
            #height=103,
            width=290,
        )
        return_button.grid(row=0, column=0, pady=(25,15), padx=(0,15),sticky = "ews")

        check_out_label = ctk.CTkLabel(
            master=self.frame_3,
            text="CHECK OUT",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 50),
            fg_color=("transparent"),
        )
        check_out_label.grid(row=0, column=3, pady=10, padx=5)

        room_entry_label = ctk.CTkLabel(
            master=self.frame_3,
            text="Enter Room No:",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 25),
            fg_color=("transparent"),
        )
        room_entry_label.grid(row=1, column=2, pady=10, padx=5)

        self.room_entry = ctk.CTkEntry(
            self.frame_3,
            width=450,
            height=50,
            placeholder_text="Enter Room No",
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            placeholder_text_color=("orange","#FFCC70"),
            border_width=2,
            border_color=("orange","#FFCC70"),
            corner_radius=0
        )
        self.room_entry.grid(row=1, column=3, pady=10, padx=(5,0))
        self.room_entry.bind("<Return>",self.remove_guest)

        submit_button = ctk.CTkButton(
            master=self.frame_3,
            command=self.remove_guest,
            #text_color=("black", "white"),
            image=check_in_icon,
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("transparent"),
            hover_color=("orange","#FFCC70"),
            corner_radius=0,
            font=("times new roman", 20),
            text="",
            height=50,
            width=50,
        )
        submit_button.grid(row=1, column=4, padx=(0,0), pady=0, sticky="w")

        self.textbox = ctk.CTkTextbox(
            self,
            border_width = 2,
            border_color = ("orange","#FFCC70"),
            text_color = ("orange","#FFCC70"),
            font=("times new roman", 30),
            scrollbar_button_hover_color = ("orange","#FFCC70"),
            wrap = "word",
            state = "disabled"
        )
        self.textbox.grid(row = 7,rowspan = 2,columnspan = 5,padx = 15,pady = (0,10),sticky = "news")

    def guest_list(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        png_5 = Image.open("back.png")
        exit_icon = ctk.CTkImage(light_image=png_5, dark_image=png_5, size=(40, 40))
        ctk.set_default_color_theme("green")
        self.grid_rowconfigure((0,1,2,3,4,5,6,7),weight = 1)
        self.grid_columnconfigure((0,1,2,3,4),weight = 1)
        self.frame_4 = ctk.CTkFrame(
            master=self, height=20, border_width=2, border_color=("orange","#FFCC70")
        )
        self.frame_4.grid(row=0, column=0,columnspan = 5, padx=15, pady=(15,5), sticky="news")

        return_button = ctk.CTkButton(
            master=self.frame_4,
            command = self.back,
            image=exit_icon,
            text_color=("black", "white"),
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("red"),
            hover_color="darkred",
            corner_radius=0,
            font=("times new roman", 20),
            text="RETURN",
            #height=103,
            width=290,
        )
        return_button.grid(row=0, column=0, pady=(25,15), padx=(0,15),sticky = "ews")

        guest_list_label = ctk.CTkLabel(
            master=self.frame_4,
            text="LIST OF ALL GUESTS",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 50),
            fg_color=("transparent"),
        )
        guest_list_label.grid(row=0, column=3, pady=10, padx=100, sticky = "e")

        self.textbox_1 = ctk.CTkTextbox(
            self,
            border_width = 2,
            border_color = ("orange","#FFCC70"),
            text_color = ("orange","#FFCC70"),
            font=("times new roman", 30),
            scrollbar_button_hover_color = ("orange","#FFCC70"),
            wrap = "word"
        )
        self.textbox_1.grid(row = 1,rowspan = 8,columnspan = 3,padx = (15,0),pady = (0,10),sticky = "news")

        self.textbox_2 = ctk.CTkTextbox(
            self,
            border_width = 2,
            border_color = ("orange","#FFCC70"),
            text_color = ("orange","#FFCC70"),
            font=("times new roman", 30),
            scrollbar_button_hover_color = ("orange","#FFCC70"),
            wrap = "word"
        )
        self.textbox_2.grid(row = 1,column = 3,rowspan = 8,columnspan = 2,padx = (0,15),pady = (0,10),sticky = "news")

        self.textbox_1.insert("0.0","GUEST NAME".center(80) + "\n")
        self.textbox_2.insert("0.0","ROOM NO".center(50) + "\n")
        row = self.list_all()
        count = 1
        for i in row:
            self.textbox_1.insert("end",str(count) + "." + str(i[0]) + "\n")
            self.textbox_2.insert("end",str(count) + "." + "Room No." + str(i[2]) + "\n")
            count += 1
        self.textbox_1.configure(state = "disabled")
        self.textbox_2.configure(state = "disabled")

    def guest_info(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        png_1 = Image.open("magnifying-glass.png")
        check_in_icon = ctk.CTkImage(light_image=png_1, dark_image=png_1, size=(30, 30))
        png_5 = Image.open("back.png")
        exit_icon = ctk.CTkImage(light_image=png_5, dark_image=png_5, size=(40, 40))
        ctk.set_default_color_theme("green")
        self.grid_rowconfigure((0,1,2,3,4,5,6,7),weight = 1)
        self.grid_columnconfigure((0,1,2,3,4),weight = 1)
        self.frame_5 = ctk.CTkFrame(
            master=self, height=20, border_width=2, border_color=("orange","#FFCC70")
        )
        self.frame_5.grid(row=0, column=0,rowspan = 7,columnspan = 5, padx=15, pady=(15,5), sticky="news")

        return_button = ctk.CTkButton(
            master=self.frame_5,
            command = self.back,
            image=exit_icon,
            text_color=("black", "white"),
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("red"),
            hover_color="darkred",
            corner_radius=0,
            font=("times new roman", 20),
            text="RETURN",
            #height=103,
            width=290,
        )
        return_button.grid(row=0, column=0, pady=(25,15), padx=(0,15),sticky = "ews")

        guest_info_label = ctk.CTkLabel(
            master=self.frame_5,
            text="GUEST INFO",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 50),
            fg_color=("transparent"),
        )
        guest_info_label.grid(row=0, column=3, pady=10, padx=5)

        room_entry_label = ctk.CTkLabel(
            master=self.frame_5,
            text="Enter Room No:",
            text_color=("orange","#FFCC70"),
            font=("times new roman", 25),
            fg_color=("transparent"),
        )
        room_entry_label.grid(row=1, column=2, pady=10, padx=5)

        self.room_entry = ctk.CTkEntry(
            self.frame_5,
            width=450,
            height=50,
            placeholder_text="Enter Room No",
            font=("times new roman", 20),
            text_color=("orange","#FFCC70"),
            placeholder_text_color=("orange","#FFCC70"),
            border_width=2,
            border_color=("orange","#FFCC70"),
            corner_radius=0
        )
        self.room_entry.grid(row=1, column=3, pady=10, padx=(5,0))
        self.room_entry.bind("<Return>",self.search_guest)

        submit_button = ctk.CTkButton(
            master=self.frame_5,
            command=self.search_guest,
            #text_color=("black", "white"),
            image=check_in_icon,
            border_color=("orange","#FFCC70"),
            border_width=2,
            fg_color=("transparent"),
            hover_color=("orange","#FFCC70"),
            corner_radius=0,
            font=("times new roman", 20),
            text="",
            height=50,
            width=50,
        )
        submit_button.grid(row=1, column=4, padx=(0,0), pady=0, sticky="w")

        self.textbox = ctk.CTkTextbox(
            self,
            border_width = 2,
            border_color = ("orange","#FFCC70"),
            text_color = ("orange","#FFCC70"),
            font=("times new roman", 30),
            scrollbar_button_hover_color = ("orange","#FFCC70"),
            wrap = "word",
            state = "disabled"
        )
        self.textbox.grid(row = 7,rowspan = 2,columnspan = 5,padx = 15,pady = (0,10),sticky = "news")

    def exit(self):
        quit()

    def password_window(self):
        if HMS.dialog is None or not HMS.dialog.winfo_exists():
            HMS.dialog = ctk.CTkToplevel(self.frame_1)
            ctk.set_default_color_theme("green")
            HMS.dialog.title("Authentication")

            self.password_entry = ctk.CTkEntry(
                master = HMS.dialog,
                #show = "*",
                placeholder_text = "Enter Password",
                placeholder_text_color = ("orange","#FFCC70"),
                text_color = ("orange","#FFCC70"),
                font=("times new roman",20),
                border_width = 2,
                border_color = ("orange","#FFCC70"),
                width = 200
            )
            self.password_entry.pack(padx=55,pady=15,anchor="center")
            self.password_entry.bind("<Return>",self.password_button)

            def focus_entry(event=None):
                HMS.dialog.focus()
                HMS.dialog.bind("<Key>",self.focus_in)

            HMS.dialog.bind("<Map>",focus_entry)

            password_button = ctk.CTkButton(
                HMS.dialog,
                command = self.password_button,
                text = "OK",
                font=("times new roman",20),
            )
            password_button.pack(padx=55,pady=(0,15),anchor="center")
        else:
            HMS.dialog.focus()

    def focus_in(self,event=None):
        self.password_entry.focus()


    def password_button(self,event=None):
        if self.password_entry.get():
            if self.password_entry.get() == "1234":
                HMS.dialog.destroy()
                self.guest_info()
            elif self.password_entry.get() == "Enter Password":
                self.password_entry.delete("0","end")
                self.password_entry.insert("0","Enter Password")
            elif self.password_entry.get() == "! Invalid Password":
                self.password_entry.delete("0","end")
                self.password_entry.insert("0","Enter Password")
            else:
                self.password_entry.delete("0","end")
                self.password_entry.insert("0","! Invalid Password")
        else:
            self.password_entry.delete("0","end")
            self.password_entry.insert("0","Enter Password")

    def resize(self,event=None):
        if self.attributes("-fullscreen"):
            self.attributes("-fullscreen",False)
        else:
            self.attributes("-fullscreen",True)

    def back(self,event=None):
        for widget in self.winfo_children():
            widget.grid_forget()
        self.frame_1.pack(padx=15, pady=15, fill="both", expand=True)
        for widget in self.frame_1.winfo_children():
            widget.pack()

    def submit(self):
        self.textbox.configure(state="normal")
        if self.name_entry.get() and \
            self.address_entry.get() and \
            self.phone_entry.get() and \
            self.days_entry.get() and \
            self.address_entry.get() and\
            (self.room_1.get()==1 or\
            self.room_2.get()==1 or\
            self.room_3.get()==1) and\
            (self.radio_var.get()==1 or\
            self.radio_var.get()==2):

            if self.room_1.get() == 1:
                if self.radio_var.get() == 1:
                    room_no = deluxe_list.pop(0)
                    self.cursor.execute("INSERT INTO GUESTS_LIST\
                                    (NAME, ADDRESS, P_NUMBER,ROOM_NO,NO_OF_DAYS,TYPE_OF_ROOM, PAYMENT)\
                                   VALUES (?, ?, ?, ?, ? ,?,?)",
                    (self.name_entry.get(),self.address_entry.get(),self.phone_entry.get(),str(room_no),
                    self.days_entry.get(),"DELUXE","BY CASH"))
                    payment = 4000 * int(self.days_entry.get())
                    self.connect.commit()
                    self.textbox.insert("end",f"Your room no is {room_no} of type DELUXE and Your Total Payment is {payment} \n")
                if self.radio_var.get() == 2:
                    room_no = deluxe_list.pop(0)
                    self.cursor.execute("INSERT INTO GUESTS_LIST\
                                    (NAME, ADDRESS, P_NUMBER,ROOM_NO,NO_OF_DAYS,TYPE_OF_ROOM, PAYMENT)\
                                   VALUES (?, ?, ?, ?, ? ,?,?)",
                    (self.name_entry.get(),self.address_entry.get(),self.phone_entry.get(),str(room_no),
                    self.days_entry.get(),"DELUXE","BY CREDIT/DEBIT CARD"))
                    payment = 4000 * int(self.days_entry.get())
                    self.connect.commit()
                    self.textbox.insert("end",f"Your room no is {room_no} of type DELUXE and Your Total Payment is {payment} \n")
            if self.room_2.get() == 1:
                if self.radio_var.get() == 1:
                    room_no = general_list.pop(0)
                    self.cursor.execute("INSERT INTO GUESTS_LIST\
                                    (NAME, ADDRESS, P_NUMBER,ROOM_NO,NO_OF_DAYS,TYPE_OF_ROOM, PAYMENT)\
                                   VALUES (?, ?, ?, ?, ? ,?,?)",
                    (self.name_entry.get(),self.address_entry.get(),self.phone_entry.get(),str(room_no),
                    self.days_entry.get(),"GENERAL","BY CASH"))
                    payment = 3000 * int(self.days_entry.get())
                    self.connect.commit()
                    self.textbox.insert("end",f"Your room no is {room_no} of type GENERAL and Your Total Payment is {payment} \n")
                if self.radio_var.get() == 2:
                    room_no = general_list.pop(0)
                    self.cursor.execute("INSERT INTO GUESTS_LIST\
                                    (NAME, ADDRESS, P_NUMBER,ROOM_NO,NO_OF_DAYS,TYPE_OF_ROOM, PAYMENT)\
                                   VALUES (?, ?, ?, ?, ? ,?,?)",
                    (self.name_entry.get(),self.address_entry.get(),self.phone_entry.get(),str(room_no),
                    self.days_entry.get(),"GENERAL","BY CREDIT/DEBIT CARD"))
                    payment = 3000 * int(self.days_entry.get())
                    self.connect.commit()
                    self.textbox.insert("end",f"Your room no is {room_no} of type GENERAL and Your Total Payment is {payment} \n")
            if self.room_3.get() == 1:
                if self.radio_var.get() == 1:
                    room_no = joint_list.pop(0)
                    self.cursor.execute("INSERT INTO GUESTS_LIST\
                                    (NAME, ADDRESS, P_NUMBER,ROOM_NO,NO_OF_DAYS,TYPE_OF_ROOM, PAYMENT)\
                                   VALUES (?, ?, ?, ?, ? ,?,?)",
                    (self.name_entry.get(),self.address_entry.get(),self.phone_entry.get(),str(room_no),
                    self.days_entry.get(),"JOINT","BY CASH"))
                    payment = 2000 * int(self.days_entry.get())
                    self.connect.commit()
                    self.textbox.insert("end",f"Your room no is {room_no} of type JOINT and Your Total Payment is {payment} \n")
                if self.radio_var.get() == 2:
                    room_no = joint_list.pop(0)
                    self.cursor.execute("INSERT INTO GUESTS_LIST\
                                    (NAME, ADDRESS, P_NUMBER,ROOM_NO,NO_OF_DAYS,TYPE_OF_ROOM, PAYMENT)\
                                   VALUES (?, ?, ?, ?, ? ,?,?)",
                    (self.name_entry.get(),self.address_entry.get(),self.phone_entry.get(),str(room_no),
                    self.days_entry.get(),"JOINT","BY CREDIT/DEBIT CARD"))
                    payment = 2000 * int(self.days_entry.get())
                    self.connect.commit()
                    self.textbox.insert("end",f"Your room no is {room_no} of type JOINT and Your Total Payment is {payment} \n")

            self.textbox.insert("end",f"!Submission Successfull.\n")
        else:
            self.textbox.insert("0.0","!INCOMPLETE DATA.\n")
        self.textbox.configure(state="disabled")

    def remove_guest(self,event=None):
        self.textbox.configure(state="normal")
        if self.room_entry.get():
            a = self.room_entry.get()
            re = self.cursor.execute("SELECT * FROM GUESTS_LIST WHERE ROOM_NO=?",(a,))
            room_type = self.cursor.execute("SELECT TYPE_OF_ROOM FROM GUESTS_LIST WHERE ROOM_NO=?",(a,))
            count = 0
            for r in re:
                if r:
                    count += 1
            if count != 0:
                self.cursor.execute("DELETE FROM GUESTS_LIST WHERE ROOM_NO=?",(a,))
                self.connect.commit()
                self.textbox.insert("0.0","Successfully Checked Out.\n")
                if room_type == "DELUXE":
                    deluxe_list.append(int(a))
                elif room_type == "GENERAL":
                    general_list.append(int(a))
                else:
                    joint_list.append(int(a))
            else:
                self.textbox.insert("0.0","This room no is not in our list.\n")
        else:
            self.textbox.insert("0.0","Enter the room no to check out.\n")
        self.textbox.configure(state="disabled")

    def list_all(self):
        row = self.cursor.execute("SELECT NAME , P_NUMBER,ROOM_NO FROM GUESTS_LIST")
        return row

    def search_guest(self,event=None):
        self.textbox.configure(state="normal")
        if self.room_entry.get():
            row = self.cursor.execute("SELECT NAME,ADDRESS,P_NUMBER,NO_OF_DAYS,TYPE_OF_ROOM,PAYMENT FROM GUESTS_LIST WHERE ROOM_NO = ?",(self.room_entry.get(),))
            for i in row:
                self.textbox.insert("0.0", f"NAME : {i[0]}             ADDRESS : {i[1]}          PHONE NUMBER : {i[2]} \n\
NO OF DAYS : {i[3]}  TYPE OF ROOM : {i[4]}       PAYMENT METHOD : {i[5]}\n")
                self.textbox.insert("end","Search successful.\n")
        else:
            self.textbox.insert("0.0","Enter the room no to get info.\n")
        self.textbox.configure(state="disabled")

def main():
    HMS().mainloop()


if __name__ == "__main__":
    main()
