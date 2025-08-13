Spam Email Detection using Naive Bayes
This repository contains a machine learning model that detects whether an email is spam or not using the Naive Bayes classifier. The project also includes a simple Flask-based web interface where you can input email content and get a prediction of whether it's spam or not.

How the Model Works
The Naive Bayes classifier is a popular probabilistic model based on Bayes’ Theorem, which assumes that the features (words in the email) are conditionally independent given the class label (spam or not spam).

Steps:
Data Preprocessing:

The dataset is cleaned by removing stopwords and performing tokenization (splitting text into words).

The text is then converted into a numeric format using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.

Model Training:

A Multinomial Naive Bayes classifier is trained on a labeled dataset of emails (spam vs. non-spam).

The model learns to associate specific word patterns with the class labels.

Prediction:

When an email is submitted via the Flask interface, it is processed in the same way (tokenization, TF-IDF vectorization) and fed into the trained Naive Bayes model to predict whether it's spam or not.

Once the Flask server is running, navigate to http://127.0.0.1:5000/ in your browser.


Technologies Used
Python – Programming language used for the backend.

Flask – Web framework used to create a simple interface.

scikit-learn – Machine learning library used to implement the Naive Bayes algorithm.

HTML/CSS – Frontend for the user interface.

pickle – Serialization tool to save and load the trained model.



Input the email content into the provided form.

Click on the "Detect Spam" button to receive the result.

If the email is classified as spam, it will return a spam message.

If the email is classified as not spam, it will return "Not Spam"
