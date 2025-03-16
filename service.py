objects = {
    1: {
        "name": "Camary",
        "data": {
            "speed": "very fast",
            "use": "driving"
        }
    },
    2: {
        "name": "Audi",
        "data": {
            "speed": "great",
            "refill": "hybrid"
        }
    }
}

def get_all_objects():
    final = []
    for id, value in objects.items():
        item = {
            "id": id,
            # "name": value["name"],
            # "data": value["data"]
            **value
        }
        final.append(item)
        
    return final

def get_object(id):
    if id not in objects:
        return None
    
    item = {
        "id": id,
        **objects[id]
    }
    return item

def add_object(value):
    if len(objects) == 0:
        new_id = 1
    else:
        new_id = max(objects.keys())+1
        
    # objects[new_id] = value
    place_object(new_id, value)
    return new_id

def delete_all_objects():
    objects.clear()
    
def delete_object(id):
    if id not in objects:
        return False
    
    objects.pop(id)
    return True

def place_object(id, value):
    objects[id] = value
    
def modify_object(id, partial_value):
    if id not in objects:
        return False
    
    updated = {
        **objects[id],
        **partial_value
    }
    place_object(id, updated)
    return True