
var openBtn = document.getElementById('open');
openBtn.addEventListener('click', function () {
    var input = document.createElement('input');
    input.type = 'file';
    input.onchange = function (e) {
        var file = e.target.files[0];
        var reader = new FileReader();
        reader.onload = function () {
            var contents = reader.result;
            document.getElementById('text').value = contents;
        }
        reader.readAsText(file);
    }
    input.click();
});

var saveBtn = document.getElementById('download');
saveBtn.addEventListener('click', function () {
    var content = document.getElementById('summary').value,
        blob = new Blob([content], { type: 'text/plain' });

    // var writer = new FileWriter();

    // writer.onwriteend = function () {
    //     console.log("Text saved to file");
    // }

    // writer.onerror = function (e) {
    //     console.log("Error saving text to file:", e);
    // }

    // writer.write(blob, "result.txt");

    saveAs(blob, "result.txt");
});

var summarizeBtn = document.getElementById('run');
var run = 0;
var intervalId = 0;

const progressBarContainer = document.querySelector('.progress-bar__container');
const progressBar = document.querySelector('.progress-bar');
const progressBarText = document.querySelector('.progress-bar__text');

const progressBarStates = [];

let progress = 0, total = 0;


summarizeBtn.onclick = function () {
    var data = {
        summarization: document.getElementById('text').value
    };

    $.ajax({
        type: "POST",
        url: "/summarize",
        //contentType: "application/json",
        data: data,
        success: function (result) {
            document.getElementById('summary').value = result.summary;
            console.log('Success');
        },
        error: function (xhr, status, error) {
            // Handle errors here
            console.log('Error:', error);
        }
    })


    fetch('/progress_state')
        .then(response => response.json())
        .then(data => {
            progress = data.progress;
            total = data.total;
            for (var i = 0; i <= total; i++) {
                progressBarStates[i] = Math.floor(100 * i) / total;
            }
            gsap.to(progressBar, { x: `${(progress * 1.0 / total) * 100}%`, duration: 0 });
        });

    intervalId = setInterval(updateProgress, 1000);

    run = 1
}

function updateProgress() {

    if (run == 1) {
        fetch('/progress_state')
            .then(response => response.json())
            .then(data => {
                progress = data.progress;
                console.log(progress);
                total = data.total;

                // Update the progress bar using GSAP animation library
                gsap.to(progressBar, { x: `${(progress * 1.0 / total) * 100}%`, duration: 1 });
                // If the progress is complete, show a completion message
                if (progress == total) {
                    progressBarText.textContent = 'Summarization Completed!';
                    progressBarContainer.style.boxShadow = '0 0 5px #4895ef';
                    gsap.to(progressBar, { backgroundColor: '#4895ef', duration: 1 });
                    run = 0;
                    clearInterval(intervalId);
                }
            });
    }
}

