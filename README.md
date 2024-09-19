8 queens:
ALOGRITHM:
Initialize the Board:
Create an 8x8 chessboard initialized to 0, where 0 represents an empty cell.
Define Safe Function:
Create a function is_safe(board, row, col) that checks if it's safe to place a queen at position (row, col) by ensuring:
No queen exists in the same row to the left.
No queen exists in the upper diagonal to the left.
No queen exists in the lower diagonal to the left.
Recursive Backtracking:
Create a recursive function solve_n_queens(board, col) that solves the problem for one column at a time:
Base Case: If all queens are placed (col == 8), return True (problem solved).
Iterate over Rows: For the current column col, try placing a queen in each row row one by one:
Check if placing the queen in (row, col) is safe using the is_safe function.
If placing the queen is safe:
Place the queen by marking board[row][col] = 1.
Recursively attempt to place queens in the next column by calling solve_n_queens(board, col + 1).
If the recursive call returns True, the current placement is correct; propagate True.
If the recursive call returns False, backtrack by removing the queen from (row, col) (mark board[row][col] = 0).
If no valid row is found for the current column, return False to backtrack.
Initial Call:
Start by calling solve_n_queens(board, 0) for the first column and proceed recursively.
Solution Found:
If the function returns True, print or store the chessboard solution.
If no solution is possible, return a failure message.

Water jug:
Algorithm:
1.Define States and Actions: • Each state can be defined as the amount of water in Jug 1 and Jug 2, i.e., (a, b) where a is the amount in Jug 1 and b is the amount in Jug 2. • The possible actions (state transitions) are:
Fill Jug 1 (set a = x)
Fill Jug 2 (set b = y)
Empty Jug 1 (set a = 0)
Empty Jug 2 (set b = 0)
Pour water from Jug 1 to Jug 2 (Pour as much as possible, without exceeding the capacity of Jug 2)
Pour water from Jug 2 to Jug 1 (Pour as much as possible, without exceeding the capacity of Jug 1) 2.Initialize the Search: • Start with both jugs empty: (0, 0). • Create a queue (for BFS) and add the initial state (0, 0) to it. • Maintain a set of visited states to avoid revisiting the same state. 3.Breadth-First Search (BFS) Process: • While the queue is not empty, do the following:
Dequeue the front element from the queue. Let this be the current state (a, b).
Check if this state equals the goal (z, ) or (, z) where one of the jugs contains exactly z liters of water.
If it does, the solution is found, and you can stop.
Otherwise, generate all possible new states by applying each of the 6 possible actions to (a, b) (fill, empty, pour).
For each new state, if it hasn’t been visited before, add it to the queue and mark it as visited. 4.Checking for a Solution: • If you find a state where either Jug 1 or Jug 2 contains exactly z liters of water, you have a solution. • If the queue is exhausted without finding a solution, it means it is impossible to measure z liters using the given jugs.

CyptoArithmetic:
Algorithm:
Understand the Problem: Each letter in the problem represents a unique digit (0-9). The number represented by the letters must satisfy the given arithmetic operation. For example, in the problem: SEND + MORE = MONEY You need to determine which digit each letter (S, E, N, D, M, O, R, Y) represents.
Identify Unique Letters: List all the unique letters involved in the problem. In the example above, the unique letters are: S, E, N, D, M, O, R, Y.
Determine Constraints: The first letter in a number cannot represent 0 (for example, S and M cannot be 0). Some letters may have additional constraints based on the operation (such as possible carries).
Use Trial and Error (Backtracking): Assign digits to letters and check if the assignment satisfies the equation. Start by assigning digits to letters and calculating the resulting numbers. Ensure that each letter has a unique digit.
Check Consistency: After each digit assignment, check whether the partial equation still holds. For example, when calculating SEND + MORE = MONEY, check the last digits (D + E = Y) first, and then proceed from right to left, ensuring each partial sum is correct, including any carry values.
Backtrack if Necessary: If a contradiction is found (e.g., the sum doesn’t match or the same digit is assigned to two letters), backtrack by undoing the last assignment and trying a new digit. This systematic approach is called backtracking, where you explore different digit combinations until a valid solution is found.
Optimize with Known Constraints: Use constraints to reduce the number of digit assignments you need to try. For example, in SEND + MORE = MONEY, since the sum is 5 digits long, M must be 1 (because the sum of two 4-digit numbers can only give a 5-digit number if the first digit is 1).
Repeat Until a Solution is Found: Continue assigning digits and checking until you find the unique combination that satisfies the equation. You can also verify the solution by plugging the assigned digits back into the original equation.

