from abc import ABC, abstractmethod

# ======================================================================
# PRODUTOS ABSTRATOS
# Cada produto define uma interface que todos os produtos concretos devem seguir.
# ======================================================================

class Botao(ABC):
    @abstractmethod
    def desenhar(self) -> None:
        """Renderiza o botão na tela."""
        pass


class Checkbox(ABC):
    @abstractmethod
    def desenhar(self) -> None:
        """Renderiza a caixa de seleção na tela."""
        pass


# ======================================================================
# PRODUTOS CONCRETOS
# Cada fábrica concreta gerará seus próprios produtos específicos da plataforma.
# ======================================================================

class AndroidBotao(Botao):
    def desenhar(self) -> None:
        print("Desenhando botão no estilo Android.")


class AndroidCheckbox(Checkbox):
    def desenhar(self) -> None:
        print("Desenhando checkbox no estilo Android.")


class IOSBotao(Botao):
    def desenhar(self) -> None:
        print("Desenhando botão no estilo iOS.")


class IOSCheckbox(Checkbox):
    def desenhar(self) -> None:
        print("Desenhando checkbox no estilo iOS.")


# ======================================================================
# ABSTRACT FACTORY
# Declara um conjunto de métodos para criação de famílias de produtos.
# Todas as fábricas concretas devem implementar esses métodos.
# ======================================================================

class UIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        """Cria um botão compatível com a plataforma."""
        pass

    @abstractmethod
    def criar_checkbox(self) -> Checkbox:
        """Cria um checkbox compatível com a plataforma."""
        pass


# ======================================================================
# FACTORIES CONCRETAS
# Cada fábrica retorna produtos consistentes entre si.
# Exemplo: A fábrica Android cria somente widgets Android.
# ======================================================================

class AndroidFactory(UIFactory):
    def criar_botao(self) -> Botao:
        return AndroidBotao()

    def criar_checkbox(self) -> Checkbox:
        return AndroidCheckbox()


class IOSFactory(UIFactory):
    def criar_botao(self) -> Botao:
        return IOSBotao()

    def criar_checkbox(self) -> Checkbox:
        return IOSCheckbox()


# ======================================================================
# CÓDIGO CLIENTE
# Trabalha APENAS com as interfaces abstratas.
# Não conhece detalhes das plataformas.
# Isso facilita testes, extensões e redução de acoplamento.
# ======================================================================

class Aplicacao:
    def __init__(self, factory: UIFactory) -> None:
        # A factory é injetada, permitindo flexibilidade e substituição fácil.
        self._factory = factory

        # Cria os componentes da interface usando a Abstract Factory.
        self.botao = self._factory.criar_botao()
        self.checkbox = self._factory.criar_checkbox()

    def renderizar_tela(self) -> None:
        """Renderiza toda a UI da aplicação."""
        self.botao.desenhar()
        self.checkbox.desenhar()


# ======================================================================
# USO PRÁTICO
# O cliente escolhe qual fábrica utilizar (Android ou iOS).
# A aplicação automaticamente cria os widgets correspondentes.
# ======================================================================

if __name__ == "__main__":

    # Exemplo de escolha baseada em contexto real (REST, mobile, config etc.)
    plataforma = "android"  # poderia vir de config.json, API, variáveis de ambiente...

    if plataforma == "android":
        factory = AndroidFactory()
    else:
        factory = IOSFactory()

    app = Aplicacao(factory)
    app.renderizar_tela()
