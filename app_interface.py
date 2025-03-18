import customtkinter as ctt
import CustomTkinterMessagebox as message
import tools

class App(ctt.CTk):
    def __init__(self, title: str, size: tuple[int], *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(title)
        self.resizable(False, False)
        self.geometry(f"{size[0]}x{size[1]}+{self.winfo_screenwidth()//2-size[0]//2}+{self.winfo_screenheight()//2-size[1]//2}")
        
        self.createWidgets()
        
    def createWidgets(self):
        equalyDivision = 1/4
        decrementLabel = 0.1
        inputWidth = 200
        inputHeight = 35
        font = ctt.CTkFont("Montserrat", size=inputHeight//2)
        
        autorLabel = ctt.CTkLabel(self, text="Autor da Música", font=font)
        autorLabel.place(relx=0.5, rely=equalyDivision-decrementLabel, anchor="center")
        
        autorInput = ctt.CTkEntry(self, placeholder_text="Digite o autor...", width=inputWidth, height=inputHeight, font=font)
        autorInput.place(relx=0.5, rely=equalyDivision, anchor="center")
        
        musicLabel = ctt.CTkLabel(self, text="Música", font=font)
        musicLabel.place(relx=0.5, rely=equalyDivision*2-decrementLabel, anchor="center")
        
        musicInput = ctt.CTkEntry(self, placeholder_text="Digite a música...", width=inputWidth, height=inputHeight, font=font)
        musicInput.place(relx=0.5, rely=equalyDivision*2, anchor="center")
        
        submitButton = ctt.CTkButton(self, text="Pesquisar", height=40, width=150, command=lambda: self.validateInputs(musicInput.get(), autorInput.get()))
        submitButton.place(relx=0.5, rely=equalyDivision*3, anchor="center")
    
    def validateInputs(self, music: str, autor: str) -> None:
        if  music == "" or autor == "":
            message.CTkMessagebox.messagebox(title="Inválido", text="Por favor, insira um autor e/ou música", button_text="OK")
            return
        
        tools.openBrowser(tools.searchGoogle(f"{autor}/{music}"))