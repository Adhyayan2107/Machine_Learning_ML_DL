from schema import Greet

from fastapi import FastAPI
# basically how to import it!
app = FastAPI()
#initiallisating it!

arr = []

@app.get('/')
def greetings():
    return {'hello': 'world'}

@app.post('/post')
def post(greet:Greet):
    arr.append(greet.name)
    return greet

@app.get('/get')
def getall():
    return arr