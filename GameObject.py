#!/usr/bin/env python3

import uuid
from direct.actor.Actor import Actor


class GameObject(object):

    usedID = 10000
    # the object that all game entities inherit

    def __init__(self, objectID = uuid.uuid4):

        self._objectID = objectID # a string/number used to refer to the object

        self._pos = [0, 0, 0]  # the x, y and z position of the object
        self._ang = [0, 0, 0]  # the yaw, pitch and roll of the object

        # a list of pointers of all tasks that must be run per frame (per step) for the object
        self._objectTasks = []

        self._actor = None  # holds the actor for the game object
        self._scale = [1, 1, 1]  # holds the scale of the game object

    def assn_actor(self, models, anims):
        self._actor = Actor(models=models, anims=anims)

    # ------------------
    # GETTERS
    # ------------------

    def getPos(self):
        return self._pos

    def getAng(self):
        return self._ang

    # -------------------
    # SETTERS
    # -------------------

    def setPos(self, pos):
        self._pos = pos

    def setAng(self, *ang):
        self._ang = ang

    # ----------------------
    # Object overide methods
    # ----------------------

    def __str__(self):
        return "Object [{objectID}]:\n POS: {pos}\n ANG: {ang}".format(objectID = self._objectID, pos = self._pos, ang = self._ang)
