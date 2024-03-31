
import pandas as pd
import joblib
import spacy

nlp = spacy.load("en_core_web_lg") 

def preprocess(text):
    list =[]
    for token in nlp(text):
        if token.is_space or token.is_punct:
            continue
        list.append(token.lemma_)
    return ' '.join(list)


base = r'\Users\lenovo\Documents\AI and ML\DS AND ML\Disease Detection from Symptoms using Transformers and Tokenizer\app'
model = joblib.load(f'{base}/model.pkl')
scaler = joblib.load(f'{base}/scaler.pkl')
df = pd.read_csv(f'{base}/Symptom2Disease.csv')
lookup = dict(zip(pd.Series(df['label'].unique()),pd.Series([i for i in range(24)])))



def predict(data):
    tp1 = preprocess(data)
    tp1 = nlp(tp1).vector
    tp1 = tp1.reshape(1,-1)
    tp1 = scaler.transform(tp1)
    pred = model.predict(tp1)
    value = [i for i in lookup if lookup[i]==pred[0]]
    return value[0]
