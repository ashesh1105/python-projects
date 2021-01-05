import abc
from abc import ABCMeta, abstractstaticmethod

class IHandler(metaclass=ABCMeta):
    """The Interface for handling requests."""

    @staticmethod
    def set_successor(successor):
        """Set the next handler in the chain"""

    @staticmethod
    def handle(amount):
        """Handle the event"""