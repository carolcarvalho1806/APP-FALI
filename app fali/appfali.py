import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


janela = customtkinter.CTk()
import os
caminho_icone = os.path.join(os.path.dirname(__file__), "icone.ico")
if os.path.exists(caminho_icone):
    janela.iconbitmap(caminho_icone)
janela.title("Quadro de Comunicação")
janela.geometry("800x650")

tamanho_letra = 50  

def falar_fome():
    visor.configure(text="Estou com fome")

def falar_sede():
    visor.configure(text="Estou com sede")

def falar_banheiro():
    visor.configure(text="Preciso ir ao banheiro")

def falar_sim():
    visor.configure(text="SIM")

def falar_nao():
    visor.configure(text="NÃO")

def falar_ajuda():
    visor.configure(text="Preciso de ajuda!")

def mostrar_frase():
    frase = entrada.get()
    if frase == "":
        visor.configure(text="Digite uma frase primeiro!")
    else:
        visor.configure(text=frase)
        entrada.delete(0, "end")

def aumentar():
    global tamanho_letra
    if tamanho_letra < 120:
        tamanho_letra = tamanho_letra + 10
        visor.configure(font=("Arial", tamanho_letra))
        info_tamanho.configure(text="Letra: " + str(tamanho_letra))

def diminuir():
    global tamanho_letra
    if tamanho_letra > 20:
        tamanho_letra = tamanho_letra - 10
        visor.configure(font=("Arial", tamanho_letra))
        info_tamanho.configure(text="Letra: " + str(tamanho_letra))

def trocar_tema():
    tema_atual = customtkinter.get_appearance_mode()
    if tema_atual == "Dark":
        customtkinter.set_appearance_mode("light")
        btn_tema.configure(text="Modo escuro")
    else:
        customtkinter.set_appearance_mode("dark")
        btn_tema.configure(text="Modo claro")

frame_barra = customtkinter.CTkFrame(master=janela)
frame_barra.pack(padx=10, pady=10, fill="x")

btn_diminuir = customtkinter.CTkButton(master=frame_barra, text="A-", width=60, height=50,
                                       font=("Arial", 22), command=diminuir, 
                                       fg_color="#6d00a1", hover_color="#960cd6", text_color="white")
btn_diminuir.pack(side="left", padx=5, pady=10)

btn_aumentar = customtkinter.CTkButton(master=frame_barra, text="A+", width=60, height=50,
                                       font=("Arial", 22), command=aumentar, 
                                       fg_color="#6d00a1", hover_color="#960cd6", text_color="white")
btn_aumentar.pack(side="left", padx=5, pady=10)

info_tamanho = customtkinter.CTkLabel(master=frame_barra, text="Letra: 50", font=("Arial", 20))
info_tamanho.pack(side="left", padx=15)

btn_tema = customtkinter.CTkButton(master=frame_barra, text="Modo claro", height=50,
                                   font=("Arial", 20), command=trocar_tema, 
                                   fg_color="#6d00a1", hover_color="#960cd6", text_color="white")
btn_tema.pack(side="right", padx=10, pady=10)

frame_visor = customtkinter.CTkFrame(master=janela, fg_color=("white", "black"))  
frame_visor.pack(padx=10, pady=10, fill="both", expand=True)

visor = customtkinter.CTkLabel(master=frame_visor, text="Clique em um botão",
                               font=("Arial", tamanho_letra), wraplength=700,
                               text_color=("black", "white"))  
visor.pack(padx=20, pady=20, fill="both", expand=True)

frame_necessidades = customtkinter.CTkFrame(master=janela, fg_color="transparent")
frame_necessidades.pack(padx=10, pady=5, fill="x")

btn_fome = customtkinter.CTkButton(master=frame_necessidades, text="Fome", height=70,
                                   font=("Arial", 24), fg_color="#4b0081", hover_color="#6d13b0", 
                                   text_color="white", command=falar_fome)
btn_fome.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_sede = customtkinter.CTkButton(master=frame_necessidades, text="Sede", height=70, 
                                   font=("Arial", 24), fg_color="#56008c", hover_color="#7817b8", 
                                   text_color="white", command=falar_sede)
btn_sede.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_banheiro = customtkinter.CTkButton(master=frame_necessidades, text="Banheiro", height=70,
                                       font=("Arial", 24), fg_color="#620096", hover_color="#8423c2", 
                                       text_color="white", command=falar_banheiro)
btn_banheiro.pack(side="left", padx=5, pady=5, expand=True, fill="x")

frame_respostas = customtkinter.CTkFrame(master=janela, fg_color="transparent")
frame_respostas.pack(padx=10, pady=5, fill="x")

btn_sim = customtkinter.CTkButton(master=frame_respostas, text="Sim", height=70,
                                  font=("Arial", 24), fg_color="#7900ac", hover_color="#9c27cc", 
                                  text_color="white", command=falar_sim)
btn_sim.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_nao = customtkinter.CTkButton(master=frame_respostas, text="Não", height=70,
                                  font=("Arial", 24), fg_color="#af69cd", hover_color="#c892e2", 
                                  text_color="white", command=falar_nao)
btn_nao.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_ajuda = customtkinter.CTkButton(master=frame_respostas, text="Ajuda!", height=70,
                                    font=("Arial", 24), fg_color="#9032bb", hover_color="#b256db", 
                                    text_color="white", command=falar_ajuda)
btn_ajuda.pack(side="left", padx=5, pady=5, expand=True, fill="x")

frame_frase = customtkinter.CTkFrame(master=janela)
frame_frase.pack(padx=10, pady=10, fill="x")

entrada = customtkinter.CTkEntry(master=frame_frase, height=50, font=("Arial", 24),
                                 placeholder_text="Escreva sua frase...")
entrada.pack(side="left", padx=10, pady=10, fill="x", expand=True)

btn_mostrar = customtkinter.CTkButton(master=frame_frase, text="Mostrar", height=50, 
                                      font=("Arial", 22), fg_color="#6d00a1", hover_color="#960cd6", 
                                      text_color="white", command=mostrar_frase)
btn_mostrar.pack(side="right", padx=10, pady=10)

janela.mainloop()