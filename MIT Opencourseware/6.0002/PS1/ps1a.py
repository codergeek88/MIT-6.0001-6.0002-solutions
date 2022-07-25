###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows_dict = {}
    # opening file (using with statement will automatically close file when statement ends)
    with open(filename) as text_file:
        for line in text_file:
            # converting a line in txt file to tuple in format: [cow name, weight]
            temp_list = line.split(",")
            # converting tuple format into dictionary format with cow name (string) weight (int) pairs
            cows_dict[temp_list[0]] = int(temp_list[1])
    return cows_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    total_list = []
    # creating list of name-weight pairs sorted by weight
    sorted_list = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    smallest_weight = sorted_list[-1][1]
    # loop will end when no more cows can be sent on a trip
    while smallest_weight <= limit and sorted_list != []:
        trip_list = []
        avail_space = limit
        # for loop for each trip
        for pair in sorted_list:
            if avail_space < smallest_weight:
                break
            # adding only names whose weights are less than current available space on trip
            if pair[1] <= avail_space:
                trip_list.append(pair[0])
                avail_space -= pair[1]
        # removing all name_weight pairs from sorted_list for cows who are on the current trip
        sorted_list = [i for i in sorted_list if i[0] not in trip_list] 
        total_list.append(trip_list)
        # if statement needed because sorted_list[-1] will raise an IndexError for an empty sorted_list
        if sorted_list != []:
            # in case lowest weight cow has been picked, smallest_weight is reset to new lowest weight cow
            smallest_weight = sorted_list[-1][1]
    return total_list

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    values_list = list(cows) #creating list of cow names
    for partition in get_partitions(values_list):
        # checking if all trips contain less than 10 tons 
        for subset in partition:
            subset_sum = 0
            for element in subset:
                subset_sum += cows[element]
            if subset_sum > limit:
                break
        else:
            return partition
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    filename = "ps1_cow_data_2.txt"
    cows = load_cows(filename)
    
    greedy_start = time.time()
    greedy_result = greedy_cow_transport(cows)
    greedy_end = time.time()
    greedy_trip_len = len(greedy_result)
    greedy_time_len = greedy_end - greedy_start
    
    brute_force_start = time.time()
    brute_force_result = brute_force_cow_transport(cows)
    brute_force_end = time.time()
    brute_force_trip_len = len(brute_force_result)
    brute_force_time_len = brute_force_end - brute_force_start
    
    print("greedy number of trips:", greedy_trip_len)
    print("greedy time:", greedy_time_len)
    print()
    print("brute force number of trips:", brute_force_trip_len)
    print("brute force time:", brute_force_time_len)

cows = load_cows("ps1_cow_data_2.txt")
print(cows)
print()
print(greedy_cow_transport(cows))
print(brute_force_cow_transport(cows))
print()
compare_cow_transport_algorithms()
    
    
    
    