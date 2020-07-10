def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Create dictionary to store values of which set a number is in
    vals = {}

    # Iterate through the arrays in arrays
    for i, array in enumerate(arrays):
        # Go through each number in the array
        for num in array:
            # If that number is not in the dictionary
            if num not in vals:
                # Put it in with the index of the array in a list
                vals[num] = [i]
            else:
                # Otherwise, append the index to the list
                vals[num].append(i)
    
    # List of results to return
    result = []

    # Number of arrays
    arrays_len = len(arrays)

    # Look at the key, value pairs in vals dictionary
    for k, v in vals.items():
        # If the value list has as many elements as arrays passed in...
        if len(v) == arrays_len:
            # Put the key in the result list
            result.append(k)
              

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
