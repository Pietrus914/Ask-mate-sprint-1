

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
