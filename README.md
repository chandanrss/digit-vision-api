## Digit Vision API

### Overview:

#### we will train a model and try to idendify/predict the picture of hand writen numbers (0-9) using ML Model.

#### This project is small but you will learn a lot...

    In `data` folder, there're several picture but some of them will be identify, rest not. it's boz of some reason. It's your chances to get into it and figure it out why ?

    Code written are very ease to understand and the folder structure is also simple to get it but make sure you must have some basic knowlege of M/L Architecture and how to run it.

    Below Steps will help you to guide through...

    Let's Start.

### 1. Before Building an API using FastAPI

    we will train a ml model and save it

### 2. API using Fast API

    Take the picture of Image, preprocess it and use that trained model to predict the digit.
    return the result as JSON

### 3. Run it Locally and Verify the Response

    Note: See at the last of this file to run it locally and test it in your sys.

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

```

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

```

### How to run it Locally and Test it

    Follow the steps below to run the project on your local machine.

### First make sure you cloned the repository properly and in using terminal, you get into right folder.

#### 1. Clone the Repository

Clone the repository and move into the project directory:

```bash

git clone https://github.com/chandanrss/digit-vision-api.git
cd digit-vision-api

```

Make sure you are inside the correct project folder before continuing.

#### 2. Create and Activate a Virtual Environment

Using a virtual environment is strongly recommended because:

You may already have different versions of libraries installed

This project should run in an isolated environment

macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate

```

Windows (Command Prompt)

```bash

python -m venv venv
venv\Scripts\activate

```

Windows (PowerShell)

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1

```

#### Note: ⚠️ If PowerShell blocks activation, run this once as Administrator:

Set-ExecutionPolicy RemoteSigned

#### 3. Install Dependencies

After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt

```

#### 4. Run the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

If the server starts successfully, you should see output similar to:

Uvicorn running on http://127.0.0.1:8000

#### 5. Test the API

Open another terminal window (activate the virtual environment there as well) and run the following command:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-F "file=@/var/www/html/aiml/digit-vision-api/data/b-one.jpeg"

```

📌 Notes

Replace the file path with any image available inside the data folder

Example:

-F "file=@data/b-one.png"

This allows you to test different input images easily

#### 6. API Endpoint Details

Endpoint: /predict

Method: POST

Content-Type: multipart/form-data

Input: Image file

Response: JSON containing the digit prediction

Example Response

```bash
{
  "prediction": 1
}
```

✅ You’re All Set!

The application is now running locally, and you can test it using different images from the data folder.
