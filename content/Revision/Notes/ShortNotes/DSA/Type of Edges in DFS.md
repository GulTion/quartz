---
subject: DSA
type: ShortNotes
status: Revision
sr-due: 2023-12-27
sr-interval: 12
sr-ease: 155
---
#note


![](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-drawing-2-4.jpg)

- **Tree Edge**: It is an edge which is present in the tree obtained after applying DFS on the graph. All the Green edges are tree edges. 
  
- **Forward Edge**: It is an edge (u, v) such that v is a descendant but not part of the DFS tree. An edge from **1 to 8** is a forward edge. 
	- **A forward edge can never lead to a cycle.**
  
- **Back edge**: It is an edge (u, v) such that v is the ancestor of node u but is not part of the DFS tree. Edge from **6 to 2** is a back edge. Presence of back edge indicates a cycle in directed graph
	- **A graph has a cycle if and only if there is a back edge.**  
	  
- **Cross Edge**: It is an edge that connects two nodes such that they do not have any ancestor and a descendant relationship between them. The edge from node **5 to 4** is a cross edge.

  
  - BFS
	  - Cross 
	  - Tree
  - DFS (directed)
	  - Forward
	  - Backward
	  - cross
	  - Tree
- DFS (undirected)
	- Backward
	- Tree