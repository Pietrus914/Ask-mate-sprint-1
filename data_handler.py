import connection
from datetime import datetime

'''function that gets an item from list of dictionary, id ->string type'''
def get_item_by_id(items,id):
    for item in items:
        if item["id"] == id:
            # '''switch timestamp to date string'''
            # timestamp = int(item.get("submission_time"))
            # date_time = datetime.fromtimestamp(timestamp)
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


def views_updated(item_id):
    question_list = connection.read_csv("sample_data/question.csv")
    for question in question_list:
        if question["id"] == item_id:
            question["view_number"] = int(question["view_number"]) + 1
            break
    connection.write_csv("sample_data/question.csv", question_list)


def sorting_questions(questions_list, order_by, order_direction):
    if questions_list[0][order_by].isdigit():
        sorted_questions = sorted(questions_list, key=lambda k: int(k[order_by]))
    else:
        sorted_questions = sorted(questions_list, key=lambda k: k[order_by])
    if order_direction == "descending":
        sorted_questions.reverse()
    return sorted_questions


'''switch timestamp to date string'''
# def transform_timestamp(item):
#     timestamp = int(item["submission_time"])
#     date_time = datetime.fromtimestamp(timestamp)
#     time_formatted = date_time.strftime('%d-%b-%Y %H:%M:%S')
#
#     return time_formatted

'''switch timestamp to date string'''
def transform_timestamp(timestamp):
    date_time = datetime.fromtimestamp(int(timestamp))
    time_formatted = date_time.strftime('%d-%b-%Y (%H:%M:%S)')

    return time_formatted

if __name__ == "__main__":
    s = connection.read_csv("sample_data/question.csv")
    print(s)
    d = sorting_questions(s, "title", "view_number")
    print(d)
