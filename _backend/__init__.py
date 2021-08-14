from flask import Flask, render_template
from _database import db_session
from flask_graphql import GraphQLView

# defining the main application
app = Flask(
    __name__,
    template_folder="../_frontend",
    static_folder="../_frontend/components",
)

# setting up the database
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# setting up the graphql api
from _backend.graphql import schema

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,
    ),
)

# defining the main application route
@app.route("/")
def main():
    return render_template("index.html")
