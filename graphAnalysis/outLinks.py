import networkx as nx
import matplotlib.pyplot as plt

if __name__=='__main__':

	G=nx.DiGraph()
	G = nx.read_gexf("./torGraph.dat")

	numbers = []
	rangeOfNumbers = []
	x = []

	for n in G.nodes_iter():
		numbers.append(G.in_degree(n))					#calculate the out-degree for each node
		if(G.out_degree(n) not in rangeOfNumbers):
			rangeOfNumbers.append(G.out_degree(n))
	
	rangeOfNumbers.sort()

	for n in rangeOfNumbers:
		x.append(numbers.count(n))					#create a list with the number of nodes for each out-degree

	plt.scatter(rangeOfNumbers,x, label = ' out-degree', color ='k')	#print a scatter with the out-degree distribution

	plt.xlim(0,30)
	plt.ylim(0,10000)

	plt.yticks([0,1000,10000,50000])
	plt.xticks([0,10,20,30])

	plt.xlabel('out-links')
	plt.ylabel('numberOfNodes')

	plt.title('out-degree distribution')
	plt.legend()

	plt.show()
