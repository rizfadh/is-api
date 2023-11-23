from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chefboost import Chefboost as chef

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    Age : int
    Sex: int
    Cp: int
    Trtbps : int
    Chol : int
    Fbs : int
    Restecg : int
    Thalachh : int
    Exng : int
    Oldpeak : float
    Slp : int
    Caa : int
    Thall : int

model = chef.load_model('model.pkl')

@app.post('/')
async def heartAttack_pred(item : model_input):
    input = item.model_dump().values()
    prediction = chef.predict(model, list(input))
    return {
        'data': item.model_dump(),
        'prediction': str(prediction),
    }
