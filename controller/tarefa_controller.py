from model.tarefa_model import TarefaModel
from view.tarefa_view import TarefaView

class TarefaController:
    def __init__(self):
        self.modelo = TarefaModel()
        self.visao = TarefaView(self)
        self.visao.atualizar_lista(self.modelo.listar_tarefas())
    
    def adicionar_tarefa(self):
        descricao = self.visao.obter_texto_entrada()
        if descricao:
            self.modelo.adicionar_tarefa(descricao)
            self.visao.limpar_entrada()
            self.visao.atualizar_lista(self.modelo.listar_tarefas())
    
    def marcar_concluida(self):
        indice = self.visao.obter_indice_selecionado()
        if indice is not None:
            self.modelo.marcar_concluida(indice)
            self.visao.atualizar_lista(self.modelo.listar_tarefas())
    
    def iniciar(self):
        self.visao.iniciar()
