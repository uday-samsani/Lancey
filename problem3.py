# Problem 3: Domino
# Given list of dominos like [1|2] [3|1] [2|3]
# Compute a way to order a given set of dominoes in such a way that they form a correct domino chain
# (the dots on one half of a stone match the dots on the neighboring half of an adjacent stone) and
# that dots on the halves of the stones which don't have a neighbor (the first and last stone) match each other.

# Example:
# Input: [2|1], [2|3] and [1|3]
# Output: `[1|2] [2|3] [3|1]` or `[3|2] [2|1] [1|3]` or `[1|3] [3|2] [2|1]`
# etc, where the first and last numbers are the same.

# Input: [1|2], [4|1] and [2|3]
# Output: [4|1] [1|2] [2|3] first and last numbers are not the same.

# Assumption: I am given tuple
dominoes_graph ={}

def build_dominoes_graph(dominoes):
    for domino in dominoes:
        a, b = domino
        if a not in dominoes_graph:
            dominoes_graph[a] = None
        if b not in dominoes_graph:
            dominoes_graph[b] = None
        dominoes_graph[a] = b

def check_domino(first_el, next_el, unvisited):
    print(first_el, next_el, unvisited)
    if next_el == first_el:
        if next_el in unvisited:
            return True
        else:
            return False
    unvisited.remove(next_el)
    if dominoes_graph[next_el] is None:
        return False
    return check_domino(first_el, dominoes_graph[next_el], unvisited)

def check_dominoes(dominoes):
    build_dominoes_graph(dominoes)
    print(check_domino(dominoes[0][0], dominoes[0][1], list(dominoes_graph.keys())))
    return check_domino(dominoes[0][0], dominoes[0][1], list(dominoes_graph.keys()))

def main():
    dominoes = [(4, 1), (3, 4), (2, 3), (1, 2)]
    result = check_dominoes(dominoes)
    print(result)
    if result:
        print("The dominoes can be arranged to form a correct chain.")
    else:
        print("The dominoes cannot be arranged to form a correct chain.")

if __name__ == "__main__":
    main()