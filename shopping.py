#!/bin/env python3

""" Shopping Module """

def shopping(s): # pylint: disable=invalid-name
    '''
    Purpose: Determine the number of purchases we can make with a budget of 10000.
    Constraints: The first purchase should not count towards the number of purchases.
    '''

    purchased_items = 0
    existing_budget = 10000
    purchase_list = []

    # Check to make sure the string passed isn't null
    if not s:
        return "Invalid: The string passed as argument zero is null."

    # Convert string contents to a list of ints. Also check to make
    # sure each string only contains digits.
    for purchased_item in s.split(", "):
        if purchased_item.isdigit():
            purchase_list.append(int(purchased_item))
        else:
            return "Invalid: One string item {purchased_item} is not a digit."

    # The first item shouldn't count towards the total
    if purchase_list[0] <= existing_budget:
        existing_budget -= purchase_list[0]

    # Iterate over a sorted list of integers and calculate the
    # number of items we can purchase with the remaining budget.
    for item in sorted(purchase_list[1:]):
        if item <= existing_budget:
            purchased_items += 1
            existing_budget -= item

    return purchased_items


if __name__ == "__main__":
    pass
