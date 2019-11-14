from collections import defaultdict 

class Graph:
	def __init__(self, connections, directed=False):
		self.graph = defaultdict(set)
		self.directed = directed
		self.addConnections(connections)

	# Generate the graph dictionary based on the array of touples that 
	# represent every edge in the graph.
	# Example: [(1, 2), (1, 3), (3, 4), (2, 4)] 
	def addConnections(self, connections):
		for a, b in connections:
			self.add(a, b)

	# Add an edge to the dictionary
	def add(self, a, b):
		self.graph[a].add(b)
		if (not self.directed):
			self.graph[b].add(a)

	# Remove an edge and all it's references from a dictionary
	def remove(self, a):
		for n, ref in self.graph.iteritems():
			try:
				ref.remove(a)
			except KeyError:
				pass
		try:
			del self.graph[a]
		except KeyError:
			pass

	# Find the shortest path between two nodes 
	def shortest_path(self, start, end, path =[]): 
		path = path + [start] 
		if start == end: 
			return path 
		shortest = None
		for node in self.graph[start]: 
			if node not in path: 
				newpath = find_shortest_path(self.graph, node, end, path) 
				if newpath: 
					if not shortest or len(newpath) < len(shortest): 
						shortest = newpath 
		return shortest

	# Utilitary recursive function that implements a DFS algorithm and
	# stacks the result in the 'output'(reference) parameter
	def topological_util(self, visited_list, vertex, output):
		if not visited_list[vertex]:
			visited_list[vertex] = True
			for neighbour in self.graph[vertex]:
				try:
					self.topological_util(visited_list, neighbour, output)
				except:
					pass
			output.append(vertex)

	# Function to create the 'visited_list' to avoid cycles and start
	# the topological_sort for the given vertex
	def topological_sort(self, vertex):
		output = []
		visited_list = defaultdict()
		for item in self.graph:
			visited_list[item] = False

		self.topological_util(visited_list, vertex, output)
		return output
