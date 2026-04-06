from flask import Flask, render_template

app = Flask(__name__)

videos = [
    {"id": 1, "title": "Python Tutorial", "file": "sample.mp4"},
    {"id": 2, "title": "Cloud Basics", "file": "sample.mp4"}
]

@app.route('/')
def home():
    return render_template('home.html', videos=videos)

@app.route('/watch/<int:video_id>')
def watch(video_id):
    video = next(v for v in videos if v["id"] == video_id)
    return render_template('watch.html', video=video)

if __name__ == '__main__':
    app.run(debug=True)