def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Dictionary for values
    vals = {}

    # Iterate through numbers in a
    for num in a:
        # Check if the absolute value of num is in vals
        if abs(num) in vals:
            # Increment the value associated with abs(a)
            vals[abs(num)] += 1
        else:
            # Otherwise, put absolute value of a into vals
            vals[abs(num)] = 1
    
    # List to put any results
    results = []

    # Look at key, value pairs in vals to find any values
    # that are 2, meaning they were counted twice and add
    # the key to results
    for k, v in vals.items():
        if v == 2:
            results.append(k)

    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
