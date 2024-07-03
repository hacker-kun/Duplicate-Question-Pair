# Identification of Duplicate Question Pairs on Quora Using NLP

This project focuses on identifying similar question pairs on Quora using advanced feature engineering techniques and machine learning models including Random Forest and XGBoost.

## Features
We have engineered various features to improve model accuracy:

1. **Token-Based Features**
2. **Length-Based Features**
3. **Fuzzy Features**

### Exploratory Data Analysis (EDA) and Feature Analysis
- Minimum Variables with Target Variable
- Maximum Variables with Target Variable
- Last Word and First Word Analysis
- Length-Based Feature Analysis
- Fuzzy Feature Analysis

## Models Used
- Random Forest
- XGBoost

## Setup Instructions

### Prerequisites
- Python 3.x

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Setup the environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Requirements**
   ```sh
   pip install streamlit scikit-learn fuzzywuzzy distance bs4

### Run Application
```sh
streamlit run App.py
