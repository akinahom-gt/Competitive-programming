class ListNode(object):
	def __init__(self, val=0, next=None, prev=None):
		self.val = val
		self.next = next
		self.prev = prev

class MyLinkedList(object):
	def __init__(self):
		self.length, self.head, self.tail = 0, None, None

	def addAtHead(self, val):
		"""
		:type val: int
		:rtype: None
		"""
		if self.length == 0:
			self.head = self.tail = ListNode(val)
			self.length = 1
			return

		newNode = ListNode(val, self.head)
		self.head.prev = newNode
		self.head = newNode
		self.length += 1


	def addAtTail(self, val):
		"""
		:type val: int
		:rtype: None
		"""
		if self.length == 0:
			self.head = self.tail = ListNode(val)
			self.length = 1
			return

		newNode = ListNode(val, None, self.tail)
		self.tail.next = newNode
		self.tail = newNode
		self.length += 1


	def find(self, index):
		'''
		the index must be valid
		'''
		if (index << 1) <= self.length: # index <= length - index
			pointer = self.head
			for _ in range(index): 
				pointer = pointer.next
		else:
			pointer = self.tail
			for _ in range(self.length - 1 - index): 
				pointer = pointer.prev

		return pointer


	def get(self, index):
		"""
		:type index: int
		:rtype: int
		"""
		if index >= self.length: 
			return -1

		return self.find(index).val


	def addAtIndex(self, index, val):
		"""
		:type index: int
		:type val: int
		:rtype: None
		"""
		if index > self.length: return
		if index == self.length: return self.addAtTail(val)
		if index == 0: return self.addAtHead(val)

		pointer = self.find(index)
		newNode = ListNode(val, pointer, pointer.prev)
		pointer.prev.next = pointer.prev = newNode # ->
		self.length += 1


	def deleteAtIndex(self, index):
		"""
		:type index: int
		:rtype: None
		"""
		if index >= self.length: 
			return
		if self.length == 1:
			self.length, self.head, self.tail = 0, None, None
			return
		if index == 0: 
			self.head = self.head.next
			self.head.prev = None
			self.length -= 1
			return
		if index == self.length - 1: 
			self.tail = self.tail.prev
			self.tail.next = None
			self.length -= 1
			return

		pointer = self.find(index)
		pointer.prev.next, pointer.next.prev = pointer.next, pointer.prev
		self.length -= 1
    
    
