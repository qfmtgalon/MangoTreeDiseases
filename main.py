from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str

@app.get("/anthracnose/")
async def anthracnose():
    return {
        "DESCRIPTION": "Anthracnose is a particularly troublesome fungal infection that requires attention across the entire cultivation and storage process. This common crop disease can strike before harvest and continue to develop even after crops are picked. It affects stems, leaves, shoots, flowers, and fruits, causing dead tissue patches, leaf drops, and fruit damage. The fungi grow and spread best in warm, humid environments.",
        "LETHALITY": "Not lethal, moderate",
        "HUMIDITY": "Warm and moist weather"
    }

@app.get("/sootymold/")
async def sooty_mold():
    return {
        "DESCRIPTION": "Dark Brown, Black mostly seen in Warm and Dry period and grows on honeydew excreted by piercing sucking insects.",
        "LETHALITY": "Not lethal, Mild, Moderate",
        "HUMIDITY": "Warm or Dry Weather"
    }

@app.get("/redrust/")
async def red_rust():
    return {
        "DESCRIPTION": "Red rust is a fungal disease that damages mango plants. Puccinia mangiferae affects the tree's leaves. Reddish-brown or orange pustules on the leaves may cause distortion and premature leaf drop. This reduces tree growth and fruit yield.",
        "LETHALITY": "Not lethal, Mild, Moderate",
        "HUMIDITY": "Wet and warm weather"
    }

@app.get("/powderymildew/")
async def powdery_mildew():
    return {
        "DESCRIPTION": "Powdery mildew is a fungal disease that affects mango trees. It appears as a white or grayish powdery growth on leaves, shoots, flowers, and fruits. Severe infections can weaken the tree and reduce productivity.",
        "LETHALITY": "Not lethal, Moderate",
        "HUMIDITY": "Moderate to high humidity, favorable conditions include warm weather"
    }
