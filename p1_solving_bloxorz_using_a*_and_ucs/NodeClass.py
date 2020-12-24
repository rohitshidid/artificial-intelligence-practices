# Node class to represents each state of the game

# Coordinates: (x,y) position or [(x1,y1), (x2,y2)] position of the block according to it's position
# Parent: parent node, if such a node exists
# Cost: Cost to reach to the node from it's parent
class Node:

    # region Constructor

    def __init__(self, coordinates, cost, heuristic = 0):
        self.coordinates = coordinates # coordinate 
        self.parent = None # parent of the node
        self.childs = [] # childs of the node
        self.cost = cost # path cost for the given node
        self.heuristic = heuristic # 0 for UCS

    #endregion

    # region Setters

    # set parent of the node
    def SetParent(self, parent):
        self.parent = parent

    # endregion

    # region Adders

    def AddChild(self, child):
        self.childs.append(child) 

    # endregion

    # region Getters

    # returns node and it's parents until root node (self -> parent -> parent -> ... -> root)
    def GetAllParents(self):
        
        node = self
        nodes = [node] # first add self

        # continue to add parent until reaching the root node
        while node.parent != None:
            node = node.parent
            nodes.append(node)
        
        return nodes

    def GetCost(self):
        return self.cost
    
    def GetCoordinates(self):
        return self.coordinates

    # endregion

# Priority Queue implementation for Node Class
class NodePQueue(object): 
    
    def __init__(self): 
        self.queue = [] 

    def show(self):
        print(self.queue)
    
    # check if the queue is empty
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # insert to the queue
    def insert(self, node): 
        self.queue.append(node)
        self.queue = list(set(self.queue))
  
    # pop from the queue according to cost of the node
    def pop(self): 
        mn = 0
        for i in range(len(self.queue)): 
            cost, heuristic, minCost, minHeuristic = self.queue[i].cost, self.queue[i].heuristic, self.queue[mn].cost, self.queue[mn].heuristic
            if (cost + heuristic) < (minCost + minHeuristic): 
                mn = i 
        item = self.queue[mn] 
        del self.queue[mn] 
        return item 