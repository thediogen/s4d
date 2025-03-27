from enum import Enum


class CartStatus(Enum):
    forming = 'forming'
    accepted = 'accepted'
    waiting_for_accept = 'waiting for accept'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
