# 🤖 Projeto: Análise de Sentimentos com IA

## 🎯 Objetivo

Analisar feedbacks de clientes utilizando Inteligência Artificial para identificação de sentimentos.

## 🛠️ Ferramentas utilizadas

* ChatGPT / Gemini
* Python (pandas)
* Excel / Google Sheets

## 📁 Atividades realizadas

* Coleta e organização de dados de feedback
* Aplicação de IA para classificação de sentimentos
* Estruturação de dados para análise
* Interpretação de resultados para geração de insights

## 📈 Resultados

* Classificação de feedbacks em positivo, negativo e neutro
* Identificação de padrões de satisfação dos clientes
* Simulação de aplicação de IA em contexto de negócio

## 💡 Observação

Projeto desenvolvido com foco em aprendizado de aplicações práticas de IA em análise de dados.





from textblob import TextBlob

def analisar_sentimento(texto):
    analise = TextBlob(texto)
    
    if analise.sentiment.polarity > 0:
        return "Positivo 😊"
    elif analise.sentiment.polarity < 0:
        return "Negativo 😡"
    else:
        return "Neutro 😐"

print("=== Analisador de Sentimentos ===")

texto = input("Digite uma frase: ")
resultado = analisar_sentimento(texto)

print("Resultado:", resultado)
