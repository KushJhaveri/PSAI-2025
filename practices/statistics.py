def median(collection: list) -> float:
    collection.sort()
    length = len(collection)

    if length % 2 == 1:
        return collection[length // 2]

    middle1 = collection[length // 2 - 1]
    middle2 = collection[length // 2]
    return (middle1 + middle2) / 2

def mean(collection: list) -> float: 
    return sum(collection) / len(collection)