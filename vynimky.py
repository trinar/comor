#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vynimka(Exception): #trieda vynimiek
  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return 'Vynimka(\'' + str(self) + '\')'

  def __str__(self):
    return str(self.value)
