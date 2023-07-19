from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample database table
database_table = [
    {
        'text': 'MD AAE 011',
        'vehicle_type': 'light',
        'balance': 5000
    },
    {
        'text': 'AAE 011',
        'vehicle_type': 'light',
        'balance': 5000
    },
    {
        'text': 'LPL-9012',
        'vehicle_type': 'heavy',
        'balance': 5000
    },
    {
        'text': 'AAE 012',
        'vehicle_type': 'light',
        'balance': 5000
    },
    {
        'text': 'AAE 015',
        'vehicle_type': 'light',
        'balance': 5000
    },
]


def find_element_by_text(text):
    for element in database_table:
        if element['text'] == text:
            return element
    return None


entry_table = [
    {
        'text': 'AAE 225',
        'vehicle_type': 'heavy',
        'balance': 5000,
        'passing_date': "07/07/23",
        'passing_time': "22:35"
    }
]


@app.route('/')
def index():
    return render_template('index.html', table=entry_table)


@app.route('/api/verify_text', methods=['POST'])
def verify_text():
    data = request.get_json()
    text_to_verify = data.get('text')
    print(text_to_verify)

    # Check if the text exists in the database table
    exists = any(item['text'] == text_to_verify for item in database_table)
    if (exists):
        if (not entry_table[-1]['text'] == text_to_verify):

            # find verify and reduces the appropriate amount
            element = find_element_by_text(text_to_verify)
            if element['vehicle_type'] == 'light':
                element['balance'] = element['balance'] - 100
            elif element['vehicle_type'] == 'heavy':
                element['balance'] = element['balance'] - 500
            print(element)

            # set passing time
            now = datetime.now()
            date = now.strftime("%d/%m/%y")
            element['passing_date'] = date
            time = now.strftime("%H:%M")
            element['passing_time'] = time
            entry_table.append(element)

    response = {'exists': exists}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
