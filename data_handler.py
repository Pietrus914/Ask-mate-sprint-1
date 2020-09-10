import datetime
from connection import read_csv

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

'''function that finds next number for id'''
def get_new_id(questions):
    tmp_id = 0
    for question in questions:
        if int(question['id']) > tmp_id:
            tmp_id = int(question['id'])

    return tmp_id + 1


'''function that adds new question to list of questions'''
def add_question(new_question):
    questions = read_csv("sample_data/question.csv")
    return questions.append(new_question)

'''function that updates question'''
def update_question(edited_question):
    questions = read_csv("sample_data/question.csv")
    for question in questions:
        if question["id"] == edited_question["id"]:
            question["title"] = edited_question["title"]
            question["message"] = edited_question["message"]
    return questions

'''function that returns current data & time'''
def get_current_data():
    return datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")