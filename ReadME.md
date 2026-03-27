# 📩 Spam Classifier using Machine Learning

## 🚀 Overview

This project is a **Spam SMS Classifier** built using Machine Learning.
It classifies messages as **Spam 🚫** or **Not Spam ✅**.

---

## 🧠 Features

* Text preprocessing (lowercase, tokenization, stopword removal, stemming)
* Feature extraction using CountVectorizer / TF-IDF
* Model training using Naive Bayes (MultinomialNB)
* Interactive UI using Streamlit
* WordCloud visualization for spam analysis

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* NLTK
* Pandas, NumPy
* Matplotlib, Seaborn
* Streamlit

---

## 📂 Project Structure

```
spam-classifier/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/spam-classifier.git
```

2. Create virtual environment:

```
python -m venv venv
```

3. Activate environment:

```
venv\Scripts\activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 📊 Model Details

* Algorithm: Multinomial Naive Bayes
* Input: Text message
* Output: Spam / Not Spam

---

## 🧠 Example

Input:

```
Congratulations! You won a free prize!
```

Output:

```
Spam 🚫
```

---

## 💡 Future Improvements

* Improve UI design
* Add more datasets
* Deploy online

---

## 👨‍💻 Author

GitHub: https://github.com/nishtha322
