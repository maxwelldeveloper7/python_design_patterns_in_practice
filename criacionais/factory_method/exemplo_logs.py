import logging
from abc import ABC, abstractmethod


# ----------------------------------------------------------------------
# Configuração de Logging (arquivo + console)
# ----------------------------------------------------------------------
logger = logging.getLogger("notificacoes")
logger.setLevel(logging.INFO)

formato = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# Log em arquivo
arquivo_handler = logging.FileHandler("notificacoes.log")
arquivo_handler.setFormatter(formato)

# Log no console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formato)

logger.addHandler(arquivo_handler)
logger.addHandler(console_handler)


# ----------------------------------------------------------------------
# Produto Abstrato
# ----------------------------------------------------------------------
class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> bool:
        """
        Envia uma mensagem e retorna True/False se foi bem sucedido.
        """
        pass


# ----------------------------------------------------------------------
# Produtos Concretos
# ----------------------------------------------------------------------
class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem: str) -> bool:
        logger.info("Enviando e-mail...")
        # Simula envio bem-sucedido
        logger.info(f"E-mail enviado com sucesso: {mensagem}")
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self, mensagem: str) -> bool:
        logger.info("Enviando SMS...")

        # Simulação de falha se a mensagem for muito longa
        if len(mensagem) > 160:
            logger.error("Falha: SMS excede 160 caracteres.")
            return False

        logger.info(f"SMS enviado: {mensagem}")
        return True


class NotificacaoPush(Notificacao):
    def enviar(self, mensagem: str) -> bool:
        logger.info("Enviando Push Notification...")
        logger.info(f"Push enviado: {mensagem}")
        return True


# ----------------------------------------------------------------------
# Creator Abstrato
# ----------------------------------------------------------------------
class NotificacaoCreator(ABC):

    @abstractmethod
    def factory_method(self) -> Notificacao:
        """Cria um objeto que implementa Notificacao."""
        pass

    def enviar_notificacao(self, mensagem: str) -> None:
        """
        Fluxo de envio com:
        - validação de entrada
        - logs centralizados
        - criação do produto via Factory Method
        """

        if not self._mensagem_valida(mensagem):
            logger.error("Envio cancelado: mensagem inválida.")
            return

        notificacao = self.factory_method()

        sucesso = notificacao.enviar(mensagem)

        if sucesso:
            logger.info("Notificação concluída com sucesso.")
        else:
            logger.warning("Notificação finalizada com falhas.")

    def _mensagem_valida(self, mensagem: str) -> bool:
        """
        Regras básicas de validação:
        - mensagem não pode ser vazia
        - tamanho mínimo
        """
        if not mensagem or mensagem.strip() == "":
            logger.error("Mensagem vazia ou inválida.")
            return False

        if len(mensagem) < 5:
            logger.error("Mensagem muito curta.")
            return False

        return True


# ----------------------------------------------------------------------
# Creators Concretos
# ----------------------------------------------------------------------
class EmailCreator(NotificacaoCreator):
    def factory_method(self) -> Notificacao:
        return NotificacaoEmail()


class SMSCreator(NotificacaoCreator):
    def factory_method(self) -> Notificacao:
        return NotificacaoSMS()


class PushCreator(NotificacaoCreator):
    def factory_method(self) -> Notificacao:
        return NotificacaoPush()


# ----------------------------------------------------------------------
# Simulação Real
# ----------------------------------------------------------------------
if __name__ == "__main__":

    email = EmailCreator()
    sms = SMSCreator()
    push = PushCreator()

    email.enviar_notificacao("Relatório disponível no sistema.")
    sms.enviar_notificacao("Seu código é 4521.")
    sms.enviar_notificacao("x")  # inválida
    sms.enviar_notificacao("A" * 200)  # SMS muito longo
    push.enviar_notificacao("Atualização instalada com sucesso.")
