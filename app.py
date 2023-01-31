from helpers import (
    os,
    secrets,
    message,
    render_template,
    getProfilePicture,
    send_from_directory,
    Flask,
)

from routes.post import postBlueprint
from routes.user import userBlueprint
from routes.index import indexBlueprint
from routes.login import loginBlueprint
from routes.signup import signUpBlueprint
from routes.logout import logoutBlueprint
from routes.editPost import editPostBlueprint
from routes.dashboard import dashboardBlueprint
from routes.deletePost import deletePostBlueprint
from routes.createPost import createPostBlueprint
from routes.deleteComment import deleteCommentBlueprint
from routes.changePassword import changePasswordBlueprint

from dbChecker import usersTable, postsTable, dbDirectory, commentsTable

usersTable()
postsTable()
dbDirectory()
commentsTable()

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)
app.config["SESSION_PERMANENT"] = True


@app.context_processor
def utility_processor():
    getProfilePicture
    return dict(getProfilePicture=getProfilePicture)


@app.errorhandler(404)
def notFound(e):
    message("1", "404")
    return render_template("404.html"), 404


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static/images"),
        "favicon.png",
        mimetype="favicon.png",
    )


app.register_blueprint(postBlueprint)
app.register_blueprint(userBlueprint)
app.register_blueprint(indexBlueprint)
app.register_blueprint(loginBlueprint)
app.register_blueprint(signUpBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(editPostBlueprint)
app.register_blueprint(dashboardBlueprint)
app.register_blueprint(deletePostBlueprint)
app.register_blueprint(createPostBlueprint)
app.register_blueprint(deleteCommentBlueprint)
app.register_blueprint(changePasswordBlueprint)


match __name__:
    case "__main__":
        app.run(debug=True)
