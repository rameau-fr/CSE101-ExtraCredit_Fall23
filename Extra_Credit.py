import random

def isSorted(lst):
    """ Check if the list is sorted in ascending order.
    
    Args:
        lst (list): The list to check for sorted order.
    
    Returns:
        bool: True if the list is sorted, False otherwise.
    """
    pass

def bogoSort(lst):
    """ Perform Bogo sort on a list.
    
    Args:
        lst (list): The list to be sorted.
    
    Returns:
        None: The list is sorted in place.
    """
    pass

def brickSort(lst):
    """ Perform Brick sort (Odd-Even sort) on a list.
    
    Args:
        lst (list): The list to be sorted.
    
    Returns:
        None: The list is sorted in place.
    """
    pass

def main():

    # test bogo sort
    lst = [9, 6, 1, 20, 100, 78, 19, 7, 22]
    bogoSort(lst)
    print('Bogo Sorted List:', lst)
    
    # test brick sort
    lst = [9, 6, 1, 20, 100, 78, 19, 7, 22]
    brickSort(lst)
    print('Brick Sorted List:', lst)
    
if __name__ == "__main__":
    main()
