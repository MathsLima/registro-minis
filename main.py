import tkinter as tk
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'miniaturas',
)
cursor = conexao.cursor()

bg = "#34495E"
letras = "#FDFEFE"

class App:
    #configura o metodo da classe principal
    def __init__(self, root):
        #tela inicial
        self.root = root
        self.root.title('Registro Miniaturas')
        self.root.geometry("300x225")
        self.root.resizable(width=False, height=False)

        #conteiner principal
        self.container_principal = tk.Frame(root)
        self.container_principal.pack(expand=True, fill="both")
        self.container_principal.configure(background=bg  )

        #serve para armazenar o tamanho do menu
        self.tamanho_inicial = "300x225"

        #inicia a tela inicial com o menu
        self.tela_inicial()
    
    #funcao para alterar as paginas
    def muda_janela(self):
        for widget in self.container_principal.winfo_children():
            widget.destroy()
    

    #tela inicial com o menu
    def tela_inicial(self):
        self.muda_janela()

        label_tela_inicial = tk.Label(self.container_principal, text="Sistema de Cadastro de Miniaturas", font=('Calibri', 13), bg=bg, fg=letras )
        label_tela_inicial.place(width=250, height=40, x=25, y=10)

        botao_pagina_1 = tk.Button(self.container_principal, text="Consultar Coleção", command=self.pagina_1)
        botao_pagina_1.place(width=200, height=40, x=50, y=60)

        botao_pagina_2 = tk.Button(self.container_principal, text="Cadastrar Miniatura", command=self.pagina_2)
        botao_pagina_2.place(width=200, height=40, x=50, y=110)

        botao_pagina_3 = tk.Button(self.container_principal,text="Excluir Miniatura", command=self.pagina_3)
        botao_pagina_3.place(width=200, height=40, x=50, y=160)

        #deixa com o menu com o tamanho inicial
        self.root.geometry(self.tamanho_inicial)

    def pagina_1(self):
        self.muda_janela()
        self.root.geometry("600x400")
        
        botao_voltar = tk.Button(self.container_principal, text=" ⬅ Voltar", command=self.tela_inicial)
        botao_voltar.pack(pady=10)

    def pagina_2(self):
        self.muda_janela()
        self.root.geometry("600x400")
        
        botao_voltar = tk.Button(self.container_principal, text="Voltar a Tela Inicial", command=self.tela_inicial)
        botao_voltar.pack(pady=20)

    def pagina_3(self):
        self.muda_janela()
        self.root.geometry("600x400")
        

        botao_voltar = tk.Button(self.container_principal, text="Voltar a Tela Inicial", command=self.tela_inicial)
        botao_voltar.pack(pady=30)


#inicia a aplicacao
root = tk.Tk()
app = App(root)
root.mainloop()
cursor.close()
conexao.close()