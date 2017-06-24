import urlparse
import networkx as nx

if __name__=='__main__':

	G = nx.DiGraph()
	G = nx.read_gexf("./torGraph.dat")

	n = 0
	onions = 0

	while(n<1000000):					#1 million nodes are randomly picked, and for each the urlparser checks if it is an onion service or not
		random_node = choice(visited_domains)	
		parsedNode = urlparse.urlparse(random_node)
		domain = str(parsedNode.netloc)
		extension = domain[-5:]

		if domain is 'onion':
			onions = onions + 1

	print onions
							#the number of .onion domain is printed, along with the percentage of the domains of Tor and the Web	
	percentOnions = onions/1000000
	percentOnions = percentOnions*100
	percentWeb = 100 - percentOnions

	print percentOnions
	print percentWeb
	
