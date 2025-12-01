"""
Exemplo do padrão Command em Python
"""

from abc import ABC, abstractmethod


# ============================================
# Receiver — executa ações reais
# ============================================

class FileSystem:
    """
    Simula operações de um sistema de arquivos.
    É o 'Receiver' do padrão Command.
    """

    def create_file(self, name: str) -> None:
        print(f"[FileSystem] Arquivo criado: {name}")

    def rename_file(self, old_name: str, new_name: str) -> None:
        print(f"[FileSystem] Arquivo renomeado: {old_name} → {new_name}")

    def delete_file(self, name: str) -> None:
        print(f"[FileSystem] Arquivo deletado: {name}")


# ============================================
# Command — Interface base
# ============================================

class Command(ABC):
    """
    Define o contrato que todos os comandos devem cumprir.
    """

    @abstractmethod
    def execute(self) -> None:
        """Executa o comando."""
        pass

    @abstractmethod
    def undo(self) -> None:
        """Desfaz o comando (quando aplicável)."""
        pass


# ============================================
# Commands Concretos
# ============================================

class CreateFileCommand(Command):
    """
    Command para criar um arquivo.
    """

    def __init__(self, fs: FileSystem, filename: str):
        self.fs = fs
        self.filename = filename

    def execute(self) -> None:
        self.fs.create_file(self.filename)

    def undo(self) -> None:
        self.fs.delete_file(self.filename)


class RenameFileCommand(Command):
    """
    Command para renomear um arquivo.
    """

    def __init__(self, fs: FileSystem, old_name: str, new_name: str):
        self.fs = fs
        self.old_name = old_name
        self.new_name = new_name

    def execute(self) -> None:
        self.fs.rename_file(self.old_name, self.new_name)

    def undo(self) -> None:
        self.fs.rename_file(self.new_name, self.old_name)


class DeleteFileCommand(Command):
    """
    Command para excluir um arquivo.
    """

    def __init__(self, fs: FileSystem, filename: str):
        self.fs = fs
        self.filename = filename

    def execute(self) -> None:
        self.fs.delete_file(self.filename)

    def undo(self) -> None:
        self.fs.create_file(self.filename)


# ============================================
# Invoker — solicita a execução
# ============================================

class CommandInvoker:
    """
    Invoker que armazena um histórico de comandos executados.
    Permite desfazer operações.
    """

    def __init__(self):
        self._history = []

    def run(self, command: Command) -> None:
        """
        Executa um comando e registra seu histórico.
        """
        command.execute()
        self._history.append(command)

    def undo_last(self) -> None:
        """
        Desfaz o último comando executado.
        """
        if not self._history:
            print("[Invoker] Nada para desfazer.")
            return

        last_command = self._history.pop()
        last_command.undo()


# ============================================
# Demonstração de Uso
# ============================================

if __name__ == "__main__":
    fs = FileSystem()
    invoker = CommandInvoker()

    # Comandos
    create = CreateFileCommand(fs, "relatorio.txt")
    rename = RenameFileCommand(fs, "relatorio.txt", "relatorio_final.txt")
    delete = DeleteFileCommand(fs, "relatorio_final.txt")

    # Execução
    invoker.run(create)
    invoker.run(rename)
    invoker.run(delete)

    # Undo
    invoker.undo_last()
    invoker.undo_last()
    invoker.undo_last()
    invoker.undo_last()  # nada para desfazer
