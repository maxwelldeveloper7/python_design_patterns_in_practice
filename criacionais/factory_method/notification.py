from abc import ABC, abstractmethod


"""
    Produto: Interface comum para todos os tipos de notificações
"""
class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        """Envia uma mensagem. Deve ser implementado pelas subclasses."""
        pass


"""    
    Produtos Concretos: Cada classe implementa uma forma específica de envio.
"""
class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem: str) -> None:
        print(f"[E-MAIL] Enviando mensagem: {mensagem}")


class NotificacaoSMS(Notificacao):
    def enviar(self, mensagem: str) -> None:
        print(f"[SMS] Enviando mensagem: {mensagem}")


class NotificacaoPush(Notificacao):
    def enviar(self, mensagem: str) -> None:
        print(f"[PUSH] Enviando mensagem: {mensagem}")


"""    
    Criador (Creator): Define o Factory Method.
    Importante: o método factory_method devolve o "Produto".
"""
class NotificacaoCreator(ABC):
    @abstractmethod
    def factory_method(self) -> Notificacao:
        """
        Factory Method.
        As subclasses decidirão *qual* produto concreto será criado.
        """
        pass

    def enviar_notificacao(self, mensagem: str) -> None:
        """
        Método de alto nível.
        Ele não sabe qual notificação concreta será criada.
        Depende apenas da interface Notificacao.
        """
        notificacao = self.factory_method()
        notificacao.enviar(mensagem)


"""
    Criadores Concretos: Cada um instancia um tipo específico de produto.
"""
class EmailCreator(NotificacaoCreator):
    def factory_method(self) -> Notificacao:
        return NotificacaoEmail()


class SMSCreator(NotificacaoCreator):
    def factory_method(self) -> Notificacao:
        return NotificacaoSMS()


class PushCreator(NotificacaoCreator):
    def factory_method(self) -> Notificacao:
        return NotificacaoPush()

"""
    Uso prático: o código cliente depende apenas dos Creators,
    e não das implementações concretas de notificação.
    Isso reduz acoplamento e aumenta extensibilidade.
"""
if __name__ == "__main__":

    # Cada criador sabe instanciar o tipo correto
    email = EmailCreator()
    sms = SMSCreator()
    push = PushCreator()

    # O método enviar_notificacao funciona igual para todos
    email.enviar_notificacao("Sua matrícula foi confirmada.")
    sms.enviar_notificacao("Código de verificação: 8421.")
    push.enviar_notificacao("Nova atualização disponível!")