from flask import Flask, render_template

app = Flask(__name__)
 
# Sample Blog Posts
posts = [
    {"id": 1, "title": "My First Blog Post", "content": "This is the content of my first blog post."},
    {"id": 2, "title": "Another Day in Paradise", "content": "Today I went to the beach and it was amazing!"},
    {"id": 3, "title": "Flask is Awesome!", "content": "I love building web applications with Flask."}
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return render_template("post.html", post=post)
    else:
        return "Post not found", 404
if __name__ == '__main__':
    app.run(debug=True)