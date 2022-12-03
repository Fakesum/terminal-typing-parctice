from english_words import english_words_set as words
import random

def timeit(f):
    import time
    a = time.time()
    res = f()
    return (res, time.time() - a)

test_length = 30
test_words = [random.choice(list(words)) for _ in range(test_length)]

list(filter((lambda word:print(word, end=" ")), test_words))
print("\n")

res,time = timeit(input)

def pressision(first, second):
    def levenshtein_distance(first, second):
        """Find the Levenshtein distance between two strings."""
        if len(first) > len(second):
            first, second = second, first
        if len(second) == 0:
            return len(first)
        first_length = len(first) + 1
        second_length = len(second) + 1
        distance_matrix = [[0] * second_length for x in range(first_length)]
        for i in range(first_length):
            distance_matrix[i][0] = i
        for j in range(second_length):
            distance_matrix[0][j]=j
        for i in range(1, first_length):
            for j in range(1, second_length):
                deletion = distance_matrix[i-1][j] + 1
                insertion = distance_matrix[i][j-1] + 1
                substitution = distance_matrix[i-1][j-1]
                if first[i-1] != second[j-1]:
                    substitution += 1
                distance_matrix[i][j] = min(insertion, deletion, substitution)
        return distance_matrix[first_length-1][second_length-1]
    return 100*levenshtein_distance(first, second) / float(max(len(first), len(second)))

print(time)
print("words typed,", len(test_words))

print("wpm:", (len(test_words) / time)*60,", correct %.2f of the time" % (100 -pressision(" ".join(test_words), res)))