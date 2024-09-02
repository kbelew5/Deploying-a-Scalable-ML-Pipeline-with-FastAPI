# Model Card

## Model Details

- **Model Type**: Logistic Regression
- **Solver**: lbfgs
- **Max Iterations**: 1000
- **Scaling**: None (consider scaling if convergence issues occur)

## Intended Use

This model is intended to predict if an individual's annual income exceeds $50K based on census data. It is designed to assist with social and economic research by providing insights into income distribution.

## Training Data

The model was trained on a subset of the Adult Census Income dataset. This dataset contains demographic information and economic attributes of individuals, and the target variable indicates whether an individual's income exceeds $50K.

- **Features**: 
  - `age`, `workclass`, `fnlgt`, `education`, `education-num`, `marital-status`, `occupation`, `relationship`, `race`, `sex`, `capital-gain`, `capital-loss`, `hours-per-week`, `native-country`
- **Label**: 
  - `salary` (binary: `<=50K`, `>50K`)

## Evaluation Data

The evaluation data is a separate subset of the Adult Census Income dataset that was not used during training. This data is used to test the model's generalization ability and performance on unseen data.

## Metrics

- **Precision**: 0.7411
- **Recall**: 0.5831
- **F1 Score**: 0.6527

These metrics indicate the model's accuracy in predicting positive income classes (`>50K`). Higher precision and recall suggest good performance, but further tuning may be necessary depending on the application.

## Ethical Considerations

- **Bias and Fairness**: 
  - The model should be regularly evaluated to ensure it does not reinforce existing biases in the training data.
  - Particular attention should be paid to demographic features such as `race`, `sex`, `native-country`, etc., to prevent any form of discrimination.
  
- **Transparency**: 
  - Users should be informed about the model's strengths and limitations.
  - All stakeholders should understand how features contribute to the predictions.

## Caveats and Recommendations

- **Generalization**: 
  - The model may not generalize well to populations outside the scope of the training data. Users should be cautious when applying this model to different demographic or geographic groups.

- **Performance**: 
  - Model performance may vary with different distributions or feature sets. It is recommended to retrain or fine-tune the model when applied to new data.

- **Further Improvements**:
  - Consider implementing feature scaling to address any convergence warnings during training.
  - Evaluate model performance periodically to ensure it meets current standards and ethical guidelines.

