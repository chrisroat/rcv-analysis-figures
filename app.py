from flask import Flask, render_template, send_from_directory

FIGURES = {
    "votes": "Results",
    "corr": "Vote correlations",
    # "frac": "Vote overlap",
    # "num_votes": "#Votes/Ballot",
    # "num_winners": "#Winners/Ballot",
    "num_votes_winners": "#Votes X #Winners/Ballot",
    "combos": "Ballot combinations",
}
ELECTIONS = {
    "2020 SF Community College District": "2020/ca/city/san_francisco/general/community_college_district/san_francisco/board",
    "2020 SF School Board": "2020/ca/city/san_francisco/general/school_district/san_francisco/board",
    "2020 Los Altos City Council": "2020/ca/county/santa_clara/general/city/los_altos/council",
    "2022 Los Altos City Council": "2022/ca/county/santa_clara/general/city/los_altos/council",
    "2020 Mountain View City Council": "2020/ca/county/santa_clara/general/city/mountain_view/council",
    "2022 Mountain View City Council": "2022/ca/county/santa_clara/general/city/mountain_view/council",
}

app = Flask(__name__)


@app.route("/data/<path:path>")
def data(path):
    return send_from_directory(".", path)


@app.route("/")
def index():
    return render_template("index.html", titles=ELECTIONS)


@app.route("/election/<title>")
def election(title):
    path = ELECTIONS[title]
    return render_template("election.html", title=title, path=path, figures=FIGURES)


if __name__ == "__main__":
    app.run()
