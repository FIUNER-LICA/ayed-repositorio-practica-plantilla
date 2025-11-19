def bubble_sort(lis):
    n = len(lis)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if lis[j] > lis[j+1]:
                # Swap if they are in the wrong order
                lis[j], lis[j+1] = lis[j+1], lis[j]
                swapped = True
        # If no two elements were swapped, the array is sorted
        if not swapped:
            break
    return lis

# Example usage
if __name__ == "__main__":
    sample_lis = [64, 34, 25, 12, 22, 11, 90]
    sorted_lis = bubble_sort(sample_lis)
    print("Sorted array:", sorted_lis)