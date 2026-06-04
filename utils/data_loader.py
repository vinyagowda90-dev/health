import pandas as pd

def load_data():
    df = pd.read_csv(
        "data/diabetes_012_health_indicators_BRFSS2015.csv"
    )
    return df
