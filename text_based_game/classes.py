import images
import sys
import random as rand
from time import sleep 


class enemy:
  alive = True
    #initialization
  def __init__(self,name,base_hp,attack,type,golddrop,xp,strength = 0, weakness = 0,loot = None):
    self.name = name
    self.hp = base_hp
    self.base_hp = base_hp
    self.attackmin,self.attackmax = attack
    self.strength = strength 
    self.weakness = weakness 
    self.golddropmin,self.golddropmax = golddrop
    self.xpmin,self.xpmax = xp
    self.charge = 0
    self.loot = loot

    #rather just give each weapon its dmg 
  def takedamage(self,attack,weapon):
    #sword = weapon 1 
    #bow = weapon 2
    #magic = weapon 3
    pass

    #boring usless attack function 
  def attack(self):
    return rand.randint(self.attackmin,self.attackmax)
  
    