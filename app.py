from flask import Flask, render_template, request
from titlecall import titlecall

app = Flask(__name__)


@app.route('/')
def index():
    name = "who"
    # return name
    return render_template('index.html', title='アニメタイトル表示くんべーた')


@app.route('/', methods=["POST"])
def post():
    year = request.form.get("year")
    cours = request.form.get("cours")

    if year == "":
        return render_template('index.html', title='アニメタイトル表示くんべーた', error="正しい西暦年を入力してね")

    result = titlecall(year, cours)
    print(result)
    return render_template('index.html', title='アニメタイトル表示くんべーた', result=result)


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
