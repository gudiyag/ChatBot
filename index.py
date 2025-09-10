from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 

bot=ChatBot("chatbot",read_only=False, 
    logic_adapters=[
        
        {
            "import_path":"chatterbot.logic.BestMatch",
            "default_response":"I am sorry, but I do not understand.",
            "maximum_similarity_threshold":0.9
        }

        ])


list_to_train=[
    "hii",
    "hii there",
    "what's your name",
    "I am chatbot",
    "how old are you ?",
    "I am ageless",
    "why are you so mad?",
    "I am not mad, I am just a bot",
    "Do you have iPhone?",
    "I've everything you have",
    "what is your favorite food?",
    "i don't eat food",
    "whats you job?",
    "I am here to answer your questions",
    "I don't know what you are saying",
]

list_trainer=ListTrainer(bot)

list_trainer.train(list_to_train)
while True:
    user_response=input("User: ")
    print("Chatbot: " + str(bot.get_response(user_response)))



