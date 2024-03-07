import csv
import openpyxl

nome_arquivo = "Teste.csv"

# com abrir(arquivo para leitura) como fileRead: 
with open(nome_arquivo,'r') as fileRead:
    # leia como csv
    reader = csv.reader(fileRead)
    # para cada linha no arquivo, adicione ao excel


