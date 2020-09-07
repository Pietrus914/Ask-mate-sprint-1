

''' function that gets an item from list of dictionary, id -> string type'''
def get_item_by_id(items,id):
    for item in items:
        if item["id"] == id:
            return item

    return None