
## Digit Vision API

### 1. Before Building an API using FastAPI
    we will train a ml model and save it 

### 2. API using Fast API
    Take the picture of Image, preprocess it and use that trained model to predict the digit.
    return the result as JSON

### 3. Run it Locally and Verify the Response

### 4. Containerize the Application
    we will make image of the API and model using Docker

### 5. Deploy to Gllogle Cloud Run
    Deploy
    HTTPs end points
    enable auto-scaljing.

    Before doing so, you mush have GCP Account.

### 6. Automate Deployment with the help of Github Action
    Trigger deployment on every push to main branch
    and it will build and deploy Automatically.



    







































### Tech Stack
    Python

    TensorFlow / Keras – ML model

    OpenCV – Image preprocessing

    FastAPI – REST API

    Docker – Containerization

    Google Cloud Run – Cloud deployment

    GitHub Actions – CI/CD


















### Learning outcomes

### By completing this project, you will gain hands-on experience with:

Building machine learning models

Serving ML models via APIs

Dockerizing ML applications

Deploying to serverless cloud platforms

Implementing CI/CD pipelines















### Folder Str.

digit-vision-api
│
├── app/
│ ├── main.py
│ ├── model.py 
│ ├── predict.py
│
├── model/
│ └── digit_model.h5
│
├── train/
│ └── train_model.py
│
├── Dockerfile
├── requirements.txt
├── .github/workflows/
│ └── deploy.yml
└── README.md