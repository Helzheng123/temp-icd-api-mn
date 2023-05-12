from flask import Flask
import pandas as pd

df = pd.read_csv('./data/diagnoses2019.csv')

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return 'this is a API service for MN ICD code details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)    
    result = top10rows.to_json(orient="records")
    return result


if __name__ == '__main__':
    app.run(debug=True)

