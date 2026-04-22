import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

MODEL_PATH = "model/model.pkl"

def train_model():
    df = pd.read_csv("dataset/transactions.csv", encoding="latin1")
    X = df[['value', 'gas', 'tx_count']]

    model = IsolationForest(contamination=0.3)
    model.fit(X)

    joblib.dump(model, MODEL_PATH)
    return "Model trained"

def load_model():
    return joblib.load(MODEL_PATH)

def predict(tx):
    model = load_model()

    import pandas as pd
    df = pd.DataFrame([tx], columns=['value', 'gas', 'tx_count'])

    pred = model.predict(df)
    return "suspicious" if pred[0] == -1 else "normal"