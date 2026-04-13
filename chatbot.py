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
