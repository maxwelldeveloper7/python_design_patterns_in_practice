class ConfiguracaoSistema:
    """
    Implementa o padrão Singleton para gerenciar configurações globais do sistema.
    
    Garante que apenas uma instância desta classe exista durante toda a execução
    da aplicação, proporcionando um ponto centralizado para configurações.
    
    Attributes:
        _instancia: Armazena a única instância da classe (variável de classe)
        valor: Configuração específica da instância
    """
        
    # Variável de classe para armazenar a única instância (Singleton)
    _instancia = None
    
    def __new__(cls):
        """
        Controla a criação de instâncias, implementando o padrão Singleton.
        
        Returns:
            A instância única da classe ConfiguracaoSistema
            
        Note:
            Este método é chamado ANTES do __init__ durante a criação do objeto
        """
        # Verifica se já existe uma instância criada
        if cls._instancia is None:
            # Cria a primeira e única instância
            cls._instancia = super().__new__(cls)
            print("Criando instãncia única:")
        # Retorna a instância existente (ou recém-criada)
        return cls._instancia
    
    def __init__(self):
        """
        Inicializa a instância com valores padrão.
        
        Note:
            Este método pode ser chamado múltiplas vezes, mas a instância
            será a mesma devido ao Singleton implementado no __new__
        """
        
        # Inicializa apenas se for a primeira vez (evita re-inicialização)
        if not hasattr(self, 'valor'):
            self.valor = "Configuração padrão"

    def atualizar_configuracao(self, novo_valor):
        """
        Atualiza a configuração do sistema.

        Args:
            novo_valor: Novo valor para a configuração

        Example:
            >>> config = ConfiguracaoSistema()
            >>> config.atualizar_configuracao("Modo produção")
        """
        self.valor = novo_valor
        print(f"Configuração atualizada para: {novo_valor}")

    def obter_configuracao(self):
        """
        Retorna a configuração atual do sistema.

        Returns:
            str: Valor da configuração atual
        """
        return self.valor

# Exemplo de uso demonstrando o padrão Singleton
def demonstrar_singleton():
    """Demonstra o funcionamento do padrão Singleton."""
    
    # Primeira "criação" - instância real é criada
    config1 = ConfiguracaoSistema()
    config1.atualizar_configuracao("Configuração inicial")
    
    # Segunda "criação" - retorna a mesma instância
    config2 = ConfiguracaoSistema()
    
    # Verificação de que são o mesmo objeto
    print(f"config1 e config2 são o mesmo objeto: {config1 is config2}")
    print(f"Configuração via config2: {config2.obter_configuracao()}")


if __name__ == "__main__":
    demonstrar_singleton()