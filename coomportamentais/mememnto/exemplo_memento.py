from __future__ import annotations
from dataclasses import dataclass
from typing import List


# =============================================================
# MEMENTO — Armazena o estado interno do objeto originador
# =============================================================
@dataclass(frozen=True)
class EditorMemento:
    """
    Representa o "instantâneo" (snapshot) do estado interno do editor.
    Usar dataclass torna o objeto imutável e seguro contra alterações acidentais.
    """
    content: str


# =============================================================
# ORIGINATOR — Objeto cujo estado deve ser salvo e restaurado
# =============================================================
class TextEditor:
    def __init__(self) -> None:
        self._content: str = ""

    def type(self, new_text: str) -> None:
        """Adiciona texto ao conteúdo atual."""
        self._content += new_text

    def save(self) -> EditorMemento:
        """
        Cria um Memento contendo o estado atual.
        O Originator é o único autorizado a criar seus próprios Mementos.
        """
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento) -> None:
        """Restaura o conteúdo a partir de um Memento."""
        self._content = memento.content

    @property
    def content(self) -> str:
        """Retorna o conteúdo atual, mantendo encapsulamento."""
        return self._content


# =============================================================
# CARETAKER — Responsável por armazenar e gerenciar Mementos
# =============================================================
class History:
    """
    Armazena os estados anteriores.
    Não altera e nem conhece detalhes internos dos Mementos.
    """
    def __init__(self) -> None:
        self._history: List[EditorMemento] = []

    def push(self, memento: EditorMemento) -> None:
        """Guarda um novo Memento na pilha de histórico."""
        self._history.append(memento)

    def pop(self) -> EditorMemento:
        """Retorna o último Memento salvo (efeito 'undo')."""
        if not self._history:
            raise IndexError("Nenhum estado salvo no histórico.")
        return self._history.pop()


# =============================================================
# Exemplo de uso
# =============================================================
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.type("Olá")
    history.push(editor.save())  # Salvando estado inicial

    editor.type(", mundo!")
    history.push(editor.save())  # Salvando segundo estado

    print("Antes do undo:", editor.content)

    editor.restore(history.pop())  # Desfaz última ação
    print("Depois de um undo:", editor.content)

    editor.restore(history.pop())  # Desfaz novamente
    print("Depois de dois undo:", editor.content)
