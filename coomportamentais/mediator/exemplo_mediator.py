from abc import ABC, abstractmethod


# =============================================================
# Interface Mediator — Define o contrato para comunicação
# =============================================================
class ChatMediator(ABC):

    @abstractmethod
    def send_message(self, message: str, user: "User") -> None:
        """Envia mensagens para os usuários registrados, exceto o remetente."""
        pass

    @abstractmethod
    def register_user(self, user: "User") -> None:
        """Registra um usuário no mediador."""
        pass


# =============================================================
# Concrete Mediator — Implementa a lógica central de comunicação
# =============================================================
class ChatRoom(ChatMediator):

    def __init__(self) -> None:
        # Lista interna de usuários registrados
        self._users: list[User] = []

    def register_user(self, user: "User") -> None:
        """Registra um usuário participante da sala de chat."""
        self._users.append(user)

    def send_message(self, message: str, user: "User") -> None:
        """
        Coordena a distribuição das mensagens.
        Envia para todos os usuários, exceto o remetente.
        """
        for u in self._users:
            if u != user:
                u.receive(message, user.name)


# =============================================================
# Colleague — Classe base para usuários
# =============================================================
class User(ABC):

    def __init__(self, name: str, mediator: ChatMediator) -> None:
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def send(self, message: str) -> None:
        """Envia mensagem através do mediador."""
        pass

    @abstractmethod
    def receive(self, message: str, sender: str) -> None:
        """Recebe mensagem encaminhada pelo mediador."""
        pass


# =============================================================
# Concrete Colleague — Usuário específico
# =============================================================
class ChatUser(User):

    def send(self, message: str) -> None:
        """
        Solicita ao mediador que distribua a mensagem.
        O usuário não envia diretamente para ninguém.
        """
        print(f"[{self.name}] enviando: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message: str, sender: str) -> None:
        """Exibe mensagem recebida."""
        print(f"[{self.name}] recebeu de {sender}: {message}")


# =============================================================
# Exemplo de uso
# =============================================================
if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = ChatUser("Maxwell", chat_room)
    user2 = ChatUser("Calebe", chat_room)
    user3 = ChatUser("Ana", chat_room)

    chat_room.register_user(user1)
    chat_room.register_user(user2)
    chat_room.register_user(user3)

    user1.send("Olá, pessoal!")
    user3.send("Bom dia, grupo!")
