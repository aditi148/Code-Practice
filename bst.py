class node:
	def init(self ,data):
		self.left = none
		self.right = none
		self.data = data
	
	def insert(self, data):
		if data < self.data:
			if self.left is none:
				self.left= node(data)
			else:
				self.left.insert(data)
		elif data > self.data:
			if self.right is none:
				self.right = node(data)
			else:
				self.right.insert(data)
		else:
			self.data = data
			
			
