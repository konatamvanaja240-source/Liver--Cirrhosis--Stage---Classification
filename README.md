## liver-Cirrhosis-Stage-Classification

- 🧠 Prediction in Liver Cirrhosis App (Short)
The app takes patient medical data (age, bilirubin, albumin, etc.) from the user and converts it into the required format. A pre-trained machine learning model (XGBoost/Random Forest) processes this data and predicts the liver cirrhosis stage.
The model output is:

0 → Stage 1 (Mild)

1 → Stage 2 (Moderate)

2 → Stage 3 (Severe)

Finally, the predicted stage is displayed on the web interface.
## Live Demo
https://huggingface.co/spaces/vanaja1234/liver-cirrhosis-app


## Project Overview
This project builds a Machine Learning web app that predicts the stage of liver cirrhosis (Stage 1, 2, 3) using patient medical data.
## Goal:
- Help in early diagnosis.
- Support doctors in decision making.
- Provide real-time predictions through a web interface.
## 🚀 3. Features (What your app can do)
- Takes patient details as input
- Predicts liver stage
- Works instantly (real-time)
- Simple UI using Streamlit
- Uses trained ML model
## 🛠️ 4. Tech Stack (What tools you used)
- Python → main language
- pandas, numpy → data handling
- sklearn, xgboost → machine learning
- Streamlit → web app
📂 Project Structure

| **File/Folder Name**                        | **Description**                                  |
|-------------------------------------------- | -------------------------------------------------|
| app.py                                      |    Web app interface using Gradio                |
| liver cirrhosis.model.pkl                   |    Serialized trained ML model                   |
| requirements.txt                            |    Projects dependencies                         |
| liver cirrhosis.csv                         |    Input Dataset                                 |
| notebook.ipynb                              |    Model development notebook                    |
| README.md                                   |    Project documentation                         |

### ⚙️ 6. How it Works (VERY IMPORTANT)
Step 1: User Input
User enters:
- Age
- Sex
- Bilirubin
- Albumin
- etc.

### Conclusion
The Liver Cirrhosis Stage Classification app successfully uses machine learning to predict the severity of liver disease based on patient data. It provides fast and accurate predictions through a simple web interface, achieving around 89% accuracy. This project demonstrates the practical use of data science in healthcare for early detection and decision support.
