def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Dict to save the complement of each num
    comp_dict = {}

    # Iterate through weights
    for i, num in enumerate(weights):
        # Check if the complement of num is in the dictionary
        if (limit-num) in comp_dict:
            # Return a tuple of indices for the two numbers
            return (i, comp_dict[limit-num])
        # If not, save the index of num in the dictionary
        comp_dict[num] = i

    return None
