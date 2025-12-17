# 📧 Spam Mail Detection System (Django + ML)

An AI-powered **Spam Mail Detection Web Application** built using  
**Machine Learning, Python, and Django**.  
The system classifies messages as **Spam** or **Ham (Not Spam)**.

---

## 🚀 Features
- User Registration & Login
- Spam / Ham message prediction
- Machine Learning model integration
- Clean UI with Header & Footer
- Django Authentication System
- Session-based prediction result display

---

## 🛠️ Tech Stack
- **Backend**: Python, Django
- **Machine Learning**: Scikit-learn
- **Model**: Logistic Regression
- **Vectorizer**: TF-IDF
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Version Control**: Git & GitHub

---

## 📂 Project Structure

spam_mail/
│── manage.py
│── spam_mail/
│── prediction/
│ ├── views.py
│ ├── forms.py
│ ├── models.py
│ └── urls.py
│── templates/
│── static/
│── model/
│ ├── model.pkl
│ └── vectorizer.pkl
│── db.sqlite3


---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository
bash
git clone https://github.com/YOUR_USERNAME/spam_mail.git
cd spam_mail

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py migrate

5️⃣ Start server
python manage.py runserver


Open browser:

http://127.0.0.1:8000/

🧠 ML Workflow

Text input from user

Text vectorized using TF-IDF

ML model predicts:

Spam ❌

Ham ✅

Result displayed on result page


👨‍💻 Author

-Sathees Kumar k
-B.Sc Computer Science
-Aspiring Python & ML Developer

📌 Future Enhancements

Email inbox integration

Model accuracy improvement

Cloud deployment

REST API support


---

