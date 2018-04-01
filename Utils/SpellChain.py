from abc import ABCMeta, abstractmethod
from enum import Enum, auto


class SpellHandlerLevel(Enum):

    GAME = auto()
    SINGLE_TARGET = auto()
    ALL = auto()


# Class for handling who/what gets the spell effects applied to them.
class SpellHandler(object):

    __metaclass__ = ABCMeta

    def __init__(self, levels):
        self.handler_levels = []
        self.next = None

        for level in levels:
            self.handler_levels.append(level)

    def set_next(self, next_handler):
        self.next = next_handler
        return self.next

    def handle(self, spell, level):
        if level == SpellHandlerLevel.ALL or level in self.handler_levels:

            self.trigger_spell(spell)

        if self.next is not None:
            self.next.handle(spell, level)

    @abstractmethod
    def trigger_spell(self, spell):
        raise NotImplementedError("You should implement this method.")
