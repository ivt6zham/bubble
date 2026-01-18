import random

words_pool = ["яблуко", "банан", "груша", "апельсин", "ківі", "слива", "манго"]

data = [random.randint(1, 100) if random.random() < 0.5 else random.choice(words_pool) for _ in range(20)]

print("Масив до сортування:")
print(data)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

numbers = [x for x in data if isinstance(x, int)]
words = [x for x in data if isinstance(x, str)]

sorted_numbers = bubble_sort(numbers)
sorted_words = bubble_sort(words)

sorted_data = sorted_numbers + sorted_words
print("\nМасив після сортування:")
print(sorted_data)