from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = 'YOUR_API_KEY_HERE'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    system_prompt = """
    You are a smart personal finance assistant that speaks English, Hindi, Tamil, and other Indian languages.
    You help people with:
    - Saving money (budgeting tips, financial planning)
    - Taxes (filing advice, rules in India)
    - Investments (stocks, SIPs, mutual funds, etc.)
    Keep answers short, clear, and beginner-friendly. Avoid legal advice.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': 'Sorry, an error occurred.', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)