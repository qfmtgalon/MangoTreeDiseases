from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str

@app.get("/anthracnose/")
async def anthracnose():
    return {
        "DESCRIPTION": "a group of fungal diseases that causes sunken spots or lesions on the leaves, stems, flowers, and fruits of many plants, including trees like maple and oak, and crops like bananas and tomatoes",
        "LETHALITY": "Not lethal, moderate",
        "HUMIDITY": "Warm and moist weather"
    }

@app.get("/sootymold/")
async def sooty_mold():
    return {
        "DESCRIPTION": "Dark Brown, Black mostly seen in Warm and Dry period and grows on honeydew excreted by piercing sucking insects.",
        "LETHALITY": "Not lethal, Mild, Moderate",
        "HUMIDITY": "Warm or Dry Weather."
    }

@app.get("/redrust/")
async def red_rust():
    return {
        "DESCRIPTION": "Red rust is a fungal disease that damages mango plants. Puccinia mangiferae affects the tree's leaves. Reddish-brown or orange pustules on the leaves may cause distortion and premature leaf drop. This reduces tree growth and fruit yield.",
        "LETHALITY": "Not lethal, Mild, Moderate",
        "HUMIDITY": "Wet and warm weather"
    }