A star algorithm:
Algorithm:
1.Initialization: • Create Open and Closed Sets: o Open Set: A priority queue or min-heap containing nodes to be evaluated, initialized with the start node. o Closed Set: A set of nodes that have already been evaluated. • Initialize Costs: o g_cost for each node: The cost from the start node to the current node. o f_cost for each node: The estimated total cost (g_cost + h_cost). o h_cost: The heuristic estimate from the current node to the goal node. • Set Start Node Costs: o g_cost of the start node to 0. o f_cost of the start node to its h_cost. 2.Algorithm Execution: • While the Open Set is not Empty:
Select the Node with the Lowest f_cost:  Dequeue the node with the lowest f_cost from the Open Set. This node is called current_node.
Check for Goal:  If current_node is the goal node, reconstruct the path from start to goal and return it.
Move Node to Closed Set:  Add current_node to the Closed Set.
Evaluate Neighbors:  For each neighbor of current_node:  If the Neighbor is in the Closed Set:  Skip it as it has already been evaluated.  Calculate Costs:  Calculate the tentative g_cost (i.e., g_cost of current_node plus the cost to reach the neighbor).  If the neighbor is not in the Open Set or the new g_cost is lower than its current g_cost:  Update the g_cost and f_cost of the neighbor.  Set the current_node as the parent of the neighbor (for path reconstruction).  If the neighbor is not in the Open Set, add it to the Open Set.
Continue Until Path is Found or Open Set is Empty:  If the Open Set becomes empty without finding the goal, report that there is no path. 3.Path Reconstruction: • Once the goal node is reached, reconstruct the path from the start node to the goal node by following parent pointers from the goal node back to the start node.

Depth First Search:
Algorithm:
1.Initialization: • Create a Set for Visited Nodes: Initialize an empty set or list to keep track of visited nodes. 2.Recursive DFS Function: • Start from a Node: o Mark the current node as visited. o Process the current node. o For each unvisited neighbor of the current node, recursively call DFS on that neighbor. 3.Termination: • The recursion ends when all reachable nodes from the starting node have been visited.

Colour mapping:
Algorithm:
Initialization: Create a data structure (e.g., a list) to store the color assigned to each node. Initially, no colors are assigned (e.g., all values are 0). Choose the number of colors m to use for coloring the map. Define a Function to Check Validity: Create a function is_safe(node, color) that checks whether it is safe to assign a particular color to node. The function ensures that none of the node’s neighbors (connected nodes) have the same color. Backtracking Algorithm to Assign Colors: Start at the first node. For each node, try assigning each color from 1 to m. Check if the Color is Valid: Use the is_safe function to check whether the color can be assigned to the current node without conflict. Recursive Call: If the color is valid, assign it to the node and recursively call the function for the next node. Backtrack: If assigning a color to a node leads to a conflict later, reset the color of the current node (backtrack) and try a different color. If all nodes are colored successfully, return the color assignments. If no solution is possible, backtrack to the previous node and try again. Termination: The algorithm terminates when either: All nodes are successfully assigned colors (in which case, a valid coloring is found). No valid color assignments are possible, meaning the map cannot be colored with the given number of colors.

