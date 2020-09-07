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
    question = data_handler.get_item_by_id(connection.read_csv("sample_data/question.csv"),question_id)
    answers = data_handler.get_answers_for_question(connection.read_csv("sample_data/answer.csv"),question_id)
    return render_template("question.html", question = question, answers = answers)


@app.route("/add-question")
def add_question():
    return render_template("add_update_question.html")


@app.route("/add-question", methods=["POST"])
def add_question_post():
    return redirect(url_for("display_question"))


@app.route("/question/<question_id>/edit")
def edit_question(question_id):
    return render_template("add_update_question.html")


@app.route("/question/<question_id>/edit", methods=["POST"])
def edit_question_post(question_id):
    return redirect(url_for("display_question"))


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
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
    return redirect(url_for("display_question"))


@app.route("/question/<question_id>/vote_down", methods=["POST"])
def question_vote_down(question_id):
    return redirect(url_for("display_question"))


@app.route("/answer/<answer_id>/vote_up", methods=["POST"])
def answer_vote_up(answer_id):
    return redirect(url_for("display_question"))


@app.route("/answer/<answer_id>/vote_down", methods=["POST"])
def answer_vote_down(answer_id):
    return redirect(url_for("display_question"))


if __name__ == "__main__":
    app.run()
