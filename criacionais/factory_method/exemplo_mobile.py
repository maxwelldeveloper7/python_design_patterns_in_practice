from abc import ABC, abstractmethod

# ==========================================================================
# Produto: Interface comum para notificações em apps móveis.
# ==========================================================================

class MobileNotification(ABC):

    @abstractmethod
    def show(self, title: str, message: str) -> None:
        """Exibe uma notificação local. A plataforma define o comportamento."""
        pass


# ==========================================================================
# Produtos Concretos: Implementações específicas por plataforma.
# ==========================================================================

class AndroidNotification(MobileNotification):
    def show(self, title: str, message: str) -> None:
        # Simulação do comportamento mobile real
        print(f"[ANDROID] Notificação:")
        print(f" - Canal: 'default'")
        print(f" - Prioridade: HIGH")
        print(f" - Título: {title}")
        print(f" - Mensagem: {message}")


class IOSNotification(MobileNotification):
    def show(self, title: str, message: str) -> None:
        print(f"[iOS] Notification:")
        print(f" - Permission: GRANTED")
        print(f" - Alert Title: {title}")
        print(f" - Body: {message}")


class WebPWANotification(MobileNotification):
    def show(self, title: str, message: str) -> None:
        print(f"[PWA] Web Push:")
        print(f" - Título: {title}")
        print(f" - Mensagem: {message}")
        print(f" - Ícone: '/assets/icon.png'")


# ==========================================================================
# Criador: Define o Factory Method.
# ==========================================================================

class NotificationCreator(ABC):

    @abstractmethod
    def factory_method(self) -> MobileNotification:
        """Retorna o tipo correto de notificação conforme a plataforma."""
        pass

    def notify(self, title: str, message: str) -> None:
        """
        Regras de alto nível: o app chama apenas este método.
        Não precisa saber qual plataforma será usada.
        """
        notificacao = self.factory_method()
        notificacao.show(title, message)


# ==========================================================================
# Criadores Concretos para cada plataforma.
# ==========================================================================

class AndroidNotificationCreator(NotificationCreator):
    def factory_method(self) -> MobileNotification:
        return AndroidNotification()


class IOSNotificationCreator(NotificationCreator):
    def factory_method(self) -> MobileNotification:
        return IOSNotification()


class PWAWebNotificationCreator(NotificationCreator):
    def factory_method(self) -> MobileNotification:
        return WebPWANotification()


# ==========================================================================
# Uso típico em um app mobile cross-platform
# ==========================================================================

def detectar_plataforma():
    """
    Função fictícia que simula a detecção da plataforma.
    Em um app real: usar API do sistema.
    """
    return "android"   # Troque para 'ios' ou 'pwa'


if __name__ == "__main__":
    plataforma = detectar_plataforma()

    # Fábrica escolhida conforme a plataforma
    if plataforma == "android":
        creator = AndroidNotificationCreator()
    elif plataforma == "ios":
        creator = IOSNotificationCreator()
    else:
        creator = PWAWebNotificationCreator()

    # App envia a notificação sem saber qual implementação está sendo usada
    creator.notify("Bem-vindo!", "Seu aplicativo iniciou corretamente.")
