from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict_image():
    filepath = "tests/test_image.png"
    response = client.post('/predict', 
            files={'file':('filename', open(filepath, 'rb'), 'image/png')}
    )

    assert response.status_code == 200


def test_predict_text():
    filepath = "tests/test_text.txt"
    response = client.post('/predict',
        files={'file': ('filename', open(filepath, 'rb'), 'text/plain')}
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'File provided is not an image.'}