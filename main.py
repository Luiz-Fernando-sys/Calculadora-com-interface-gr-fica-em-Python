#Importando as bibliotecas necessárias para trabalharmos com interface gráfica em python
from sys import flags
from tkinter import *
from tkinter import ttk
from tkinter import font
from unittest import result


#Cores a serem usadas no programa
#Criando variáveis e atribuindo cores a ela
cor1 = "#1e1f1e" #Cor escura
cor2 = "#feffff" #Cor clara
cor3 = "#38576b" #Azul
cor4 = "#b8c3ff" #Cinza
cor5 = "#2448ff" #Laranja


# As três próximas linhas abaixo são linhas essenciais que todo código com interface gráficaempython deve ter para criarmos uma janela em python.
janela = Tk() #Criação da janela. | Basicamente criamos uma classe do tipo TK e atribuimos à uma variável. No caso jogamos a janela dentro da variável. Com isso podemos atribuir algumas especificações para esta janela, que no caso são o título dela e também a repetição dela infinitamente até o usuário clicar para fechar a janela do programa.
janela.title("Calculadora") #Dando um nome para o programa. Este nome será exibido na janela
janela.geometry("235x310") #Definindo um valor respectivamente para largura e altura da janela.
#Definindo que a cor de fundo da janela inteira será preta.
janela.config(bg=cor1)


#CRIANDO FRAMES  |  DIVIDINDO A TELA DO PROGRAMA EM DUAS PARTES
#Dividiremos a tela em duas: Uma parte para exibir o resultado e outra parte para o corpo (onde conterá os botões, etc).

#Criação do primeiro Frame da tela, que será o frame que será exibido o resultadona dsa operações na tela.
# Iremos criar uma variável chamada "frame_tela" e iremos passar ela como frame.
frame_tela = Frame(janela, width=235, height=50, bg=cor3) #Devemos passar dentro dos parênteses qual a Janela pai que este Frame será criado. No caso queremos que ele seja criado dentro da janela principal que demos o nome de janela. E depois também colocamos a largura, algura e cor de fundo deste frame.
frame_tela.grid(row=0, column=0) #Dividimos o frame por grid, atribuindo-lhe linhas e colunas.

#Definindo o Frame do corpo do programa.
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variável todos valores
todos_valores = ''

# Criação da Label
#Para exibirmos o resultado nesta área da tela, temos que criar uma variável passando para ela que ela irá receber somente tipo string dentro dela. Isso devido ao fato de que esta área da tela é uma Label.
valor_texto = StringVar()


# CRIANDO AS FUNÇÕES DAS OPERÇÃOES


# Função responsável por pegar os valores dos botões que o usuário digitou e colocar na tela do visor da calculadora para ser exibido qual a conta que ele está fazendo.
# A função desta função é concatenar todos os caracateres apertados nos botões

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #Mandando o resultado da conta para o visor exibir o resultado para o usuário
    valor_texto.set(todos_valores) #Mandamos o resultado da conta para dentro da variável que do tipo string que é responsável por exibir os resultados das contas dentro do label do visor da área de resultados.


# Função para calcular os valores inseridos pelo usuário
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# Função responsável por limpar a tela do visor da calculadora
def limpar_tela():
    global todos_valores
    todos_valores = "" # Função que limpa o valor desta variável usada nas funções anteriores
    valor_texto.set("") # Função usada para limpar o valor do visor na tela da calculadora.


#CRIANDO A ÁREA DE VISUALIZAÇAO DOS RESULTADOS

# Passamos esta variável para dentro do atributo 'textvariable' dentro desta label conforme o código abaixo.
app_label = Label(frame_tela, textvariable=valor_texto, width=17, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivt 17'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)



#CRIANDO BOTÕES
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=14, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE) #Especificamos que botão será criado dentro do "frame_corpo". Definimos texto dento dele, largura e altura, cor, e fonte. Também colocamos o estilo do botão com o 'relief' e 'overrelief'.
b_1.place(x=0, y=0) #Definimos a posição dele na tela em relação ao frame em que ele foi colocado, que no caso foi dentro do "frame_corpo"

b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE) # O lambda neste caso serve para eu chamar a minha função lá em baixo que concatena os valores na tela do visor da calculadora. Cada botão o lambda chama a função lá em baixo passando para ela o valor igual ao texto do botão em questão, de maneira que a função lá em baixo receba o valor e concatene na tela em forma de string
b_2.place(x=116, y=0)

b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=7, height=2, bg=cor5, fg=cor2, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=175, y=0)


b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=58, y=52)

b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=115, y=52)

b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="X", width=7, height=2, bg=cor5, fg=cor2, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE) # Perceba que se o usuário clicar em "x" que é o sinal de vezes, teremos sendo exibido no visor da calculadora a o sinal de asterisco e, não, a letra X.
b_7.place(x=175, y=52)


b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=58, y=104)

b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=115, y=104)

b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=7, height=2, bg=cor5, fg=cor2, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=175, y=104)


b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=58, y=156)

b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=115, y=156)

b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=7, height=2, bg=cor5, fg=cor2, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=175, y=156)


b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=14, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE) #Especificamos que botão será criado dentro do "frame_corpo". Definimos texto dento dele, largura e altura, cor, e fonte. Também colocamos o estilo do botão com o 'relief' e 'overrelief'.
b_16.place(x=0, y=208) #Definimos a posição dele na tela em relação ao frame em que ele foi colocado, que no caso foi dentro do "frame_corpo"

b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=".", width=7, height=2, bg=cor4, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=116, y=208)

b_18 = Button(frame_corpo, command=calcular, text="=", width=7, height=2, bg=cor5, fg=cor2, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=175, y=208)




janela.mainloop() #Comando responsável por ficar exibindo esta janela por tempo indeterminado, até que eu feche a janela clicando no botão de fechar a janela ao lado de maximizar.



##########################################################################################################

# MELHORIAS PARA A PRÓXIMA VERSÃO

# - Centralizar os elementos dos botões, pois estão todos na direita
# - Fazer o botão de "%" não fazer o módulo de um número pelo outro número, e sim, o cálculo de porcentagem.
# - Fazer com que dê para usar também os números do teclado para fazer conta e, não precise toda vez ficar tendo que clicar com o mouse nos botões da calculadora.
# - Fazer com que não precise clicar no botão "C" para limpar a tela para uma nova conta. Fazer com que só de digitar uma nova conta ele já apague tudo.