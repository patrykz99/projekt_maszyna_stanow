import customtkinter


class GUI:
    def __init__(self):
        self.ticket_machine = customtkinter.CTk()
        self.ticket_machine.title("Ticket Machine APP")
        self.ticket_machine.geometry("400x300")  # wymiary okna
        self.ticket_machine._set_appearance_mode("light")

        # siatka 2x2
        self.ticket_machine.grid_rowconfigure((0, 1), weight=1)
        self.ticket_machine.grid_columnconfigure((0, 1), weight=1)

    def display(self):
        return self.ticket_machine.mainloop()

    def create_buttons(self):
        # przycis bilet normalny
        button_norm = customtkinter.CTkButton(
            self.ticket_machine,
            text="Bilet normalny",
            height=50,
            text_color="#000000",
            hover_color="#0c6d09",
            corner_radius=7,
            fg_color="#ffffff",
            bg_color="#92a3f6",
        )
        button_norm.grid(row=1, column=0)
        # przycisk bilet ulgowys
        button_ulg = customtkinter.CTkButton(
            self.ticket_machine,
            text="Bilet ulgowy",
            height=50,
            text_color="#ffffff",
            hover_color="#0c6d09",
            corner_radius=7,
            fg_color="#000000",
            bg_color="#92a3f6",
        )
        button_ulg.grid(row=1, column=1)

    def create_frames(self):
        # top frame with text
        top_frame = customtkinter.CTkFrame(
            self.ticket_machine, corner_radius=0, fg_color="#92a3f6"
        )
        top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        text = customtkinter.CTkLabel(
            self.ticket_machine,
            text="Wybierz bilet",
            width=300,
            height=50,
            font=("Arial", 16),
            corner_radius=10,
            text_color="black",
        )
        text.grid(row=0, column=0, columnspan=2)
        # bottom frame contains buttons
        bottom_frame = customtkinter.CTkFrame(
            self.ticket_machine, corner_radius=0, fg_color="#92a3f6"
        )
        bottom_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
import customtkinter, time
import tkinter as tk


