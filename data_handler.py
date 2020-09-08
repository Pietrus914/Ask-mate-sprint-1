

'''function that gets an item from list of dictionary, id ->string type'''
def get_item_by_id(items,id):
    for item in items:
        if item["id"] == id:
            return item

    return None

'''function that gets all answers for a given question'''
def get_answers_for_question(answers,question_id):
    all_answers = []
    for answer in answers:
        if answer["question_id"] == question_id:
            all_answers.append(answer)

    return all_answers

'''function that deletes item from list'''
def delete_item_from_items(items, item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return items


'''function that adds vote up'''
def add_vote_up(items,item_id,down=None):
    for item in items:
        if item["id"] == item_id:
            # if down:
            #     item["vote_number"] = item.get("vote_number", 0) - 1
            # else:
            item["vote_number"] = int(item.get("vote_number", 0))+1
            return items

'''function that substract vote'''
def substract_vote(items,item_id):
    for item in items:
        if item["id"] == item_id:
            item["vote_number"] = int(item.get("vote_number", 0)) - 1
            return items
