# 🏆 Dominant Cells in a Grid - Python Solution  

## **📌 Problem Statement**  
A **dominant cell** in a 2D grid is a cell that has a **strictly greater value** than all of its **neighboring** cells.  
A cell’s **neighbors** are those that share a side or corner, meaning each cell can have up to **8 neighbors**.  

The goal is to **find the number of dominant cells in the grid**.

---

## **🔹 Input Format**
```plaintext
n   # Number of rows  
m   # Number of columns  
grid values (n rows, m columns)  

## **🔹 Sample Input**
3
3
1 2 7
4 5 6
8 8 9

## **🔹 Sample Output*
2

🚀 Solution Approach

✅ Used directional vectors to efficiently check all 8 neighbors.
✅ Optimized grid traversal with O(nm) complexity.
✅ Handled edge cases for grid boundaries (corner, edge, and inner cells).

 How to Run the Code?
commmand:
python dominant_cells.py








