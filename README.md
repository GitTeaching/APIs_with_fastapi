# APIs_with_fastapi
Python - Building APIs with FastAPI.


**1- Quantmetry_ResNet_api :**

Image classification API using ResNet. Based on : https://www.quantmetry.com/blog/tutoriel-deployer-api-machine-learning/

<img src="https://github.com/GitTeaching/APIs_with_fastapi/blob/main/quantmetry_ResNet_api/architecture.png" width=600 />

**2- devdotto_microservices :**

Movies and casts microservices in Python using FastAPI, Postgres and Docker compose. 

Based on : https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc

- **/python_microservices**: 4 different microservices, movie_service, a database for movie_service, cast_service and a database for cast service. Using **Nginx** to access both services using a single host address : port 8080. Run ```docker-compose up -d```, then http://localhost:8080/api/v1/movies/docs for movie service docs and http://localhost:8080/api/v1/casts/docs for cast service docs.

**3- banknote_ml_api :**

Deploying Machine Learning Models (Bank note classification using Random Forest algorithm) as APIs.
