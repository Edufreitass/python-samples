from abc import ABC, abstractmethod


class Animal(ABC):
    """
    @abstractmethod:
        Usado para declarar um método abstrato em uma classe abstrata. As subclasses devem fornecer uma implementação.
    """

    @abstractmethod
    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"


class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
