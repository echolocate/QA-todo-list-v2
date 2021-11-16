from application import app, db
from application.models import Tasks

@app.route('/create/task')
def create_task():
    new_task = Tasks(description="New Task")
    db.session.add(new_task)
    db.session.commit()
    return f"Task with id {new_task.id} added to database."

# @app.route('/read')
# def read():
#     all_games = Games.query.all()
#     games_string = ""
#     for game in all_games:
#         games_string += "<br>"+ game.name
#     return games_string

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name