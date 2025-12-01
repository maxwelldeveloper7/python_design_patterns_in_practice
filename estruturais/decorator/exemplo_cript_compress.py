from abc import ABC, abstractmethod


# ----------------------------------------------------------
# Component (Interface base)
# ----------------------------------------------------------

class MessageService(ABC):
    """
    Interface que define a operação de envio de mensagem.
    Representa o 'Component' no padrão Decorator.
    """

    @abstractmethod
    def send(self, message: str) -> None:
        pass


# ----------------------------------------------------------
# Concrete Component (Objeto original)
# ----------------------------------------------------------

class BasicMessageService(MessageService):
    """
    Implementação principal do serviço de mensagens.
    Envia o texto exatamente como foi recebido.
    """

    def send(self, message: str) -> None:
        print(f"Enviando mensagem: {message}")


# ----------------------------------------------------------
# Decorator Abstrato
# ----------------------------------------------------------

class MessageDecorator(MessageService):
    """
    Representa a estrutura base para todos os decoradores.
    Armazena um componente e delega chamadas para ele.
    """

    def __init__(self, wrapped: MessageService) -> None:
        self._wrapped = wrapped

    @abstractmethod
    def send(self, message: str) -> None:
        pass


# ----------------------------------------------------------
# Concrete Decorators (decoradores reais)
# ----------------------------------------------------------

class EncryptedMessageDecorator(MessageDecorator):
    """
    Adiciona criptografia antes de enviar a mensagem.
    """

    def send(self, message: str) -> None:
        encrypted = self._encrypt(message)
        self._wrapped.send(encrypted)

    def _encrypt(self, message: str) -> str:
        # Exemplo simples: inverte o texto como "pseudo-criptografia"
        return message[::-1]


class CompressedMessageDecorator(MessageDecorator):
    """
    Adiciona compressão simples antes de enviar a mensagem.
    """

    def send(self, message: str) -> None:
        compressed = self._compress(message)
        self._wrapped.send(compressed)

    def _compress(self, message: str) -> str:
        # Exemplo simplificado: remove espaços
        return message.replace(" ", "")


# ----------------------------------------------------------
# Uso prático do padrão Decorator
# ----------------------------------------------------------

# Serviço básico
service = BasicMessageService()

# Decorando com criptografia
encrypted_service = EncryptedMessageDecorator(service)

# Decorando com compressão e criptografia
compressed_then_encrypted = EncryptedMessageDecorator(
    CompressedMessageDecorator(service)
)

# Execução
service.send("Mensagem simples.")
encrypted_service.send("Mensagem confidencial.")
compressed_then_encrypted.send("Mensagem com compressão e criptografia.")
