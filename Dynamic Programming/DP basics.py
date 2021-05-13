# Dynamic programming is both an optimzation technique and a computer programming method.
# The main idea is that we can break down complicated problems into smaller subproblems in a recursive manner
# Then we find the solutions for these subproblems and finally we combine the subresults to find the final solution
# We solve each subproblems only once - we reduce the number of computations
# Subproblems can be stored in memory - memoization and tabulation
# Dynamic Programming Paradigm
# OPTIMAL SUBSTRUCTURE:
# A problem is said to have optimal substruture if an optimal solution can be constructed from optimal solutions of its subproblems
# BELLMAN-EQUATION:
# There is a relationship between the subresults and the final result - this is what the Bellman-equaion defines
# If a given problem has optimal substructure and overlapping subproblems then we can use dynamic programming approach
# MEMOIZATION AND TABULATION
# The problem of recursion is that we may solve the same subproblems multiple times. This can be eliminated by:
# 1.) Top-Down approach (Memoization)
# We can store the solutions of the subproblems in a table(priority queue for example)
# Whenever we try to solve a new subproblem we first check whether it is present in the table(so we have already solved that problem)
# 2.) Bottom-Up approach (Tabulation)
# We reformulate the original problem in a bottom-up fashion. We iteratively generate the subresults for larger and laarger subproblems
# DP and Divide and Conquer approaches:
# Several problems can be solved by combining optimal solutions to non-overlapping subproblems. This strategy is called divide and conquer method.
#