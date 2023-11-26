# Quad Trees and N-Dimensional Quad Trees.

Andrew Hunter-Owega

230147039

CPSC 482

Project README

An implementation of a point-quad tree outlined in the paper by [1], as well as an N-dimensional quad tree.

## Dependencies

This project uses "treelib," created by Xiaming Chen, for illustration and testing.
The following is a screenshot from it's documentation on installation:

![image](https://github.com/ahunterow/CPSC482Project/assets/115964818/2282b7f4-4698-4bf4-b256-3387f003ca1f)

## Classes

Main:
  Main is a driver to run test code for NDNode and QNode.

NDNode:
  Represents a node in an N-Dimensional Quad Tree. Seeing as this is how we interact with the tree, deletion of the root is not allowed; however, this could easily be implemented with an external tree object.
  
QNode:
  Represents a node in a Quad Tree. Seeing as this is how we interact with the tree, deletion of the root is not allowed; however, this could easily be implemented with an external tree object.

qtreeTest:
  This is the output file to show the tree structure using the treelib library.

For additional information on the functions within, refer to each class. Above each function should be additional restrictions that apply for their use. Additionally, the paper also explains the inner workings of each function.

## Testing
  When testing, these classes were verified using two dimensional data. In the case of the NDNode, three dimensional data was also used. 

## Sources

[1] R. A. Finkel and J. L. Bentley, “Quad trees a data structure for retrieval on Composite Keys,” Acta Informatica, vol. 4, no. 1, pp. 1–9, Mar. 1974. doi:10.1007/bf00288933

treelib found at https://github.com/caesar0301/treelib
