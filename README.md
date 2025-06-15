# mental_health_prediction
# Mental Health Prediction in the Workplace

This project predicts the likelihood of mental health issues among employees using survey data and machine learning. It includes data cleaning, exploratory data analysis (EDA), feature engineering, model training, model interpretation, and a deployed web app for real-time predictions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Web App](#web-app)
- [References](#references)
- [License](#license)

## Overview

Mental health in the workplace is a critical concern, especially in the tech industry. This project leverages the [OSMI Mental Health in Tech Survey](https://www.kaggle.com/osmi/mental-health-in-tech-survey) to build a predictive model that helps identify individuals who may be at risk, using Python and popular data science libraries.

## Features

- **Data cleaning and preprocessing**
- **Exploratory Data Analysis (EDA)**
- **Feature engineering**
- **Machine learning model training (Random Forest, etc.)**
- **Model evaluation and interpretation (SHAP)**
- **Interactive web app with Streamlit**


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayushi17c/mental-health-prediction.git
   cd mental-health-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset**
   - Download from [Kaggle - OSMI Mental Health in Tech Survey](https://www.kaggle.com/osmi/mental-health-in-tech-survey)
   - Place `survey.csv` in the `data/` folder

## Usage

### Running the Notebook

- Open and run all cells in `notebooks/EDA_and_Modeling.ipynb` to see data cleaning, EDA, feature engineering, modeling, and evaluation.

### Training the Model

- (Optional) Run the scripts in `src/` to preprocess data and train the model.

### Launching the Streamlit App

- After training, run:
   ```bash
   streamlit run app/streamlit_app.py
   ```
- This will start a web server for interactive predictions.

## Results

- _Summarize your results here (model accuracy, F1 score, ROC-AUC, or important findings)._
- Example:  
   - Model Accuracy: **XX%**
   - ROC-AUC: **YY**
   - Top features: `family_history`, `work_interfere`, `remote_work`, etc.

## Web App

- _If you have deployed your Streamlit app online, add the link here._
- _Otherwise, describe how to use the local app._

## References

- [OSMI Mental Health in Tech Survey - Kaggle](https://www.kaggle.com/osmi/mental-health-in-tech-survey)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/)

## License

This project is licensed under the MIT License.

---

_If you use or reference this project, please give credit!_
