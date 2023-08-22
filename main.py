from chatbot import ChatBot
myChatBot = ChatBot()

#criar o modelo
myChatBot.createModel()

#apenas carregar um modelo pronto
myChatBot.loadModel()




print("Bem vindo ao Chatbot do PIPE (Pesquisa Inovativa em Pequenas Empresas)")


pergunta = input("como posso te ajudar?")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("posso lhe ajudar com algo a mais?")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    printString = (resposta + "   [" + intencao[0]['intent'] + "]")
    print(printString)


print("Foi um prazer atendê-lo")
