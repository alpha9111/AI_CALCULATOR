# AI_CALCULATOR
#USING AI+PYTHON
#pip install chatterbot
from chatterbot import ChatBot
Bot = ChatBot(name = 'calculator',
              read_only = True,
              logic_adapters = ["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter = "chatterbot.storage.SQLStorageAdapter")

print('\033c')
print("Hello,I am a calculator. How may I help you?")
while (True):
  user_input = input("me: ")
  if user_input.lower() == 'quit':
    print("Exiting")
    break
    try:

      response = Bot.get_response(user_input)
      print("calculator:",response)
    except:
        print("calculator: please enter valid input.")
