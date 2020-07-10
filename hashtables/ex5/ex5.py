# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Dictionary to store file paths and last file/folder
    file_paths = {}

    # Iterate through the files
    for file in files:
        # # Split the file path on '/' and store the whole path
        # # as a key in file_paths and the last split as the value
        # file_paths[file] = file.split('/')[-1]

        # Split the file path on '/'
        f_split = file.split('/')
        # Check if the last split is a key in file_paths
        if f_split[-1] in file_paths:
            # If so, add the whole file path to the value list
            file_paths[f_split[-1]].append(file)
        # Otherwise, create a key with a list for value of the path
        else:
            file_paths[f_split[-1]] = [file]


    # Result list to store matches
    result = []

    # Iterate through the queries
    for query in queries:
        # Check if query is key in file_paths
        if query in file_paths:
            # Add the value list to result
            result += file_paths[query]


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
