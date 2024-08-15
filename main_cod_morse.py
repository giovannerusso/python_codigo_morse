# -*- coding: utf-8 -*-
"""main_cod_morse.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VpxRGX_2R0CaL_jl1xBp_YUl6uZakpsp
"""

'''
Esse sistema tem como característica decodificar uma palavra ou frase codificada em código morse
'''

#Importa pacotes
import os
import sys
import datetime
import pandas as pd
import param_morse

#Abrir o arquivo de mensagem
arquivo = open("msg3.txt", "r")
msg = arquivo.read()
arquivo.close()
file_path = "decode_morse.csv"

# Função que decodifica uma mensagem em morse
'''
A função fun_d_morse tem as seguintes carecterísticas de entrada e saída:
Imput: Mensagem texto, Mensagem dicionário
'''
def fun_d_morse(msg,dic_morse):

    msg_lst = msg.split(" ")
    msg_uni = []
    for letter in msg_lst:
        msg_uni.append(dic_morse[letter])
    #return "".join(str(msg_uni))
    return "".join(str(msg_uni).replace(",","",).replace(" ","").replace("'","").replace("[","").replace("]","").replace("#"," "))



# salvar em arquivo
# datetime da geração
import datetime
'''
A função fun_d_morse tem as seguintes carecterísticas de entrada e saída:
Imput: mensagem em texto claro
Output: palavra escrito em letras e algarismos, salva em arquivo csv
'''
def save_msg_txt(msg_uni):

    #input : mensagem em texto claro
    #output : palavra escrito em letras e algarismos, salva em arquivo csv

    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_uni, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode ="a", index = False, header=hdr)

if __name__ == "__main__":
    msg_uni = fun_d_morse(msg,param_morse.dict_morse)
    save_msg_txt(msg_uni)

"""# Nova seção"""
