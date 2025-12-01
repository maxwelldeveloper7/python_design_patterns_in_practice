"""
Exemplo do padrão Proxy aplicado ao controle de acesso de um serviço sensível.
"""

from abc import ABC, abstractmethod


class SensitiveDataService(ABC):
    """
    Interface comum para o serviço real e seu Proxy.
    Permite que ambos possam ser usados de forma intercambiável.
    """

    @abstractmethod
    def get_data(self) -> str:
        """Retorna dados sigilosos."""
        pass


class RealSensitiveDataService(SensitiveDataService):
    """
    Implementação concreta do serviço que realmente acessa o recurso caro.
    Aqui poderia haver uma chamada a API, conexão com banco, etc.
    """

    def get_data(self) -> str:
        # Simula operação pesada
        print("[RealService] Acessando dados sensíveis no servidor remoto...")
        return "DADOS SIGILOSOS: Relatórios confidenciais."


class SensitiveDataProxy(SensitiveDataService):
    """
    Proxy responsável por:
    - Controlar acesso (autenticação)
    - Evitar chamadas desnecessárias (cache simples)
    - Manter o mesmo contrato do serviço real
    """

    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password
        self._real_service = RealSensitiveDataService()
        self._cached_data = None

    def _is_authenticated(self) -> bool:
        """
        Regra de autenticação simplificada.
        Em sistemas reais, haveria uso de tokens, hashing, AD/LDAP etc.
        """
        return self.user == "admin" and self.password == "1234"

    def get_data(self) -> str:
        """
        O cliente usa este método como se estivesse acessando o serviço real.
        Porém, o Proxy controla o acesso e otimiza chamadas.
        """

        if not self._is_authenticated():
            return "[Proxy] Acesso negado: credenciais inválidas."

        # Se o dado já foi carregado, não acessar novamente o serviço real
        if self._cached_data is None:
            print("[Proxy] Cache vazio. Buscando dados no serviço real...")
            self._cached_data = self._real_service.get_data()
        else:
            print("[Proxy] Retornando dados do cache.")

        return self._cached_data


# ------------------ Exemplo de Uso ------------------

if __name__ == "__main__":
    print("Tentativa com usuário inválido:")
    proxy_invalid = SensitiveDataProxy("guest", "1111")
    print(proxy_invalid.get_data(), end="\n\n")

    print("Acesso com usuário válido:")
    proxy_valid = SensitiveDataProxy("admin", "1234")
    print(proxy_valid.get_data())
    print(proxy_valid.get_data())  # Aqui virá do cache
