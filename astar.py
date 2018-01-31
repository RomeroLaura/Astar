#!/usr/bin/env python

#imports
from Queue import PriorityQueue



#create a new class for states to move around
class State(object):
	def __init__(self, value, parent, start= 0, goal = 0):
		#initialize values
		self.children = []
		self.parent = parent
		self.value = value
		self.dist = 0
		if parent:
			self.path = parent.path[:]
			self.path.append(value)
			self.start = parent.start
			self.goal = parent.goal
		else:
			self.path = [value]
			self.start = start
			self.goal = goal
	
	def GetDist(self):
		pass

	def CreateChildren(self):
		pass

#subclass
class State_String(State):
	def __init__(self, value, parent, start = 0, goal = 0):
		super(State_String, self).__init__(value, parent, start, goal)
		self.dist = self.GetDist()

	def GetDist(self):
		if self.value == self.goal:
			return 0
		dist = 0
		for i in xrange(len(self.goal)):
			letter = self.goal[i]
			dist += abs(i-self.value.index(letter))
		return dist
		
	def CreateChildren(self):
		if not self.children:
			for i in xrange(len(self.goal)-1):
				val = self.value
				val = val[:i] + val[i+1] +val[i] + val[i+2:]
				child = State_String(val, self)
				self.children.append(child)


class AstarAlgorithm:
	def __init__(self, start, goal):
		self.path = []
		self. closedQueue = []
		self.openQueue = PriorityQueue()
		self.start = start
		self.goal = goal
	
	def Solve(self):
		startState = State_String(self.start, 0, self.start, self.goal)
		self.openQueue.put((0, startState))
		while(not self.path and self.openQueue.qsize()):
			closestChild = self.openQueue.get()[1]
			closestChild.CreateChildren()
			self.closedQueue.append(closestChild)
			for child in closestChild.children:
				if child not in self.closedQueue:
					if not child.dist:
						self.path = child.path
						#break
					else:
						self.openQueue.put((child.dist, child))
		if not self.path:
			print "Not found"
		else:
			print self.path

					
#main

if __name__ == "__main__":
	start1 = "glean"
	goal1 = "angel"
	a = AstarAlgorithm(start1, goal1)
	a.Solve()
	print "done"
	
		