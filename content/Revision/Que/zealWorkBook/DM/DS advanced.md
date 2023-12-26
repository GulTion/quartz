---
atQ: 10
type: zealWorkBook
subject: DM
---

# row-order and column order #notes/DS/ArrayConsider the following C programming statements: 
[Assume update on variable is an atomic statement]

## 3D

B = Base Address (start address)  \n
W = Weight (storage size of one element stored in the array) \n
M = Row (total number of rows)  
N = Column (total number of columns)  
P = Width (total number of cells depth-wise)  
x = Lower Bound of Row  
y = Lower Bound of Column  
z = Lower Bound of Width 

### row-order
$$A[i][j][k]= B + W\cdot(M\cdot N(i – x) + N(j – y) + (k – z))$$
### Column order
$$A[i][j][k]= B + W \cdot (M \cdot N(i – x) + M\cdot(k – z) + (j – y))$$


## 2D
![[Pasted image 20230925120207.png]]


# Comparison of function Asymptotically 
#notes/algo/asymptotic/comparison
![[Pasted image 20230925111904.png]] new way to think about f1 and f3, f5 and f6,they are same, when we will give log both side

#  relationship between E and V based on the type of graph 
#notes/DS/Graph/E_and_V_relation
 ![[Pasted image 20230925112813.png]]