class GUI():
    def __init__(self):
        self.ticket_machine = customtkinter.CTk()
        self.ticket_machine.title("Ticket Machine APP")
        self.ticket_machine.geometry("400x300") #wymiary okna
        self.ticket_machine._set_appearance_mode("light")
        self.ticket_machine.config(bg="#92a3f6")  # Ustawienie koloru tła dla całego okna
        
        
        #siatka 2x2
        self.ticket_machine.grid_rowconfigure((0,1), weight=1)
        self.ticket_machine.grid_columnconfigure((0, 1), weight=1)
        
        # Tworzenie etykiety do wyświetlania wybranego biletu
        self.selection_label = customtkinter.CTkLabel(self.ticket_machine, text="", width=300, height=50, font=("Arial",16), corner_radius=10, text_color="black")
        self.selection_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        #top frame with text
        top_frame = customtkinter.CTkFrame(self.ticket_machine,corner_radius=0,fg_color="#92a3f6")
        top_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
        text = customtkinter.CTkLabel(self.ticket_machine, text="Wybierz bilet",width=300,height=50,font=("Arial",16),corner_radius=10, text_color="black")
        text.grid(row=0,column=0,columnspan=2)
        #bottom frame contains buttons
        bottom_frame=customtkinter.CTkFrame(self.ticket_machine,corner_radius=0,fg_color="#92a3f6")
        bottom_frame.grid(row=1,column=0,columnspan=2,sticky="nsew")

        # Tworzenie przycisków
        self.button_norm = customtkinter.CTkButton(self.ticket_machine, text="Bilet normalny", height=50, text_color="#000000", hover_color="#0c6d09", corner_radius=7, fg_color="#ffffff", bg_color="#92a3f6",
                                                   command=self.select_normalny_bilet)
        self.button_norm.grid(row=1, column=0)
        
        self.button_ulg = customtkinter.CTkButton(self.ticket_machine, text="Bilet ulgowy", height=50, text_color="#ffffff", hover_color="#0c6d09", corner_radius=7, fg_color="#000000", bg_color="#92a3f6",
                                                  command=self.select_ulgowy_bilet)
        self.button_ulg.grid(row=1, column=1)
    
    def select_normalny_bilet(self):
        self.clear_window()
        self.selection_label = customtkinter.CTkLabel(self.ticket_machine, text="Wybrano bilet normalny", width=300, height=50, font=("Arial",16), corner_radius=10, text_color="#000000")
        self.selection_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.price_label = customtkinter.CTkLabel(self.ticket_machine, text="Do zapłaty: 3 zł", width=300, height=50, font=("Arial",16), corner_radius=10, text_color="#000000")
        self.price_label.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.button_cancel = customtkinter.CTkButton(self.ticket_machine, text="Anuluj", height=50, text_color="#ffffff", hover_color="#c60b0b", corner_radius=7, fg_color="#000000", bg_color="#92a3f6",
                                             command=self.cancel_purchase)
        self.button_cancel.grid(row=2, column=0,columnspan=2)
        
        price = 3  # Cena biletu normalnego
        #obsluga monet
        result = self.sum_monety(price)
        if result[2] == True:
            self.print_ticket()
        
    
    def select_ulgowy_bilet(self):
        self.clear_window()
        self.selection_label = customtkinter.CTkLabel(self.ticket_machine, text="Wybrano bilet ulgowy", width=300, height=50, font=("Arial",16), corner_radius=10, text_color="#000000")
        self.selection_label.grid(row=0, column=0, columnspan=2, pady=20)
    
        self.price_label = customtkinter.CTkLabel(self.ticket_machine, text="Do zapłaty: 2 zł", width=300, height=50, font=("Arial",16), corner_radius=10, text_color="#000000")
        self.price_label.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.button_cancel = customtkinter.CTkButton(self.ticket_machine, text="Anuluj transakcje", height=50, text_color="#ffffff", hover_color="#c60b0b", corner_radius=7, fg_color="#000000", bg_color="#92a3f6",
                                             command=self.cancel_purchase)
        self.button_cancel.grid(row=2, column=0,columnspan=2)
        
        price = 2  # Cena biletu ulgowego
        #obsluga monet
        result = self.sum_monety(price)
        if result[2] == True:
            self.print_ticket()
        
    #funkcja sum 
    def sum_monety(self,price):
        sum = 0
        while True:
            num = int(input("Wrzuc monete: "))
            sum += num
            if sum >= price:
                if sum > price:
                    print(f'Wrzucona ilosc: {sum}, Reszta do wydania: ')
                return sum, sum - price, True
            else:
                print(f'Pozostało do wrzucenia: {price-sum} zł')
    def cancel_purchase(self):
        self.clear_window()
        self.selection_label = customtkinter.CTkLabel(self.ticket_machine, text="Zakup został anulowany", width=300, height=50, font=("Arial", 16), corner_radius=10, text_color="#000000")
        self.selection_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        #dodanie ze po 5 sekundach sie zamyka program
        self.ticket_machine.after(5000, self.ticket_machine.destroy)

    def print_ticket(self):
        #wydruk biletu
        self.clear_window()
        self.selection_label = customtkinter.CTkLabel(self.ticket_machine, text="Wydruk biletu",
                                                      width=300, height=50, font=("Arial", 16,"bold"), corner_radius=10,
                                                      text_color="#000000")
        self.selection_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        time.sleep(3)
        self.selection_label = customtkinter.CTkLabel(self.ticket_machine, text="W trakcie...",
                                                      width=300, height=50, font=("Arial", 16, "bold"),
                                                      corner_radius=10, text_color="#000000")
        self.selection_label.grid(row=1, column=0, columnspan=2, pady=20)
            
    def clear_window(self):
        for widget in self.ticket_machine.winfo_children():
            widget.destroy()
    
    def display(self):
        return self.ticket_machine.mainloop()   




    