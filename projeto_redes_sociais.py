import random
import pandas as pd
import matplotlib.pyplot as plt

# Definir variáveis para geração de dados fictícios
num_usuarios = 500
min_horas_diarias = 1
max_horas_diarias = 8

# Gerar dados fictícios
dados = []

for _ in range(num_usuarios):
    nome = f"Usuário{_+1}"
    horas_diarias = random.randint(min_horas_diarias, max_horas_diarias)
    posts_feitos = random.randint(0, 30)
    curtidas_recebidas = random.randint(0, 100)
    comentarios_feitos = random.randint(0, 20)
    sentimentos_negativos = random.randint(0, 10)
    
    dados.append([nome, horas_diarias, posts_feitos, curtidas_recebidas, comentarios_feitos, sentimentos_negativos])

colunas = ["Nome", "Horas_Diarias", "Posts_Feitos", "Curtidas_Recebidas", "Comentarios_Feitos", "Sentimentos_Negativos"]

# Criar DataFrame com Pandas
df = pd.DataFrame(dados, columns=colunas)

# Salvar dados fictícios em um arquivo CSV
df.to_csv("dados_rede_social.csv", index=False)

# Transformação
media_mensagens = df["Posts_Feitos"].mean()
grupo_mais_ativo = df["Grupo"].value_counts().idxmax()

def possui_emoji(mensagem):
    return "😃" in mensagem

df["Possui_Emoji"] = df["Mensagem"].apply(possui_emoji)
total_emojis = df["Possui_Emoji"].sum()

df["Hora_Enviada_Hora"] = df["Hora_Enviada"].str.split(":").str[0]  # Suponha que você tenha uma coluna "Hora_Enviada" no DataFrame
horas_mais_ativas = df["Hora_Enviada_Hora"].value_counts().head(3)

# Carga - Visualizações Interativas
plt.figure(figsize=(10, 6))
df_usuario = df.groupby("Nome")["Posts_Feitos"].sum().sort_values(ascending=False)
df_usuario.plot(kind="bar")
plt.title("Número de Mensagens por Usuário")
plt.xlabel("Usuário")
plt.ylabel("Número de Mensagens")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
df_grupo = df.groupby("Grupo")["Posts_Feitos"].sum().sort_values(ascending=False)
df_grupo.plot(kind="bar")
plt.title("Número de Mensagens por Grupo")
plt.xlabel("Grupo")
plt.ylabel("Número de Mensagens")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Carga - Análise de Sentimentos (Fictícia)
def analise_sentimento(mensagem):
    # Simulação de análise de sentimentos
    if "😃" in mensagem:
        return "Positivo"
    elif "😢" in mensagem:
        return "Negativo"
    else:
        return "Neutro"

df["Sentimento"] = df["Mensagem"].apply(analise_sentimento)
sentimentos = df["Sentimento"].value_counts()

print("Análise de Sentimentos:")
print(sentimentos)
