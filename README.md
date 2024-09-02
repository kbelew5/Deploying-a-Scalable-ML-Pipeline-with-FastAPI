# Deploying a Machine Learning Model with FastAPI

## Overview

This project demonstrates how to build, train, and deploy a machine learning model using FastAPI. The objective of the 
model is to predict whether an individual's annual income exceeds $50K based on demographic data from the UCI Adult 
Census dataset. The project follows several steps, including setting up CI/CD with GitHub Actions, writing unit tests, 
creating a RESTful API with FastAPI, and interacting with the API locally.

## Project Steps

### 1. Model Building
- **Data Preprocessing**: Cleaned and processed the census data, including encoding categorical variables and normalizing numerical features.
- **Model Training**: Trained a logistic regression model to predict income levels using the processed data.
- **Performance Evaluation**: Evaluated the model's performance using precision, recall, and F1 score metrics. Computed the model's performance on various slices of data.
- **Model and Encoder Saving**: Saved the trained model and encoder for later use in the API.

### 2. Unit Testing
- Developed unit tests to verify the correctness of data preprocessing, model training, inference, and metrics computation functions.
- All tests were executed successfully, confirming the functionality of the machine learning pipeline.
- **Screenshot**: ![Unit Tests Passed](screenshots/unit_test.png)

### 3. Continuous Integration (CI) with GitHub Actions
- Set up GitHub Actions to automatically run `pytest` and `flake8` on every push to the main branch.
- Ensured that all tests pass and that the code adheres to the PEP8 style guide.
- **Screenshot**: ![CI Passing](screenshots/continuous_integration.png)

### 4. API Creation with FastAPI
- Created a RESTful API using FastAPI with two endpoints:
  - **GET /**: Returns a welcome message to confirm the API is running.
  - **POST /data/**: Takes in user data and returns a prediction on whether the individual's income exceeds $50K.
- **Screenshot**: ![API Interaction](screenshots/local_api.png)

### 5. API Interaction
- Interacted with the API locally using the `requests` module in Python.
- Sent a GET request to confirm the API is running.
- Sent a POST request with sample data to test the model's prediction capability.
- Verified that both requests returned the expected results.

### 6. Model Card
- Created a model card detailing the model type, intended use, training data, evaluation data, metrics, ethical considerations, caveats, and recommendations. The model card is included in the repository as `MODEL_CARD.md`.

### Links
- GitHub  link: https://github.com/kbelew5/Deploying-a-Scalable-ML-Pipeline-with-FastAPI/settings
