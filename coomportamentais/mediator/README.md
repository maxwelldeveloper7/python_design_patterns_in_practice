# Padrão Mediator (Mediador)

## Visão Geral

O padrão **Mediator** é um padrão comportamental que define como um conjunto de objetos interage entre si. Em vez de os objetos se comunicarem diretamente, eles fazem isso através de um objeto mediador central, promovendo baixo acoplamento e facilitando a manutenção do código.

## Implementação

Criamos um sistema de chat onde usuários não se comunicam diretamente; toda comunicação passa por um **mediador** central que coordena as interações.

### Componentes Principais
![](../../assets/img/mediator.png)
#### 1. ChatMediator (Interface Mediator)
```python
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: "User") -> None:
        pass
    
    @abstractmethod
    def register_user(self, user: "User") -> None:
        pass
```

Define o contrato para comunicação entre usuários.

#### 2. ChatRoom (Concrete Mediator)
```python
class ChatRoom(ChatMediator):
    def __init__(self) -> None:
        self._users: list[User] = []
```

Implementa a lógica central de comunicação, coordenando o envio de mensagens entre usuários registrados.

#### 3. User (Colleague)
```python
class User(ABC):
    def __init__(self, name: str, mediator: ChatMediator) -> None:
        self.name = name
        self.mediator = mediator
```

Classe base para usuários que se comunicam através do mediador.

#### 4. ChatUser (Concrete Colleague)
```python
class ChatUser(User):
    def send(self, message: str) -> None:
        print(f"[{self.name}] enviando: {message}")
        self.mediator.send_message(message, self)
```

Implementação específica de usuário que envia e recebe mensagens.

## Como Funciona

1. **Registro**: Usuários são registrados na sala de chat
2. **Envio**: Quando um usuário envia uma mensagem, ela é passada para o mediador
3. **Distribuição**: O mediador distribui a mensagem para todos os outros usuários
4. **Recebimento**: Cada usuário recebe a mensagem através do método `receive()`

## Código

```python
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

```

### Saída Esperada
```
[Maxwell] enviando: Olá, pessoal!
[Calebe] recebeu de Maxwell: Olá, pessoal!
[Ana] recebeu de Maxwell: Olá, pessoal!
[Ana] enviando: Bom dia, grupo!
[Maxwell] recebeu de Ana: Bom dia, grupo!
[Calebe] recebeu de Ana: Bom dia, grupo!
```

## Vantagens

- **Baixo Acoplamento**: Usuários não precisam conhecer uns aos outros diretamente
- **Centralização**: Lógica de comunicação fica centralizada no mediador
- **Flexibilidade**: Fácil adicionar novos tipos de usuários ou modificar comportamentos
- **Reutilização**: O mediador pode ser reutilizado em diferentes contextos

## Casos de Uso

- Sistemas de chat e mensageria
- Interfaces gráficas com múltiplos componentes
- Sistemas de workflow
- Controladores de tráfego aéreo
- Sistemas de notificação
