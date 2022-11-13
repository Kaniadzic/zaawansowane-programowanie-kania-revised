
from flask import Flask
from flask import render_template
from Model.MoviesLogic import MoviesLogic
from Model.TagsLogic import TagsLogic
from Model.RatingsLogic import RatingsLogic
from Model.LinksLogic import LinksLogic


app = Flask(__name__, template_folder='View')


@app.route('/')
def home() -> str:
    return render_template("index.html", title="Home page (it's empty!)")


@app.route('/movies')
def movies():
    logic = MoviesLogic()
    movies = logic.read_movies("Database/movies.csv")
    return render_template("index.html", data=movies, title="Movies")


@app.route('/links')
def links():
    logic = LinksLogic()
    links = logic.read_links("Database/links.csv")
    return render_template("index.html", data=links, title="Links")


@app.route('/ratings')
def ratings():
    logic = RatingsLogic()
    ratings = logic.read_ratings("Database/ratings.csv")
    return render_template("index.html", data=ratings, title="Ratings")


@app.route('/tags')
def tags():
    logic = TagsLogic()
    tags = logic.read_tags("Database/tags.csv")
    return render_template("index.html", data=tags, title="Tags")
