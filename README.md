# Tor data extractor

Repository of the final project of the Computer Science degree.

The tool is composed by a crawler and a graph analyzer. The crawler (dataExtractor folder) extracts pages from the Tor Web and stores it in graph format. The graph analyzer (grapghAnalysis folder) takes as input the files generated by the crawler and gets information about its parameters. It is able to apply algorithms to the Tor graph.

To make it work (Ubuntu 12.04 and above) the user should follow the next instructions:

1. Install Python, Scrapy, the Tor client and Polipo on your system.
2. Download the folder dataExtractor from the repository. 
3. You should be able to execute the crawler by typing 'scrapy crawl dataExtractor'.
4. The crawler will extract pages until it has no more links to follow or the user press CTRL+D.
5. The extracted data is stored in \tmp folder on your system.
6. That file is the input for the graph analyzer, download the folder from the repository and store the extracted data file in that folder. 
7. Execute the createGraph.py script. It will generate a .gexf file that will be the input for the rest of the scripts of that folder.
8. Execute the desired script, each one apply an algorithm to the extracted graph.
