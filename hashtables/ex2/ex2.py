#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Dictionary to store flight connections
    connections = {}

    # Iterate through tickets, saving sources as keys in dictionary
    # and destinations as values
    for ticket in tickets:
        connections[ticket.source] = ticket.destination

    # Route list to return the path taken
    route = []

    # Start at source = None and append destinations until None found
    step = connections["NONE"]

    for ticket in tickets:
        route.append(step)
        step = connections[step]

    return route
