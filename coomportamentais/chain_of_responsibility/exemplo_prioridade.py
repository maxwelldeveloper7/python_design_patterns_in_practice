"""
Exemplo do padrão Chain of Responsibility com boas práticas de Clean Code:
- Métodos curtos e objetivos
- Nomes descritivos
- Baixo acoplamento e alta coesão
- Comentários apenas onde agregam contexto real
"""

from abc import ABC, abstractmethod


# ----------------------------
# Objeto da requisição
# ----------------------------

class Request:
    """
    Representa uma requisição genérica com um nível de prioridade.
    """
    def __init__(self, priority: str, message: str):
        self.priority = priority
        self.message = message


# ----------------------------
# Interface Base do Handler
# ----------------------------

class Handler(ABC):
    """
    Interface comum para todos os manipuladores.
    Cada Handler deve:
    - Tentar processar a requisição
    - Encaminhar para o próximo handler caso não consiga
    """

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: "Handler") -> "Handler":
        """
        Define o próximo handler da cadeia.
        O retorno permite encadeamento fluente:
        ex: h1.set_next(h2).set_next(h3)
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Request) -> None:
        """
        Método que tenta processar a requisição.
        Subclasses devem implementar a lógica específica.
        """
        pass

    def _forward(self, request: Request) -> None:
        """
        Encaminha a requisição para o próximo handler, caso exista.
        """
        if self._next_handler:
            self._next_handler.handle(request)
        else:
            print(f"[Sem Handler] Nenhum manipulador conseguiu processar: {request.message}")


# ----------------------------
# Handlers Concretos
# ----------------------------

class LowPriorityHandler(Handler):
    """Processa somente requisições de prioridade 'baixa'."""

    def handle(self, request: Request) -> None:
        if request.priority == "baixa":
            print(f"[LowPriorityHandler] Processando: {request.message}")
        else:
            self._forward(request)


class MediumPriorityHandler(Handler):
    """Processa somente requisições de prioridade 'média'."""

    def handle(self, request: Request) -> None:
        if request.priority == "media":
            print(f"[MediumPriorityHandler] Processando: {request.message}")
        else:
            self._forward(request)


class HighPriorityHandler(Handler):
    """Processa somente requisições de prioridade 'alta'."""

    def handle(self, request: Request) -> None:
        if request.priority == "alta":
            print(f"[HighPriorityHandler] Processando: {request.message}")
        else:
            self._forward(request)


# ----------------------------
# Demonstração de Uso
# ----------------------------

if __name__ == "__main__":
    # Construção da cadeia
    low = LowPriorityHandler()
    medium = MediumPriorityHandler()
    high = HighPriorityHandler()

    # Encadeamento: low -> medium -> high
    low.set_next(medium).set_next(high)

    # Testes
    low.handle(Request("baixa", "Gerar relatório simples"))
    low.handle(Request("media", "Exportar dados para CSV"))
    low.handle(Request("alta", "Enviar alerta urgente"))
    low.handle(Request("critica", "Evento desconhecido"))
