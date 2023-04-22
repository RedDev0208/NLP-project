
import config
from flask import Flask, render_template, request, jsonify
from model import summarize_text

app = Flask(__name__)


@app.route('/')
def template():
    return render_template("template.html")


@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['summarization']
    print(input_text)

    config.total = round(len(input_text) / 512)
    print(config.total)
    print(len(input_text))

    summarized_text = summarize_text(input_text)
    print(summarized_text)

    return jsonify({'summary': summarized_text})
    # return render_template("template.html", summary=summarized_text)


@app.route("/progress_state")
def progress_state():
    return jsonify({"progress": config.progress, "total": config.total})


if __name__ == "__main__":
    app.run(debug=True, port=5690, host="0.0.0.0")
