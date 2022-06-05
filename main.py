import random
import json
from flask import Flask, request
app = Flask(__name__)
@app.route('/jokes/', methods=['GET', 'POST'])
def welcome():
    num = request.args.get('num')
    if (num == None or num == ""):
        num = 10
    

    jokes = ["Where are average things manufactured? The satisfactory.",
            "What do you call a fake noodle? An Impasta.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "Why did the tomato blush? Because it saw the salad dressing.",
            "Why did the skeleton go to the dance? Because he had no body to go with.",
            "What sits at the bottom of the sea and twitches? A nervous wreck.",
            "What does a nosy pepper do? Gets jalapeno business!",
            "What do you call a cow with no legs? Ground beef.",
            "What did the left eye say to the right eye? Between you and me, something smells.",
            "How do you make a tissue dance? Put a little boogie in it."
            ]
    random.seed()
    random.shuffle(jokes)
    output = {'jokes': jokes[:int(num)]}
    return output
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
