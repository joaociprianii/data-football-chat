from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain.schema import HumanMessage
import os
import pandas as pd
import datetime
import time
import os
import sqlite3

def get_api_key():
    load_dotenv(find_dotenv())
    api_key = os.getenv("GROQ_API_KEY")
    return api_key


def get_all_tables_data(files):
    data = []

    for file in files:
        df = pd.read_csv(file)
        data.append(df)

    combined_data = pd.concat(data, ignore_index=True)

    return combined_data

def get_csv_content_as_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()



def load_info(file_paths):
    combined_content = ""

    for file in file_paths:
        with open(file, 'r', encoding='utf-8') as f:
            combined_content += f.read() + "\n"

    return combined_content



def answer_question_with_glossary_and_data(question):

    def load_info(file_paths):
        combined_content = ""

        for file in file_paths:
            with open(file, 'r', encoding='utf-8') as f:
                combined_content += f.read() + "\n"

        return combined_content

    combined_info = load_info(file_paths=[r'C:\Users\Wellbe\DataspellProjects\dsProject\football_api\files\infos\glossary.txt'])

    database_data = get_csv_content_as_string(r'C:\Users\Wellbe\DataspellProjects\dsProject\football_api\files\2024-11-22\data_info_pl.csv')

    template = """ 
    Você é um assistente especializado em futebol, capaz de responder perguntas de maneira precisa e informada.
    É muito importante que voce responda de forma direta quando os dados estiverem no banco de dados.
    Caso não haja a informação, voce pode dizer algo como "Segundo minhas pesquisas" e completar com a resposta. Mas sempre da forma mais direta possivel.
    Voce nao pode incluir códigos, não ser que seja pedido. 
    Tente sempre memorizar as 3 respostas anteriores para guardar de contexto.
    Use as informações nos arquivos csv que foram disponibilizados para voce e dos documentos disponíveis para formular suas respostas.
    Lembrando que voce tem todas dados sobre o campeonato brasileiro e campeonato ingles(premier league) e os dados junto dos significados das siglas que voce tem a disposição estao dentro do arquivo {combined_info}  
    
    É muito importante que voce responda de forma direta quando os dados estiverem no banco de dados.
    
    Contexto:
    - Banco de dados: contém dados atualizados sobre jogadores, times, estatísticas e competições.
    - Documentos de apoio: incluem explicações detalhadas sobre regras, história, termos e estratégias de futebol.
    
    Arquivos com as estatisticas: {database_data}
    Informações adicionais: {combined_info}
    
    Pergunta do usuário: {question}
    
    Resposta:
    """

    # Preencher o prompt com os dados
    prompt = PromptTemplate.from_template(template=template)
    filled_prompt = prompt.format(database_data=database_data[:1], combined_info=combined_info[:1], question=question)

    # Conectar ao modelo de IA e obter a resposta
    chat = ChatGroq(model="llama3-8b-8192")
    response = chat.invoke([HumanMessage(content=filled_prompt)])
    return response