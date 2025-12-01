# Sistema de Configuração - Padrão Singleton

Este projeto demonstra a implementação do padrão de design **Singleton** em Python através de um sistema de configuração global.

## Sobre o Padrão Singleton

O padrão Singleton garante que uma classe tenha apenas uma instância durante toda a execução da aplicação e fornece um ponto global de acesso a essa instância.

## Implementação

### Classe `ConfiguracaoSistema`

A classe implementa o padrão Singleton através do método especial `__new__()`, que controla a criação de instâncias.

#### Características principais:

- **Instância única**: Apenas um objeto da classe existe na aplicação
- **Acesso global**: Configurações acessíveis de qualquer parte do código
- **Inicialização controlada**: Evita re-inicialização da instância existente

#### Métodos:

- `atualizar_configuracao(novo_valor)`: Atualiza a configuração do sistema
- `obter_configuracao()`: Retorna a configuração atual

## Como usar

```python
from configuration_system import ConfiguracaoSistema

# Primeira instância
config1 = ConfiguracaoSistema()
config1.atualizar_configuracao("Modo desenvolvimento")

# Segunda "instância" (na verdade, a mesma)
config2 = ConfiguracaoSistema()

# Ambas referenciam o mesmo objeto
print(config1 is config2)  # True
print(config2.obter_configuracao())  # "Modo desenvolvimento"
```

## Execução

Para ver a demonstração do padrão:

```bash
python configuration_system.py
```

## Vantagens do Singleton

- Controle rigoroso sobre instanciação
- Acesso global consistente
- Economia de memória (uma única instância)
- Ideal para configurações, logs, conexões de banco

## Considerações

O padrão Singleton deve ser usado com cuidado, pois pode introduzir acoplamento forte e dificultar testes unitários.