Travelling salesman:
Algorithm:
1.Define the Problem: • Given a list of cities and a distance matrix, calculate all possible paths that start from one city, visit all other cities exactly once, and return to the starting city. 2.Generate Permutations: • Generate all possible permutations of the cities. 3.Calculate the Path Distance: • For each permutation (tour), calculate the total distance by summing the distances between consecutive cities in the permutation, including the distance back to the starting city. 4.Select the Shortest Path: • Keep track of the permutation that gives the minimum distance. 5.Return the Shortest Path: • After all permutations are checked, return the path with the minimum distance.

Tic tac toe:
Algorithm:
1.Initialize the Game Board: o Create a 3x3 grid (usually represented by a 2D list or array) where each cell can be empty, "X", or "O". o The board starts with all cells empty. 2.Choose Starting Player: o Decide which player will go first (Player 1 as "X" and Player 2 as "O"). 3.Loop Through Player Turns: o Player Input: On each turn, the current player selects an empty cell to place their mark ("X" or "O"). o Validate Input: Ensure that the selected cell is empty. If it is not, ask the player to pick another cell. 4.Update the Board: o Place the current player's mark ("X" or "O") on the chosen cell. 5.Check for a Winner: o After each move, check if the current player has won the game by:  Checking all rows to see if any row has the same mark.  Checking all columns to see if any column has the same mark.  Checking both diagonals to see if either diagonal has the same mark. 6.Check for a Draw: o If no player wins and all cells are filled, the game is a draw. 7.Switch Players: o Switch to the other player after each valid move. 8.Repeat Steps 3-7 Until the Game Ends: o The game ends when there is a winner or when there is a draw. 9.Announce Result: o Announce the winner or declare a draw.

Decision Tree:
Algorithm:
1.Start with the Entire Dataset: At the root node, consider the entire dataset with all features and target values. 2.Select the Best Feature to Split: For each feature, evaluate a splitting criterion to determine how to best split the dataset: 3.For Classification: Use Information Gain based on Entropy or Gini Impurity to find the feature that provides the best classification. Information Gain (IG) measures the reduction in entropy after a dataset is split on a particular feature. Gini Impurity measures the probability of incorrectly classifying a randomly chosen element if it was labeled according to the class distribution. 4.For Regression: Use Variance Reduction or Mean Squared Error (MSE) as the splitting criterion to find the feature that best reduces the variance in the target variable. 5.Split the Dataset: Divide the dataset into subsets based on the selected feature and its possible values or threshold (for continuous features). 6.Create Child Nodes: Create a new node for each subset resulting from the split. The subset of data at each child node now becomes the input for the next iteration. 7.Repeat Recursively: For each child node, repeat steps 2-4 on the respective subset of data. Continue this process recursively for each subset until one of the stopping criteria is met: All instances in the node belong to the same class (for classification). The target variable's values are very similar (for regression). No more features are available for splitting. A specified maximum depth is reached. 8.Assign Class or Value to Leaf Nodes: Once a stopping condition is reached, assign a class label (for classification) or the mean of the target values (for regression) to the leaf node. 9.(Optional) Pruning the Tree: To prevent overfitting, you may perform pruning: Pre-pruning: Stop the tree from growing by limiting its depth or by specifying a minimum number of samples required for a split. Post-pruning: Build the entire tree, then remove parts that have little contribution to improving accuracy.

