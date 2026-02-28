import random

from fastapi import FastAPI
# basically how to import it!
app = FastAPI()
#initiallisating it!

arr = []

@app.get('/')
def greetings():
    return {'hello': 'world'}

@app.post('/post')
def post():
    var = random.randint(0,10)
    arr.append(var)
    return (var)

@app.get('/get')
def getall():
    return arr