# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola Mundo"

@app.route('/<name>')
def helloName(name):
    return f"Hello, {escape(name)}!"

@app.route('/saludo')
def helloParameter():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

if __name__ == "__main__":
    app.run(debug=True)
