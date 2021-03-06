import json
import pygraphviz as pg
import networkx as nx
import matplotlib.pyplot as plt


#this method creates the non directed graph by using two input files, one for each crawl

def loadgraph(fname, fname2):   

        G=nx.Graph()
	
	i = 0
	G.add_node("http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page")	#addition of the first node

	for line in open(fname):						#for each line of the JSON file, the url and the referer are added only if there is a previous reference in the graph
	    i = i+1
	    print i
	    j=json.loads(line)
	    url=j["url"]
	    referer=j["referer"]	    
	    if(referer in G):
	    	G.add_node(url)
		G.add_edge(referer,url)
	i = 0

	for line in open(fname):						#once all the urls and referers are in the graph, the linked urls are added
		    i = i+1
		    print i	
		    j=json.loads(line)
		    url=j["url"]
		    referer=j["referer"]
		    try:
		    	for linked_url in j["linkedurls"]:
				if(len(linked_url)<150):
					G.add_edge(url,linked_url)
		    except KeyError, e:
				k=0

	i = 0

	for line in open(fname2):
	    i = i+1
	    print i
	    j=json.loads(line)
	    url=j["url"]
	    referer=j["referer"]	    
	    if(referer in G):
	    	G.add_node(url)
		G.add_edge(referer,url)
	i = 0

	for line in open(fname2):
	    i = i+1
	    print i	
	    j=0
	    j=json.loads(line)
	    url=j["url"]
	    referer=j["referer"]
	    try:
	    	for linked_url in j["linkedurls"]:
			G.add_edge(url,linked_url)
	    except KeyError, e:
			k=0	

	
        return G


#main method, invocates the method to create the graph and prints the basic properties of the graph, and the connectivity info

if __name__=='__main__':

        G=loadgraph("./rawData_1.json", "./rawData_2.json")
	nx.write_gexf(G, "./torGraph.gexf")

 	print nx.info(G)
	print nx.is_connected(G)
	print nx.number_connected_components(G)



