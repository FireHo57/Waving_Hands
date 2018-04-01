# Class to track basic status effects on players
from abc import abstractmethod
import random

class Effect(object):

    def __init__(self, duration=1, long_duration=False):
        self.duration = duration
        self.long_duration = long_duration
        self.turns_active = 0
        self.expired = False

    def has_expired(self):
        return self.expired

    def turn(self):
        self.turns_active += 1
        self.expired = self.turns_active >= self.duration
        return self.effect

    @abstractmethod
    def effect(self, effect_target):
        raise NotImplementedError("\'effect\' method not implemented")


# class for managing the various effects that can be applied to a target and their time periods
class EffectsManager:

    def __init__(self, parent):
        self.parent = parent
        self.effects_buffer = []

    def set_effect(self, effect):
        self.effects_buffer.append(effect)

    def resolve_effects(self):
        # if there is only one effect
        if self.effects_buffer.count <= 1:
            self.parent.apply_effect(self.effects_buffer[0].turn())

        # if there are long duration effects e.g. blindness, invisibility etc
        effects_to_apply = [effect for effect in self.effects_buffer if effect.long_duration]
        for effect in effects_to_apply:
            self.parent.apply_effect(effect.turn())

        self.effects_buffer = [effect for effect in self.effects_buffer if not effect.expired]


class Amnesia(Effect):

    def effect(self, effect_target):
        effect_target.gestures = effect_target.last_gestures


class ParalysisLeft(Effect):

    def effect(self, effect_target):
        effect_target.left_gesture = effect_target.previous_left_gesture


class ParalysisRight(Effect):

    def effect(self, effect_target):
        effect_target.right_gesture = effect_target.previous_right_gesture


class ConfusionLeft(Effect):

    def effect(self, effect_target):
        effect_target.left_gesture = random.choice(effect_target.allowed_gestures)


class ConfusionRight(Effect):

    def effect(self, effect_target):
        effect_target.right_gesture = random.choice(effect_target.allowed_gestures)

class Fear(Effect):

    def effect(selfself, effect_target):
        effect_target.set_allowed_gestures("P,p,W,w,>")
