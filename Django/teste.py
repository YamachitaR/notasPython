# Importando as bibliotecas necessárias
import numpy as np
from sklearn.linear_model import LogisticRegression

# Dados de exemplo
horas_estudo = np.array([2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)  # Convertendo para matriz
horas_sono = np.array([8, 7, 6, 7, 6, 8, 7]).reshape(-1, 1)  # Convertendo para matriz
passou_no_exame = np.array([0, 0, 1, 1, 1, 1, 1])

# Criando e ajustando o modelo de regressão logística
modelo = LogisticRegression()
modelo.fit(np.hstack((horas_estudo, horas_sono)), passou_no_exame)

# Imprimindo os coeficientes
print("Coeficiente beta0 (interceptação):", modelo.intercept_)
print("Coeficiente beta1 (horas de estudo):", modelo.coef_[0][0])
print("Coeficiente beta2 (horas de sono):", modelo.coef_[0][1])

# Previsão para um novo aluno com 5 horas de estudo e 7 horas de sono
nova_amostra = np.array([[5, 7]])
probabilidade_passar = modelo.predict_proba(nova_amostra)
print("Probabilidade de passar no exame:", probabilidade_passar[0][1])