/**
 * This is myapp.py

import config
from flask import Flask, render_template, request, jsonify
from model import summarize_text

app = Flask(name)

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

if name == "main":
app.run(debug=True, port=5690, host="0.0.0.0")

And this is my model.py

def summarize_text(LONG_ARTICLE):

# Initialize summarization pipeline0
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

summary = ""

for i in range(0, len(LONG_ARTICLE), 512):

    # Split long text into chunks of size 512
    chunk = LONG_ARTICLE[i:i+512]

    # Dynamically calculate max_length based on input_length
    input_length = len(chunk)

    # Set max_length as 150% of input_length, with a maximum limit of 1024
    max_length = min(int(input_length * 1.5), 1024)

    result = summarizer(chunk, max_length=max_length,
                        min_length=40, do_sample=False)
    if len(result) > 0:
        summary += result[0]["summary_text"] + " "

    config.progress += 1

return summary
This is template.js file

var summarizeBtn = document.getElementById('run');
var run = 0;
var intervalId = 0;

const progressBarContainer = document.querySelector('.progress-bar__container');
const progressBar = document.querySelector('.progress-bar');
const progressBarText = document.querySelector('.progress-bar__text');

const progressBarStates = [];

let progress = 0, total = 0;

summarizeBtn.onclick = function () {
var data = {
summarization: document.getElementById('text').value
};

$.ajax({
    type: "POST",
    url: "/summarize",
    //contentType: "application/json",
    data: data,
    success: function (result) {
        document.getElementById('summary').value = result.summary;
        console.log('Success');
    },
    error: function (xhr, status, error) {
        // Handle errors here
        console.log('Error:', error);
    }
})


fetch('/progress_state')
    .then(response => response.json())
    .then(data => {
        progress = data.progress;
        total = data.total;
        for (var i = 0; i <= total; i++) {
            progressBarStates[i] = Math.floor(100 * i) / total;
        }
        gsap.to(progressBar, { x: `${(progress * 1.0 / total) * 100}%`, duration: 0 });
    });

intervalId = setInterval(updateProgress, 1000);

run = 1
}

function updateProgress() {

if (run == 1) {
    fetch('/progress_state')
        .then(response => response.json())
        .then(data => {
            progress = data.progress;
            console.log(progress);
            total = data.total;

            // Update the progress bar using GSAP animation library
            gsap.to(progressBar, { x: `${(progress * 1.0 / total) * 100}%`, duration: 1 });
            // If the progress is complete, show a completion message
            if (progress == total) {
                progressBarText.textContent = 'Summarization Completed!';
                progressBarContainer.style.boxShadow = '0 0 5px #4895ef';
                gsap.to(progressBar, { backgroundColor: '#4895ef', duration: 1 });
                run = 0;
                clearInterval(intervalId);
            }
        });
}
}

And this is template.js file

var summarizeBtn = document.getElementById('run');
var run = 0;
var intervalId = 0;

const progressBarContainer = document.querySelector('.progress-bar__container');
const progressBar = document.querySelector('.progress-bar');
const progressBarText = document.querySelector('.progress-bar__text');

const progressBarStates = [];

let progress = 0, total = 0;

summarizeBtn.onclick = function () {
var data = {
summarization: document.getElementById('text').value
};

$.ajax({
    type: "POST",
    url: "/summarize",
    //contentType: "application/json",
    data: data,
    success: function (result) {
        document.getElementById('summary').value = result.summary;
        console.log('Success');
    },
    error: function (xhr, status, error) {
        // Handle errors here
        console.log('Error:', error);
    }
})


fetch('/progress_state')
    .then(response => response.json())
    .then(data => {
        progress = data.progress;
        total = data.total;
        for (var i = 0; i <= total; i++) {
            progressBarStates[i] = Math.floor(100 * i) / total;
        }
        gsap.to(progressBar, { x: `${(progress * 1.0 / total) * 100}%`, duration: 0 });
    });

intervalId = setInterval(updateProgress, 1000);

run = 1
}

function updateProgress() {

if (run == 1) {
    fetch('/progress_state')
        .then(response => response.json())
        .then(data => {
            progress = data.progress;
            console.log(progress);
            total = data.total;

            // Update the progress bar using GSAP animation library
            gsap.to(progressBar, { x: `${(progress * 1.0 / total) * 100}%`, duration: 1 });
            // If the progress is complete, show a completion message
            if (progress == total) {
                progressBarText.textContent = 'Summarization Completed!';
                progressBarContainer.style.boxShadow = '0 0 5px #4895ef';
                gsap.to(progressBar, { backgroundColor: '#4895ef', duration: 1 });
                run = 0;
                clearInterval(intervalId);
            }
        });
}
}

As you can see model.py, config.progress increased by 1
And in model.py, I sent config.progress to js file.
And In template,js I received data.progress, data.progress is as same as config.progress.
And I call updateProgress function in every 1 sec.
But config.progress is not increased.
Why does this happen? Please share me correct code.
 */