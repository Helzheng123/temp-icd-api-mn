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

@app.route('/code/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    return filtered.to_json(orient="records")

#MEDICARE
@app.route('/code/<value>', methods=['GET'])
def payer(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

#4
@app.route('/code/<value>/age_group/<value2>', methods=['GET'])
def code2(value, value2):
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['age_group_code'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records") 

if __name__ == '__main__':
    app.run(debug=True)