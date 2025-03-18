import customtkinter as ctt
import tools

class App(ctt.CTk):
    def __init__(self, title, size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(title)
        self.resizable(False, False)
        self.geometry(f"{size[0]}x{size[1]}+{self.winfo_screenwidth()//2-size[0]//2}+{self.winfo_screenheight()//2-size[1]//2}")
        
        self.createWidgets()
        
    def createWidgets(self):
        equalyDivision = 1/4
        decrementLabel = 0.08
        
        autorLabel = ctt.CTkLabel(self, text="Autor da Música")
        autorLabel.place(relx=0.5, rely=equalyDivision-decrementLabel, anchor="center")
        
        self.autorVar = ctt.StringVar(value="oi")
        autorInput = ctt.CTkEntry(self, placeholder_text="Digite o autor", textvariable=self.autorVar)
        autorInput.place(relx=0.5, rely=equalyDivision, anchor="center")
        
        musicLabel = ctt.CTkLabel(self, text="Autor da Música")
        musicLabel.place(relx=0.5, rely=equalyDivision*2-decrementLabel, anchor="center")
        
        self.musicVar = ctt.StringVar(value="oi")
        musicInput = ctt.CTkEntry(self, placeholder_text="Digite o autor", textvariable=self.musicVar)
        musicInput.place(relx=0.5, rely=equalyDivision*2, anchor="center")
        
        submitButton = ctt.CTkButton(self, text="Pesquisar", height=40, width=150, command=self.validateInputs)
        submitButton.place(relx=0.5, rely=equalyDivision*3, anchor="center")
    
    def validateInputs(self):
        music = self.musicVar.get()
        autor = self.autorVar.get()
        
        if  music == "" or autor == "":
            return
        
        tools.openBrowser(tools.searchGoogle(f"{autor}/{music}"))
        

app = App("Pesquisador de música", (400, 400))
app.mainloop()