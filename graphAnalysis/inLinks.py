import networkx as nx
import matplotlib.pyplot as plt

if __name__=='__main__':

	G=nx.DiGraph()
	G = nx.read_gexf("./torGraph.dat")

	numbers = []
	rangeOfNumbers = []
	x = []

	for n in G.nodes_iter():					#calculate the in-degree for each node
		numbers.append(G.in_degree(n))
		if(G.in_degree(n) not in rangeOfNumbers):
			rangeOfNumbers.append(G.in_degree(n))
	
	rangeOfNumbers.sort()

	for n in rangeOfNumbers:					#create a list with the number of nodes for each in-degree
		x.append(numbers.count(n))

	plt.scatter(rangeOfNumbers,x, label = ' in-degree', color ='k')	#print a scatter with the in-degree distribution

	plt.xlim(0,30)
	plt.ylim(0,10000)

	plt.yticks([0,1000,10000,50000])
	plt.xticks([0,10,20,30])

	plt.xlabel('in-links')
	plt.ylabel('numberOfNodes')
	plt.title('in-degree distribution')

	plt.legend()
	plt.show()
