import networkx as nx
import matplotlib.pyplot as plt


if __name__=='__main__':

	G=nx.DiGraph()
	G = nx.read_gexf("./torGraph.dat")

	sizes = []
	rangeOfSizes = []
	x = []

	for h in nx.strongly_connected_component_subgraphs(G):			#get the size of each strongly connected component of the main graph
		sizeAux = h.size()
		sizes.append(sizeAux)
		if(sizeAux not in rangeOfSizes):
			rangeOfSizes.append(sizeAux)

	rangeOfSizes.sort()

	for n in rangeOfSizes:
		print n								#create a list with the number of components for each size
		x.append(sizes.count(n))

	

	plt.scatter(rangeOfSizes,x, marker='.',label =' WCC-size', color ='k')	#create a scatter with the distribution of the size of the SCC

	giant = max(nx.strongly_connected_component_subgraphs(G),key = len)	#print the size of the biggest strongly connected component
	print giant.size	

	plt.xlim(0,1000000)
	plt.ylim(0,5000)

	plt.xticks([0,1000,10000,100000,1000000])
	plt.yticks([0,1000,2000,3000,4000,5000])

	plt.xlabel('Size')
	plt.ylabel('Number of components')
	plt.title('WCC sizes ditribution')

	plt.legend()
	plt.show()





























