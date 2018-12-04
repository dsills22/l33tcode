#merge overlapping intervals

class Solution():
	def compare(self, a, b):
		if a.start < b.start:
			return -1
		elif a.start > b.start:
			return 1
		elif a.end < b.end:
			return -1
		elif a.end > b.end:
			return 1
		else:
			return 0

	def partition(self, intervals, low, high):
		pivotElem = intervals[high]
		rightMostSmallElem = low - 1
		for i in range(low, high):
			elem = intervals[i]
			if self.compare(elem, pivotElem) <= 0:
				rightMostSmallElem = rightMostSmallElem + 1
				intervals[i], intervals[rightMostSmallElem] = intervals[rightMostSmallElem], intervals[i]
		intervals[high], intervals[rightMostSmallElem + 1] = intervals[rightMostSmallElem + 1], intervals[high]
		return rightMostSmallElem + 1

	def quicksort(self, intervals, low, high):
		if low < high:
			partitionPoint = self.partition(intervals, low, high)
			self.quicksort(intervals, partitionPoint + 1, high)
			self.quicksort(intervals, low, partitionPoint - 1)

	def merge(self, intervals):
		print(intervals)
		self.quicksort(intervals, 0, len(intervals) - 1)
		for i in range(1, len(intervals)):
			if intervals[i-1].start <= intervals[i].end and intervals[i-1].end >= intervals[i].start:
				intervals[i].start = min(intervals[i-1].start, intervals[i].start)
				intervals[i].end = max(intervals[i-1].end, intervals[i].end)
				intervals[i-1] = None
		result = []
		for i in range(0, len(intervals)):
			if intervals[i] != None:
				result.append(intervals[i])
		return result

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))
print(sol.merge([[1, 20], [0, 10], [8, 15], [19, 21], [20, 21], [19, 20], [27, 32]]))
