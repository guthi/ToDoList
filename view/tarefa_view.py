import tkinter as tk

class TarefaView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Gerenciador de Tarefas")
        
        self.entrada = tk.Entry(self.root, width=40)
        self.entrada.pack()
        
        self.botao_adicionar = tk.Button(self.root, text="Adicionar Tarefa", command=self.controller.adicionar_tarefa)
        self.botao_adicionar.pack()
        
        self.lista = tk.Listbox(self.root, width=50)
        self.lista.pack()
        
        self.botao_concluir = tk.Button(self.root, text="Marcar como Concluída", command=self.controller.marcar_concluida)
        self.botao_concluir.pack()
    
    def obter_texto_entrada(self):
        return self.entrada.get()
    
    def limpar_entrada(self):
        self.entrada.delete(0, tk.END)
    
    def atualizar_lista(self, tarefas):
        self.lista.delete(0, tk.END)
        for i, tarefa in enumerate(tarefas):
            status = "✔" if tarefa['concluida'] else "✘"
            self.lista.insert(tk.END, f"{i}. {tarefa['descricao']} [{status}]")
    
    def obter_indice_selecionado(self):
        selecionado = self.lista.curselection()
        return selecionado[0] if selecionado else None
    
    def iniciar(self):
        self.root.mainloop()
