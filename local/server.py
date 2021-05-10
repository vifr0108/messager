import time
from datetime import datetime

from flask import Flask, request, abort

app = Flask(__name__)
db = [
    {
        'name': 'Jack',
        'text': 'Hello',
        'time': time.time()
    },
    {
        'name': 'Mary',
        'text': 'Jack',
        'time': time.time()
    },
]


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    dt = datetime.now()
    return {
        'status': True,
        'name': 'Skillbox Messenger',
        # 'time1': time.time(),
        # 'time2': time.gmtime(),
        # 'time3': time.asctime(),
        # 'time4': dt,
        # 'time5': str(dt),
        # 'time6': dt.strftime('%Y/%m/%d %H:%M !!!'),
        'count_messages': len(db),
        'count_users': len(set(m['name'] for m in db))
    }


@app.route("/send", methods=['POST'])
def send():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if not 0 < len(name) <= 64:
        return abort(400)
    if not 0 < len(text) <= 10000:
        return abort(400)

    db.append({
        'name': name,
        'text': text,
        'time': time.time()
    })

    # bot
    if text == '/help':
        db.append({
            'name': 'Bot help',
            'text': data['text'],
            'time': time.time()
        })
        print(db)

    if text == '/status':
        db.append({
            'name': 'Bot status',
            'text': status(),
            'time': time.time()
        })
        print(status())

    return {}


@app.route("/messages")
def messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    filtered_messages = []

    for message in db:
        if message['time'] > after:
            filtered_messages.append(message)

    return {'messages': filtered_messages[:50]}


app.run()
