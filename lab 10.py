#Bubble Sort Algorithm Using Classes and Methods

class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

    def get_sorted_data(self):
        return self.data
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort = BubbleSort(data)
bubble_sort.sort()
print("Bubble Sorted:", bubble_sort.get_sorted_data())

#Insertion Sort Algorithm Using Python

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
data = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(data)
print("Insertion Sorted:", data)

# Selection Sort Algorithm Using Python

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
data = [64, 34, 25, 12, 22, 11, 90]
selection_sort(data)
print("Selection Sorted:", data)

#Merge Sort Algorithm Using Python

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
data = [64, 34, 25, 12, 22, 11, 90]
merge_sort(data)
print("Merge Sorted:", data)

#Linear Search Algorithm Using Python

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
data = [64, 34, 25, 12, 22, 11, 90]
result = linear_search(data, 22)
print("Element found at index:", result)

#Binary Search Algorithm Using Python (Requires Sorted Array)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
data = [11, 12, 22, 25, 34, 64, 90]
result = binary_search(data, 22)
print("Element found at index:", result)

#Binary Tree Implementation Using Python

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.value:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)
bt = BinaryTree()
data = [50, 30, 20, 40, 70, 60, 80]
for d in data:
    bt.insert(d)

print("Inorder Traversal:")
bt.inorder(bt.root)