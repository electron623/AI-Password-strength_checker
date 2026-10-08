# 🔐 AI Password Strength Checker

An **AI-based Password Strength Checker** that evaluates the strength of passwords using password characteristics and an entropy-based machine learning model. The project combines traditional password-strength analysis with a trained AI model to provide a more intelligent assessment and suggestions for creating stronger passwords.

## 📌 Overview

Weak passwords are one of the most common causes of account compromise. Traditional password checkers generally evaluate passwords using fixed rules such as length, uppercase/lowercase characters, numbers, and special symbols.

This project extends that approach by incorporating **machine learning and entropy analysis** to estimate password strength and provide recommendations for improving weak passwords.

The project contains the password-checking logic, training dataset, trained entropy model, and an AI suggestion component.

## ✨ Features

* 🔍 **Password Strength Analysis**

  * Evaluates the characteristics of a password.
  * Provides an indication of password strength.

* 🤖 **AI-Based Analysis**

  * Uses a trained machine learning model to analyze password entropy/strength.
  * The trained model is stored as `entropy_model.pkl`.

* 📊 **Password Dataset**

  * Includes a dataset used for developing and working with the model.
  * Dataset modification functionality is provided for preparing or adjusting training data.

* 💡 **AI Suggestions**

  * Provides suggestions to improve password strength.
  * Helps users understand characteristics that can make passwords more difficult to guess.

* 🔐 **Entropy-Based Evaluation**

  * Uses entropy as an important measure of password unpredictability.

## 🗂️ Project Structure

```text
AI-Password-strenght_checker/
│
├── AI_suggester.py
│   └── Generates AI-based suggestions for improving passwords.
│
├── dataset modifier.py
│   └── Utility for modifying/preparing the password dataset.
│
├── dataset.csv
│   └── Dataset used for the machine learning component.
│
├── entropy_model.pkl
│   └── Trained machine learning model for entropy/strength analysis.
│
├── original_Passwordchecker.py
│   └── Original password-strength checking implementation.
│
└── password_Datasets.txt
    └── Password dataset/reference data.
```

## 🛠️ Technologies Used

| Technology           | Purpose                              |
| -------------------- | ------------------------------------ |
| **Python**           | Core programming language            |
| **Machine Learning** | Password-strength/entropy prediction |
| **Pandas / CSV**     | Dataset handling                     |
| **Pickle (`.pkl`)**  | Storing the trained model            |
| **Entropy Analysis** | Measuring password unpredictability  |

> The exact Python dependencies should be verified from the source files before adding them to `requirements.txt`.

## ⚙️ How It Works

The project follows a general pipeline:

```text
                ┌─────────────────┐
                │  User Password  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Password        │
                │ Analysis        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Entropy /       │
                │ Feature         │
                │ Extraction      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Trained ML      │
                │ Model           │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Strength        │
                │ Assessment      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ AI Suggestions  │
                └─────────────────┘
```

### 1. Password Input

The user provides a password to the password-checking component.

### 2. Feature Analysis

Relevant characteristics of the password are analyzed to determine its complexity and unpredictability.

### 3. Entropy Prediction

The trained model stored in `entropy_model.pkl` is used as part of the AI-based evaluation process.

### 4. Strength Assessment

The password is assessed according to the analysis performed by the project.

### 5. AI Recommendations

`AI_suggester.py` provides recommendations intended to help improve password quality.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/AbondentSpace1386/AI-Password-strenght_checker.git
```

### 2. Enter the project directory

```bash
cd AI-Password-strenght_checker
```

### 3. Install dependencies

If a `requirements.txt` file is added to the project:

```bash
pip install -r requirements.txt
```

Otherwise, install the Python libraries imported by the project files.

### 4. Run the Password Checker

```bash
python original_Passwordchecker.py
```

### 5. Run the AI Suggestion Component

```bash
python AI_suggester.py
```

> The exact execution flow may depend on how the scripts are currently connected.

## 📊 Dataset

The repository contains:

* `dataset.csv`
* `password_Datasets.txt`

These files provide password-related data used by the project.

`dataset modifier.py` can be used to modify or prepare the dataset for the machine-learning workflow.

For security and privacy, **real personal passwords should never be added to the dataset**.

## 🧠 Machine Learning Model

The project includes:

```text
entropy_model.pkl
```

This file contains the trained model used by the AI component.

The general machine-learning workflow is:

```text
Dataset
   ↓
Data Preparation
   ↓
Feature Extraction
   ↓
Model Training
   ↓
Entropy/Strength Prediction
   ↓
Password Recommendation
```

The model can potentially be retrained when the dataset is updated.

## 🔒 Security Considerations

This project is intended primarily for **password-strength assessment and educational cybersecurity purposes**.

Important security practices include:

* Never store passwords in plaintext.
* Never include real user passwords in training datasets.
* Avoid logging passwords during testing.
* Do not use passwords from real accounts as test inputs.
* Password-strength estimation should not be treated as a guarantee against compromise.
* For real authentication systems, use established password-storage mechanisms such as salted, memory-hard password hashing.

## 🎯 Objectives

The main objectives of this project are:

1. To develop an intelligent password-strength checker.
2. To analyze password complexity and entropy.
3. To apply machine learning to password-strength assessment.
4. To provide useful feedback for improving weak passwords.
5. To demonstrate the application of AI in cybersecurity.
6. To promote better password-security practices.

## 🔮 Future Enhancements

Possible improvements include:

* Add a graphical/web-based interface.
* Add more comprehensive password-pattern detection.
* Integrate established password-strength estimation techniques.
* Improve the training dataset.
* Compare multiple machine-learning algorithms.
* Add visualization of entropy and strength scores.
* Add automated testing.
* Provide more detailed explanations for AI predictions.
* Add secure password-generation functionality.
* Package the project as a reusable Python application.




