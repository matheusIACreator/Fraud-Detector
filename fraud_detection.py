import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

df = pd.read_csv("fraudes.csv")
df.head()

#remove colunas sem valor semântico
df = df.drop(columns=['transaction_id','customer_id'])


#Pré-processamento de Variáveis Categóricas
df_encoded = pd.get_dummies(df, columns=['location'],drop_first=True)

#Separar Varáiveis dependente  e independente
X = df_encoded.drop(columns=['is_fraud'])
y = df_encoded['is_fraud']

# Normaliza
scaler = StandardScaler()
X[['amount', 'time']] = scaler.fit_transform(X[['amount','time']])

#Divide em treine e teste 
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)
#Vizularizar os dados de teste:  print(X_train)

#Treinamento do Modelo

model =MLPClassifier(hidden_layer_sizes=(10,8,10), max_iter=500,
                     random_state=42, learning_rate_init=0.01, activation='relu')
model.fit(X_train, y_train)

#Avaliação do Modelo

y_pred =model.predict(X_test)
report =classification_report(y_pred,y_test, output_dict=True)

# Vizualizar: print(report)

#ADICIONAR NOVOS DADOS

new_transactions = [
    {"amount": 1235.3, "time":10,"location":"Loja Física"},
    {"amount": 12.53, "time":13,"location":"Online"},
    {"amount": 12332.31, "time":20,"location":"Online"},
    {"amount": 12, "time": 7, "location":"Loja Física"},
]

#Criar Dataframe
df_new = pd.DataFrame(new_transactions)

#Transforma variável vategórica 
df_new_encoded = pd.get_dummies(df_new, columns=['location'],drop_first=True)

#Normaliza
df_new_encoded[['amount',  'time']] = scaler.fit_transform(df_new_encoded[['amount','time']])

#Fazer previsão
predictions = model.predict(df_new_encoded)
probabilities = model.predict_proba(df_new_encoded)[:,1]

df_new["fraud_probability"] = probabilities
df_new["is_fraud_predicted"]= predictions

#Exibir previsões 
print(df_new[["amount", "time", "location", "fraud_probability", "is_fraud_predicted"]])
