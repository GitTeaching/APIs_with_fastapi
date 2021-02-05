from io import BytesIO
from typing import List
import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile
from model import load_model, predict, prepare_image
from PIL import Image
from pydantic import BaseModel

app = FastAPI()

# Load ML/DL model
model = load_model()


# Define the response JSON
class Prediction(BaseModel):
    filename: str
    content_type: str
    predictions: List[dict] = []


@app.post("/predict", response_model=Prediction)
async def prediction(file: UploadFile = File(...)):
    # Ensure that the file is an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File provided is not an image.")

    content = await file.read()
    image = Image.open(BytesIO(content)).convert("RGB")

    # preprocess the image and prepare it for classification
    image = prepare_image(image, target=(224, 224))
    response = predict(image, model)

    # return the response as a JSON
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "predictions": response,
        #"predictions": [{'score': 0.733, 'class': 'sports_car'}],
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)


# @app.post('/predict')
# def prediction(file: UploadFile=File(...)):

#     #Inialize the data dictionnary that will be returned
#     response = {'success': False}

#     #Ensure that the file is an image
#     if not file.content_type.startswith('image/'):
#         raise HTTPException(status_code=400, detail='File provided not an image.')

#     return response
