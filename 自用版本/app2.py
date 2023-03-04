from flask import Flask, render_template, request
from markupsafe import Markup
import openai
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

openai.api_key = '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'
app = Flask(__name__)
messages = [{"role": "system", "content": "你好"},
    {"role": "user", "content": "你好"}]
@app.route('/')
def home():

    return render_template('index.html')

@app.route('/get_response', methods=['POST'])

def get_bot_response():
    user_input = request.form['user_input']
    # print(user_input)
    messages.append({'role': 'user', 'content': user_input})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ai_response = completion.choices[0].message['content']
    # print(ai_response)
    messages.append({'role': 'assistant', 'content': ai_response})
    print(messages)
    return  Markup(markdown.markdown(ai_response, extensions=['fenced_code', 'codehilite']))
@app.route('/reset')
def reset():
    global messages
    messages = []
    return "Conversation history has been reset."
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888,debug=True)
