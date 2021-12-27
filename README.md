# **Ex3**


### :pushpin: Implementation of a data structure of a weighted and directed graph in Python

int this project we implements a data structure of a weighted and directed graph in Python,
the implementation includes a class of graphs and a class of algorithms on graphs.

This project is built on our previous Ex2 project: Design and implementation of directed and weighted graphs in Java.
this program can lode directional graphs and perform the following functions:

- **isConnected** - will returns true if and only if there is a valid path from each node to each other node
- **shortestpath** - Computes the length of the shortest path between src to dest 
- **Center** - Finds the node that has the shortest distance to it's farthest node.
  return The nodes id, min-maximum distance.
- **TSP** - Computes a list of consecutive nodes which go over all the nodes in cities the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution the lower the better.

During the README you can see the comparisons to our solution performance for our implementation in java.

 ## Part 1️⃣: 
 ### DiGraph inheritance GraphInterface:
 | Methods  | Details |
| ------------- | ------------- |
| `v_size(self)` |Returns the number of vertices in this graph|
| `e_size(self)` |Returns the number of edges in this graph |
| `get_all_v(self)` |return a dictionary of all the nodes in the Graph|
| `all_in_edges_of_node(self, id1: int)` |return a dictionary of all the nodes connected to (into) node_id ,each node is represented using a pair (other_node_id, weight)|
| `all_out_edges_of_node(self, id1: int)` |return a dictionary of all the nodes connected from node_id , each node is represented using a pair (other_node_id, weight)|
| `get_mc(self)` |Returns the current version of this graph|
| `add_edge(self, id1: int, id2: int, weight: float)` |Adds an edge to the graph|
| `add_node(self, node_id: int, pos: tuple = None)` | Adds a node to the graph|
| `remove_node(self, node_id: int)` | Removes a node from the graph|
| `remove_edge(self, node_id1: int, node_id2: int)` |Removes an edge from the graph|

 ## Part 2️⃣:
 ### GraphAlgo inheritance GraphAlgoInterface:
 Realization of the department that inherits from the (abstract) GraphAlgoInterface department

  | Methods  | Details |
| ------------- | ------------- |
| `get_graph(self)` |return: the directed graph on which the algorithm works on |
| `load_from_json(self, file_name: str)`| Loads a graph from a json file |
| `save_to_json(self, file_name: str)`| Saves the graph in JSON format to a file |
| `shortest_path(self, id1: int, id2: int)` | Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm |
| `path(self, id1: int, key: int)` | help function to shortest_path , if the Key different from 1 returns the maximum distance for the center| 
| `TSP(self, node_lst: List[int])` | Finds the shortest path that visits all the nodes in the list |
| `help_tsp(self, id1, id2)` | Help function returns a list | 
| `is_connected(self)` | Checking that the graph is linked |
| `revers(self)` | help function to is_connected , revers the graph |
| `centerPoint(self)` | Finds the node that has the shortest distance to it's farthest node |
| `plot_graph(self)` | show the graph |

During the project: 
- **isConnected** - we used BFS algorithm and after we reverse the BFS.
- **shortest_path** -  we used dykstra algorithm. 
- **TSP** - we used in function shortest_path. 
- we implemented the object **Node**. 
 
 ## Part 3️⃣: 
 graph A0: 
 
 
 ![WhatsApp Image 2021-12-27 at 15 49 09](https://user-images.githubusercontent.com/93201414/147477865-64892bf5-e280-4aec-896d-d7a3df6b8250.jpeg)


Analysis of the performance of our algorithm On graphs size 1000, 10000, 1000000, 1000000 : 

### isConnected():
1000: 0.007sec

10000: 80ms 

100000: 15sec 875ms

1000000000: time out

### shortestPath:
1000: 0.104sec

10000: 9sec 654ms

100000:timeout

1000000000:time out

### center:
1000: 1min 49sec

10000: time out

100000: time out

1000000000: time out

### tsp:
1000: 0.51sec

10000: 52sec 746ms

100000: time out

1000000000: time out

### save:
1000: 0.148sec 

10000: 1sec 376ms

100000: 56sec 394ms

1000000000: time out

### load:
1000: 0.02sec

10000: 189ms

100000: 13sec 594ms

1000000000: time out

### get graph:
1000: 0.02sec

10000: 15ms

100000: 249ms

1000000000: time out


