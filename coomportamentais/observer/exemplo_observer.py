from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# =============================================================
# OBSERVER — Interface dos observadores
# =============================================================
class Observer(ABC):
    """
    Interface que define o contrato para qualquer objeto que deseje
    ser notificado de mudanças do Subject.
    """

    @abstractmethod
    def update(self, temperature: float) -> None:
        """Executa ações quando o estado observado muda."""
        pass


# =============================================================
# SUBJECT — Interface do objeto observado
# =============================================================
class Subject(ABC):
    """
    Interface que padroniza a relação de inscrição e notificação.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notifica todos os observadores sobre atualizações."""
        pass


# =============================================================
# CONCRETE SUBJECT — Mantém o estado observado
# =============================================================
class WeatherStation(Subject):
    """
    Representa uma estação climática que mantém uma lista de
    observadores e um valor de temperatura.
    """

    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._temperature: float = 0.0

    def attach(self, observer: Observer) -> None:
        """Registra um observador interessado nas atualizações."""
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Remove um observador da lista."""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Notifica todos os observadores."""
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, new_temperature: float) -> None:
        """
        Atualiza o estado e dispara notificações.
        A separação em dois métodos evita efeitos colaterais inesperados.
        """
        self._temperature = new_temperature
        self.notify()


# =============================================================
# CONCRETE OBSERVERS — Reagem a atualizações
# =============================================================
class DisplayObserver(Observer):
    """Exibe a temperatura sempre que ela muda."""

    def update(self, temperature: float) -> None:
        print(f"[DISPLAY] Temperatura atualizada: {temperature}°C")


class LogObserver(Observer):
    """Registra temperatura em log sempre que houver mudança."""

    def update(self, temperature: float) -> None:
        print(f"[LOG] Registrando temperatura: {temperature}°C")


# =============================================================
# Exemplo de uso
# =============================================================
if __name__ == "__main__":
    station = WeatherStation()

    display = DisplayObserver()
    logger = LogObserver()

    station.attach(display)
    station.attach(logger)

    station.set_temperature(25.3)
    station.set_temperature(27.8)

    station.detach(logger)

    station.set_temperature(30.1)  # Apenas o display será notificado
