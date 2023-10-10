def my_list(given, target):
    for item in given:
        if isinstance(item, list):
            result = my_list(item, target)
            if result is not None:
                return result
        elif isinstance(item, str) and item == target:
            return item
        elif isinstance(item, int) and item == target:
            return item
    return None

my_given = [["person",77,[1,2,3]],55,"why",[1,2,"hey"]]

found_item = my_list(my_given,3)

if found_item is not None:
    print("found_it:", found_item)
else :
    print("item not found")