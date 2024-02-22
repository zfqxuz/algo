import random
from Node import *

class Tree():
    nodeType=CommonNode
    def __init__(self):
        self.data=[random.randrange(0,100) for i in range(20)]
        self.root=self.nodeType()