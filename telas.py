
import tkinter as tk

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Navegação entre Páginas")

        # Configurar o contêiner principal
        self.contenedor_principal = tk.Frame(root)
        self.contenedor_principal.pack(expand=True, fill="both")

        # Inicializar a tela inicial
        self.tela_inicial()
    
    def limpar_contenedor(self):
        # Limpar qualquer widget existente no contêiner
        for widget in self.contenedor_principal.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_contenedor()

        # Adicionar widgets à tela inicial
        label_tela_inicial = tk.Label(self.contenedor_principal, text="Bem-vindo à tela inicial!")
        label_tela_inicial.pack(pady=20)
        """
        botao_nova_pagina_1 = tk.Button(self.contenedor_principal, text="Ir para Nova Página 1", command=self.nova_pagina_1)
        botao_nova_pagina_1.pack(pady=10)

        botao_nova_pagina_2 = tk.Button(self.contenedor_principal, text="Ir para Nova Página 2", command=self.nova_pagina_2)
        botao_nova_pagina_2.pack(pady=10)

        botao_nova_pagina_3 = tk.Button(self.contenedor_principal, text="Ir para Nova Página 3", command=self.nova_pagina_3)
        botao_nova_pagina_3.pack(pady=10)
        """
"""
    def nova_pagina_1(self):
        self.limpar_contenedor()

        # Adicionar widgets à Nova Página 1
        label_nova_pagina_1 = tk.Label(self.contenedor_principal, text="Esta é a Nova Página 1!")
        label_nova_pagina_1.pack()

        botao_voltar = tk.Button(self.contenedor_principal, text="Voltar à Tela Inicial", command=self.tela_inicial)
        botao_voltar.pack(pady=10)

    def nova_pagina_2(self):
        self.limpar_contenedor()

        # Adicionar widgets à Nova Página 2
        label_nova_pagina_2 = tk.Label(self.contenedor_principal, text="Esta é a Nova Página 2!")
        label_nova_pagina_2.pack()

        botao_voltar = tk.Button(self.contenedor_principal, text="Voltar à Tela Inicial", command=self.tela_inicial)
        botao_voltar.pack(pady=10)

    def nova_pagina_3(self):
        self.limpar_contenedor()

        # Adicionar widgets à Nova Página 3
        label_nova_pagina_3 = tk.Label(self.contenedor_principal, text="Esta é a Nova Página 3!")
        label_nova_pagina_3.pack()

        botao_voltar = tk.Button(self.contenedor_principal, text="Voltar à Tela Inicial", command=self.tela_inicial)
        botao_voltar.pack(pady=10)
        
"""
# Inicializar a aplicação
root = tk.Tk()
app = Aplicacao(root)
root.mainloop()
