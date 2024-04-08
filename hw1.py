# Problem 1
def PAD(N):
    # initializes the first three elements of the Padovan sequence.
    if N == 0 or N == 1 or N == 2:
        return 1
    # For N>2, calculate PAD(N) recursively.
    else:
        return PAD(N-2) + PAD(N-3)

# Probelm 2
def SUMS(N):
    # no additions are required, so the function returns 0.
    if N == 0 or N == 1 or N == 2:
        return 0
    # 
    else:
        return SUMS(N-2) + SUMS(N-3)

# Problem 3
def ANON(TREE):
    # Check if TREE is a tuple, indicating it is an internal node with children
    if type(TREE) is tuple:
        # Recursively apply ANON to each subtree
        return tuple(ANON(subtree) for subtree in TREE)
    else:
        # If TREE is not a tuple, it is a leaf node, replace it with '?'
        return '?'
    
# print(ANON(42))
# print(ANON("FOO"))
# print(ANON(((("L", "E"), "F"), "T")))
# print(ANON((5, "FOO", 3.1, -0.2)))
# print(ANON((1, ("FOO", 3.1), -0.2)))
# print(ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2))))
# print(ANON(("R", ("I", ("G", ("H", "T"))))))


# Problem 4
def TREE_HEIGHT(TREE):
    # Base case: If TREE is not a tuple, it is a leaf node, so its height is 0.
    if type(TREE) is not tuple:
        return 0
    # Recursive case: Compute the height of each subtree, add 1 for the current level,
    # and return the maximum height among all subtrees.
    else:
        return 1 + max(TREE_HEIGHT(subtree) for subtree in TREE)

# print(TREE_HEIGHT(1))
# print(TREE_HEIGHT((5, "FOO", 3.1, -0.2)))
# print(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)))
# print(TREE_HEIGHT(("R", ("I", ("G", ("H", "T"))))))


# Problem 5
def TREE_ORDER(TREE):
    # Base case: If TREE is an integer, return it as a tuple.
    if type(TREE) is int:
        return (TREE,)
    # Recursive case: TREE is a tuple (L, m, R).
    L, m, R = TREE
    return TREE_ORDER(L) + TREE_ORDER(R) + (m,)

# print(TREE_ORDER(42))
# print(TREE_ORDER(((1, 2, 3), 7, 8)))
# print(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100))))