class Util:
    """
    @staticmethod + @property:
    Propriedades de classe sem a necessidade de acesso à instância ou à classe.
    """
    @staticmethod
    @property
    def versao():
        return "1.0"

print(Util.versao)  # Saída: 1.0
