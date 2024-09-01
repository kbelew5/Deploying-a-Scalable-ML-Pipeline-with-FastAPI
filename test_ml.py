import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

# Load the census data
data = pd.read_csv('data/census.csv')

# Define variables
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# Split the data into training and test sets
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Process the training data
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Process the test data
X_test, y_test, _, _ = process_data(
    test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)

# Train the model on the training data
model = train_model(X_train, y_train)


def test_data_processing():
    """
    Test if the data processing function returns the expected number of features.
    """
    assert X_train.shape[1] == X_test.shape[1], "The number of features in X_train and X_test should match"
    assert len(y_train) == X_train.shape[0], "The number of labels should match the number of training samples"
    assert len(y_test) == X_test.shape[0], "The number of labels should match the number of test samples"
    pass

def test_model_training():
    """
    Test if the model training function returns a trained model.
    """
    assert model is not None, "The model should not be None"
    assert hasattr(model, "predict"), "The trained model should have a predict method"
    pass

def test_inference():
    """
    Test if the inference function returns predictions of the correct shape.
    """
    preds = inference(model, X_test)
    assert isinstance(preds, np.ndarray), "Predictions should be a numpy array"
    assert len(preds) == len(X_test), "The number of predictions should match the number of test samples"
    pass

def test_model_metrics():
    """
    Test if the compute_model_metrics function returns the correct metrics.
    """
    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    assert 0.0 <= precision <= 1.0, "Precision should be between 0 and 1"
    assert 0.0 <= recall <= 1.0, "Recall should be between 0 and 1"
    assert 0.0 <= fbeta <= 1.0, "F-beta score should be between 0 and 1"
    pass

# Run the tests
if __name__ == "__main__":
    pytest.main()
