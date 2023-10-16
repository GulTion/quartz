---
type: ShortNotes
subject: DS
repeation: 7
last_time: 2023-10-16T00:00:00.000+05:30
---


#  Sorting #notes/ALGO/sorting 
## Bubble Sort #notes/ALGO/sorting/bubble_sort


![Bubble Sort](https://cdn.emre.me/sorting/bubble_sort.gif)

### Implementation

```python
def bubble_sort(array):
    # We set swapped to True so the loop runs at least once
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Swap the elements
                array[i], array[i + 1] = array[i + 1], array[i]
                # Set the flag to True so we'll loop again
                swapped = True

    return array
```

## Selection Sort #notes/ALGO/sorting/selection_sort

![Selection Sort](https://cdn.emre.me/sorting/selection_sort.gif)

### Implementation

```python
def selection_sort(array):
    for i in range(len(array)):
        # We assume that the first item of the unsorted segment is the smallest
        min_value = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_value]:
                min_value = j

        # Swap values of the lowest unsorted element with the first unsorted element
        array[i], array[min_value] = array[min_value], array[i]

    return array
```

## Insertion Sort #notes/ALGO/sorting/insertion_sort

![Insertion Sort](https://cdn.emre.me/sorting/insertion_sort.gif)

### Implementation

```python
def insertion_sort(array):
    # We assume that the first item is sorted
    for i in range(1, len(array)):
        picked_item = array[i]

        # Reference of the index of the previous element
        j = i - 1

        # Move all items to the right until finding the correct position
        while j >= 0 and array[j] > picked_item:
            array[j + 1] = array[j]
            j -= 1

        # Insert the item
        array[j + 1] = picked_item

    return array
```

## Merge Sort

![Merge Sort](https://cdn.emre.me/sorting/merge_sort.gif)

### Implementation

```python
def merge_sort(array):
    # If the list is a single element, return it
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    # Recursively sort and merge each half
    l_list = merge_sort(array[:mid])
    r_list = merge_sort(array[mid:])

    # Merge the sorted lists into a new one
    return _merge(l_list, r_list)


def _merge(l_list, r_list):
    result = []
    l_index, r_index = 0, 0

    for i in range(len(l_list) + len(r_list)):
        if l_index < len(l_list) and r_index < len(r_list):

            # If the item at the beginning of the left list is smaller, add it to the sorted list
            if l_list[l_index] <= r_list[r_index]:
                result.append(l_list[l_index])
                l_index += 1

            # If the item at the beginning of the right list is smaller, add it to the sorted list
            else:
                result.append(r_list[r_index])
                r_index += 1

        # If we have reached the end of the of the left list, add the elements from the right list
        elif l_index == len(l_list):
            result.append(r_list[r_index])
            r_index += 1

        # If we have reached the end of the of the right list, add the elements from the left list
        elif r_index == len(r_list):
            result.append(l_list[l_index])
            l_index += 1

    return result
```

## Time Complexities of Sorting Algorithms


|Algorithm|Time Complexity (**Best**)|Time Complexity (**Average**)|Time Complexity (**Worst**)|Space Complexity|
|---|---|---|---|---|
|Bubble Sort|O(n)|O(n2)|O(n2)|O(1)|
|Selection Sort|O(n2)|O(n2)|O(n2)|O(1)|
|Insertion Sort|O(n)|O(n2)|O(n2)|O(1)|
|Merge Sort|O(n log(n))|O(n log(n))|O(n log(n))|O(n)|
|Heap Sort|O(n log(n))|O(n log(n))|O(n log(n))|O(1)|
|Quick Sort|O(n log(n))|O(n log(n))|O(n2)|O(log(n))|
|Radix Sort|O (nk)|O(nk)|O(nk)|O(n+k)|
|Tim Sort|O(n)|O(n log(n))|O(n log(n))|O(n)|

