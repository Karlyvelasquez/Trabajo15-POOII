class Algoritmos:
    @staticmethod
    def quicksort(arr, key=None):
        if key is None:
            key = lambda x: x
        if len(arr) <= 1:
            return arr
        pivot = key(arr[len(arr) // 2])
        left = [x for x in arr if key(x) < pivot]
        middle = [x for x in arr if key(x) == pivot]
        right = [x for x in arr if key(x) > pivot]
        return Algoritmos.quicksort(left, key) + middle + Algoritmos.quicksort(right, key)

    @staticmethod
    def mergesort(arr, key=None):
        if key is None:
            key = lambda x: x
        if len(arr) <= 1:
            return arr

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if key(left[i]) < key(right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        mid = len(arr) // 2
        left_half = Algoritmos.mergesort(arr[:mid], key)
        right_half = Algoritmos.mergesort(arr[mid:], key)
        return merge(left_half, right_half)