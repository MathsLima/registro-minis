import tkinter as tk

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

        #inicia a tela inicial com o menu
        self.tela_inicial()
    
    #funcao para alterar as paginas
    def muda_janela(self):
        for widget in self.container_principal.winfo_children():
            widget.destroy()
    

    #tela inicial com o menu
    def tela_inicial(self):
        self.muda_janela()

        label_tela_inicial = tk.Label(self.container_principal, text="Sistema de Cadastro de Miniaturas", font=('Calibri', 13))
        label_tela_inicial.place(width=250, height=40, x=25, y=10)

        botao_pagina_1 = tk.Button(self.container_principal, text="Ir para Nova Página 1", command=self.pagina_1)
        botao_pagina_1.place(width=200, height=40, x=50, y=60)

        botao_pagina_2 = tk.Button(self.container_principal, text="Ir para Nova Página 2", command=self.pagina_2)
        botao_pagina_2.place(width=200, height=40, x=50, y=110)

        botao_pagina_3 = tk.Button(self.container_principal, text="Ir para Nova Página 3", command=self.pagina_3)
        botao_pagina_3.place(width=200, height=40, x=50, y=160)



    def pagina_1(self):
        self.muda_janela()

        pagina_1 = tk.Label(self.container_principal, text="Página 1!")
        pagina_1.pack()

        botao_voltar = tk.Button(self.container_principal, text="Voltar à Tela Inicial", command=self.tela_inicial)
        botao_voltar.pack(pady=10)

    def pagina_2(self):
        self.muda_janela()
        
        pagina_2 = tk.Label(self.container_principal, text="Página 2!")
        pagina_2.pack()

        botao_voltar = tk.Button(self.container_principal, text="Voltar à Tela Inicial", command=self.tela_inicial)
        botao_voltar.pack(pady=20)

    def pagina_3(self):
        self.muda_janela()
        
        pagina_3 = tk.Label(self.container_principal, text="Página 3!")
        pagina_3.pack()

        botao_voltar = tk.Button(self.container_principal, text="Voltar à Tela Inicial", command=self.tela_inicial)
        botao_voltar.pack(pady=30)


#inicia a aplicacao
root = tk.Tk()
app = App(root)
root.mainloop()
