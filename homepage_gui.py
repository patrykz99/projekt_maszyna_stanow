import customtkinter  


class GUI():
    def __init__(self):
        self.ticket_machine = customtkinter.CTk()
        self.ticket_machine.title("Ticket Machine APP")
        self.ticket_machine.geometry("400x300") #wymiary okna
        self.ticket_machine._set_appearance_mode("light")
        
        #siatka 2x2
        self.ticket_machine.grid_rowconfigure((0,1), weight=1)
        self.ticket_machine.grid_columnconfigure((0, 1), weight=1)
    def display(self):
        return self.ticket_machine.mainloop()
    def create_buttons(self):
        #przycis bilet normalny
        button_norm = customtkinter.CTkButton(self.ticket_machine,text="Bilet normalny",height=50,text_color="#000000",hover_color="#0c6d09",corner_radius=7,fg_color="#ffffff",bg_color="#92a3f6")
        button_norm.grid(row=1, column=0)
        #przycisk bilet ulgowys
        button_ulg = customtkinter.CTkButton(self.ticket_machine,text="Bilet ulgowy",height=50,text_color="#ffffff",hover_color="#0c6d09",corner_radius=7,fg_color="#000000",bg_color="#92a3f6")
        button_ulg.grid(row=1, column=1)
    def create_frames(self):
        #top frame with text
        top_frame = customtkinter.CTkFrame(self.ticket_machine,corner_radius=0,fg_color="#92a3f6")
        top_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
        text = customtkinter.CTkLabel(self.ticket_machine, text="Wybierz bilet",width=300,height=50,font=("Arial",16),corner_radius=10, text_color="black")
        text.grid(row=0,column=0,columnspan=2)
        #bottom frame contains buttons
        bottom_frame=customtkinter.CTkFrame(self.ticket_machine,corner_radius=0,fg_color="#92a3f6")
        bottom_frame.grid(row=1,column=0,columnspan=2,sticky="nsew")
        
        
        






    
