from flask import Flask, render_template, url_for, redirect, request
import data_handler, connection

app = Flask(__name__)


@app.route("/list")
def main_page():
    headers = ["Title", "Message", "Submission Time", "Views", "Votes"]
    story_keys = ["title", "message", "submission_time", "view_number", "vote_number"]
    questions = connection.read_csv("sample_data/question.csv")
    return render_template("index.html", headers=headers, questions=questions, story_keys=story_keys)


@app.route("/question/<question_id>")
def display_question(question_id):
    question = data_handler.get_item_by_id(connection.read_csv("sample_data/question.csv"), question_id)
    answers = data_handler.get_answers_for_question(connection.read_csv("sample_data/answer.csv"), question_id)
    answers_headers = ["Votes' number", "Answer", "Submission time"]
    return render_template("question.html", question=question, answers=answers, answers_headers=answers_headers)


@app.route("/add-question")
def add_question_get():
    new_question = {
        "id": None,
        "title": "",
        "message": "",
        "submission_time": None,
        "view_number": 0,
        "vote_number": 0
    }
    return render_template("add_update_question.html", question=new_question)


@app.route("/add-question/post", methods=["POST"])
def add_question_post():
    new_question = dict(request.form)
    new_question["id"] = data_handler.get_new_id()

    new_question["submission_time"] = data_handler.get_current_data()

    questions = data_handler.add_question(new_question)
    connection.write_csv("sample_data/question.csv", questions)

    return redirect(url_for("display_question"))


@app.route("/question/<int:question_id>/edit")
def edit_question_get(question_id):
    question = data_handler.get_item_by_id(question_id)

    if question is None:
        return redirect(url_for("display_question"))
    else:
        return render_template("add_update_question.html", question=question)


@app.route("/question/<int:question_id>/edit/post", methods=["POST"])
def edit_question_post(question_id):
    edited_question = dict(request.form)
    questions = data_handler.update_question(edited_question)
    connection.write_csv("sample_data/question.csv", questions)

    return redirect(url_for("display_question"))


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    questions = connection.read_csv("sample_data/question.csv")
    data_handler.delete_item_from_items(questions, question_id)

    connection.write_csv("sample_data/question.csv", questions)

    return redirect(url_for("main_page"))


@app.route("/question/<question_id>/new-answer")
def add_answer(question_id):
    return render_template("new_answer.html")


@app.route("/question/<question_id>/new-answer", methods=["POST"])
def edit_answer_post(answer_id):
    return redirect(url_for("display_question"))


@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    return redirect(url_for("display_question"))


@app.route("/question/<question_id>/vote_up", methods=["POST"])
def question_vote_up(question_id):
    questions = connection.read_csv("sample_data/question.csv")
    questions = data_handler.add_vote_up(questions, question_id)
    connection.write_csv("sample_data/question.csv", questions)

    return redirect(url_for("display_question", question_id=question_id))


@app.route("/question/<question_id>/vote_down", methods=["POST"])
def question_vote_down(question_id):
    questions = connection.read_csv("sample_data/question.csv")
    questions = data_handler.substract_vote(questions, question_id)
    connection.write_csv("sample_data/question.csv", questions)

    return redirect(url_for("display_question", question_id=question_id))


@app.route("/answer/<answer_id>/vote_up", methods=["POST"])
def answer_vote_up(answer_id):
    return redirect(url_for("display_question"))


@app.route("/answer/<answer_id>/vote_down", methods=["POST"])
def answer_vote_down(answer_id):
    return redirect(url_for("display_question"))


if __name__ == "__main__":
    app.run()