Alpha-beta pruning:
Algorithm:
1.Start at the Root of the Tree: Begin with the root node and initialize two variables: Alpha (α): Initialized to negative infinity (-∞) for the maximizing player. Beta (β): Initialized to positive infinity (+∞) for the minimizing player. 2.Traverse the Tree Using Minimax: The algorithm traverses the game tree, exploring all possible moves, alternating between maximizing and minimizing layers. Evaluate Each Node (Recursively Apply Minimax): For each node, apply the Minimax algorithm with alpha and beta values passed down the tree: 3.Maximizing Player's Turn: Try to maximize the score by choosing the best available move. 4.For each child node: Evaluate the node using the Minimax algorithm. Update the alpha (α) value if the current node's value is greater than the current α. If α ≥ β at any point, stop further exploration of this branch (prune the branch), since the minimizing player won't allow this move to happen. 5.Minimizing Player's Turn: Try to minimize the score by choosing the best available move. 6.For each child node: Evaluate the node using the Minimax algorithm. Update the beta (β) value if the current node's value is less than the current β. If β ≤ α at any point, stop further exploration of this branch (prune the branch), since the maximizing player won't allow this move to happen. 7.Update Alpha and Beta: As the tree is traversed, the alpha and beta values are updated at each node based on the current best scores for the maximizing and minimizing players. 8.Prune the Branch: Prune (skip the evaluation of) a branch when: Maximizing Player: When the value of the current node is greater than or equal to beta (i.e., α ≥ β). This means the minimizing player would never choose this move, so we can stop searching this branch. Minimizing Player: When the value of the current node is less than or equal to alpha (i.e., β ≤ α). This means the maximizing player would never choose this move, so this branch can be pruned. 9.Return the Best Value: After evaluating all possible moves and pruning unnecessary branches, return the best value (either maximum or minimum depending on the turn) to the parent node. 10.End the Algorithm: The process continues until the entire tree is traversed or pruned. The value returned by the root node is the best move for the maximizing player.

Feet forward:
Algorithm:
Initialize the Network: Randomly initialize the weights and biases of the network. These values are often set to small random numbers, and the biases can be initialized to zeros. Input the Data: Pass the input data to the input layer of the neural network. Each input corresponds to a neuron in the input layer. Feedforward Process: Perform the following steps for each layer, moving from the input layer to the output layer: For each layer
𝑙 l (starting from layer 1): a. Compute the weighted sum of inputs: For each neuron 𝑖 i in the current layer: 𝑧 𝑖 ( 𝑙 )
∑ 𝑗
1 𝑛 𝑤 𝑖 𝑗 ( 𝑙 ) ⋅ 𝑎 𝑗 ( 𝑙 − 1 ) + 𝑏 𝑖 ( 𝑙 ) z i (l)​
j=1 ∑ n​w ij (l)​⋅a j (l−1)​+b i (l)​
𝑧 𝑖 ( 𝑙 ) z i (l)​is the weighted sum of inputs for neuron 𝑖 i in layer 𝑙 l. 𝑤 𝑖 𝑗 ( 𝑙 ) w ij (l)​is the weight from neuron 𝑗 j in the previous layer to neuron 𝑖 i in the current layer. 𝑎 𝑗 ( 𝑙 − 1 ) a j (l−1)​is the activation of neuron 𝑗 j in the previous layer. 𝑏 𝑖 ( 𝑙 ) b i (l)​is the bias for neuron 𝑖 i in layer 𝑙 l. b. Apply the activation function:
For each neuron 𝑖 i, apply the activation function to the weighted sum: 𝑎 𝑖 ( 𝑙 )
𝜎 ( 𝑧 𝑖 ( 𝑙 ) ) a i (l)​=σ(z i (l)​) 𝑎 𝑖 ( 𝑙 ) a i (l)​is the activation (output) of neuron 𝑖 i in layer 𝑙 l. 𝜎 σ is the activation function (such as ReLU, Sigmoid, or Tanh). Output Layer: After the feedforward process through all layers, the final layer (the output layer) produces the output of the network. For classification tasks, the output can be passed through a Softmax function to convert it into probabilities. Loss Function: Compute the loss based on the difference between the predicted output and the actual target values. The loss function depends on the task: Cross-entropy loss for classification tasks. Mean Squared Error (MSE) for regression tasks. Backpropagation (for training): If training the model, use the backpropagation algorithm to compute the gradients of the loss function with respect to the weights and biases. Update the weights and biases using an optimization algorithm like Stochastic Gradient Descent (SGD) or Adam. Repeat: Repeat steps 2-6 for multiple iterations (epochs) or until the model converges (loss stabilizes or decreases to a satisfactory level).
