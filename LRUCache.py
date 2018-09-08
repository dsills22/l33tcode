
class Heap(object):
	#class NoneElem(object):
	#	def __init__(self):
	#		self.value = None

	def __init__(self, elements=[], heapType="min", comparisonProperty=None):
		self.elements = elements
		self.heapType = heapType #min or max
		self.comparisonProperty = comparisonProperty
		self.tree = list(self.elements)
		self.heapify(self.tree)

	def getTree(self):
		return self.tree

	def find(self, element):
		for i, e in enumerate(self.tree):
			if self.compare(element, e) == 0:
				return i
		return None

	def update(self, element, newElement):
		i = self.find(element)
		if i != None:
			self.tree[i] = newElement
			self.tree[i], self.tree[len(self.tree) - 1] = self.tree[len(self.tree) - 1], self.tree[i]
			self.reheap()

	def pop(self):
		return self.tree.pop()

	def push(self, a):
		self.tree.append(a)
		self.reheap()

	def reheap(self):
		c = len(self.tree) - 1
		p = int(c / 2)
		while p >= 0 and self.compare(self.tree[p], self.tree[c]) == 1:
			self.tree[p], self.tree[c] = self.tree[c], self.tree[p]
			c = p
			p = int(c / 2)

	def heapify(self, elements, start=None):
		length = len(elements)
		start = start or length - 1
		for c in range(start, 0, -1):
			p = int(c / 2)
			if p >= 0 and p < c:
				if self.compare(elements[p], elements[c]) == 1:
					elements[p], elements[c] = elements[c], elements[p]
					self.heapify(elements, p)

	def compare(self, a, b):
		if isinstance(a, Heap.NoneElem) or isinstance(b, Heap.NoneElem):
			return -1

		if self.comparisonProperty == None:
			if a > b:
				return (self.heapType=="min" and 1) or (self.heapType=="max" and -1)
			elif a < b:
				return (self.heapType=="min" and -1) or (self.heapType=="max" and 1)
			else:
				return 0
		else:
			if a[self.comparisonProperty] > b[self.comparisonProperty]:
				return (self.heapType=="min" and 1) or (self.heapType=="max" and -1)
			elif a[self.comparisonProperty] < b[self.comparisonProperty]:
				return (self.heapType=="min" and -1) or (self.heapType=="max" and 1)
			else:
				return 0


heap = Heap([7,6,5,4,3,2,1,0,88,-3])
print(heap.getTree())
heap.push(-10)
print(heap.getTree())
heap.push(1)
print(heap.getTree())
heap.update(0, -11)
print(heap.getTree())

