class TarefaModel:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, descricao):
        self.tarefas.append({'descricao': descricao, 'concluida': False})
    
    def listar_tarefas(self):
        return self.tarefas
    
    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]['concluida'] = True
