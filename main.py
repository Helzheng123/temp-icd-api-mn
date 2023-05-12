from flask import Flask, request 
import pandas as pd 

df = pd.read_csv('data/diagnoses2019.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is an api service for MN medication details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/payer/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['payer'] == value]
    return filtered.to_json(orient="records")

#MEDICARE
@app.route('/payer/<value>', methods=['GET'])
def payer(value):
    print('value: ', value)
    filtered = df[df['payer'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

#4
@app.route('/payer/<value>/age_group/<value2>', methods=['GET'])
def payer2(value, value2):
    filtered = df[df['payer'] == value]
    filtered2 = filtered[filtered['age_group_code'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records") 

if __name__ == '__main__':
    app.run(debug=True)