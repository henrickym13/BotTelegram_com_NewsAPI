import telebot
from api.news_api import ApiRequest
from time import sleep

BOT_TOKEN = 'seu token gerado pelo botfather do telegram'
bot = telebot.TeleBot(BOT_TOKEN)


def exibir_noticias(messagem, tema):
    """Função para exibir noticias pelo tema escolhido pelo usuario"""

    # pegando o dado da classe e passando para uma variavel
    dados_api = ApiRequest()
    noticias = dados_api.request_api(tema)

    # exibir as noticias para o usuario
    bot.send_message(messagem.chat.id, 'Aqui estão as principais noticias de hoje')
    sleep(1.3)
   
    for noticia in noticias:
        bot.send_message(messagem.chat.id, f"URL = {noticia}")
        sleep(1.0)


@bot.message_handler(commands=['opcao1'])
def opcao1(messagem):
    # chamar função
    exibir_noticias(messagem, 'business')
    

@bot.message_handler(commands=['opcao2'])
def opcao2(messagem):
    # chamar função
    exibir_noticias(messagem, 'entertainment')


@bot.message_handler(commands=['opcao3'])
def opcao3(messagem):
    # chamar função
    exibir_noticias(messagem, 'general')


@bot.message_handler(commands=['opcao4'])
def opcao4(messagem):
    # chamar função
    exibir_noticias(messagem, 'health')


@bot.message_handler(commands=['opcao5'])
def opcao5(messagem):
    # chamar função
    exibir_noticias(messagem, 'science')


@bot.message_handler(commands=['opcao6'])
def opcao6(messagem):
    # chamar função
    exibir_noticias(messagem, 'sports')


@bot.message_handler(commands=['opcao7'])
def opcao7(messagem):
    # chamar função
    exibir_noticias(messagem, 'technology')


def responder_tudo(messagem):
    """Função para responder qualquer mensagem do usuario
    que não seja uma opção valida"""
    return True


@bot.message_handler(func=responder_tudo)
def enviar_mensagem(messagem):
    texto = """
        Escolha uma opção de noticia para continuar (Clique no item):
        /opcao1 Negócios
        /opcao2 Entretenimento
        /opcao3 Em geral
        /opcao4 Saúde
        /opcao5 Ciência
        /opcao6 Esportes
        /opcao7 Tecnologia
        Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(messagem, texto)


bot.infinity_polling()