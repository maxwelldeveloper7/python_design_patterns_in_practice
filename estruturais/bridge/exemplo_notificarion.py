from abc import ABC, abstractmethod

# ---------------------------------------
# Implementor: Define a interface da parte "implementação"
# ---------------------------------------

class MessageSender(ABC):
    """
    Define a interface que todas as implementações de envio de mensagem devem seguir.
    Este é o 'Implementor' no padrão Bridge.
    """

    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        """Envia a mensagem para o destinatário."""
        pass


# ---------------------------------------
# Concrete Implementors
# ---------------------------------------

class EmailSender(MessageSender):
    """Implementação concreta para envio de mensagens via E-mail."""

    def send(self, recipient: str, message: str) -> None:
        print(f"[Email] Para: {recipient} | Mensagem: {message}")


class SMSSender(MessageSender):
    """Implementação concreta para envio de mensagens via SMS."""

    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS] Para: {recipient} | Mensagem: {message}")


# ---------------------------------------
# Abstraction: Interface principal usada pelo cliente
# ---------------------------------------

class Notification:
    """
    Abstração que utiliza a implementação (MessageSender).
    Permite trocar implementações de envio sem alterar a lógica da notificação.
    """

    def __init__(self, sender: MessageSender) -> None:
        # Composição: a abstração *contém* uma referência para a implementação.
        self._sender = sender

    def notify(self, recipient: str, message: str) -> None:
        """Método de alto nível para enviar notificações."""
        self._sender.send(recipient, message)


# ---------------------------------------
# Refined Abstraction
# ---------------------------------------

class UrgentNotification(Notification):
    """
    Uma variação da abstração.
    Demonstra como novas abstrações podem ser criadas sem alterar as implementações.
    """

    def notify(self, recipient: str, message: str) -> None:
        # Possível extensão de comportamento
        urgent_message = f"[URGENTE] {message}"
        self._sender.send(recipient, urgent_message)


# ---------------------------------------
# Uso prático do padrão Bridge
# ---------------------------------------

# Implementações diferentes
email_sender = EmailSender()
sms_sender = SMSSender()

# Abstrações usando implementações distintas
normal_notification = Notification(email_sender)
urgent_notification = UrgentNotification(sms_sender)

normal_notification.notify("usuario@dominio.com", "Seu relatório está disponível.")
urgent_notification.notify("99999-9999", "Falha no servidor detectada!")
