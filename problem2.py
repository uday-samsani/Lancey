# Problem 2: Accumulate
# Implement the accumulate operation, which, given a collection and an operation to perform
# on each element of the collection, returns a new collection containing the result of applying
# that operation to each element of the input collection.

# Example:
# Input: collection = [1, 2, 3], operation = lambda x: x * 2
# Output: [2, 4, 6]

def accumulate(collection, operation):
    return [operation(x) for x in collection]

def main():
    collection = [1,2,3,4,5]
    result = accumulate(collection, lambda x: x*x)
    print(f"Original collection: {collection}")
    print(f"Accumulated collection: {result}")

if __name__ == "__main__":
    main()