from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

bot=ChatBot("chatbot",read_only=False, 
    logic_adapters=[
        
        {
            "import_path":"chatterbot.logic.BestMatch",
            "default_response":"I am sorry, but I do not understand.",
            "maximum_similarity_threshold":0.9
        }

        ])

trainer=ListTrainer(bot)
trainer.train([
    "hi",
    "hello",
    "how's it going ",
    "not bad",
    "how can i lose weight",
    "You've got to work out mate!",
    "any suggestions",
    "Yes, 1- work out 2- stop eating everythis 3- follow diet",
    "other suggestions",
    "please visit this link: https://www.youtube.com/watch?v=LhL5SNZfnQs"
])



# list_trainer=ListTrainer(bot)

# list_trainer.train(list_to_train)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def main():
    return render_template("index.html")



# while True:
#     user_response=input("User: ")
#     print("Chatbot: " + str(bot.get_response(user_response)))
    


@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))


if __name__=="__main__":
    app.run(debug=True)


