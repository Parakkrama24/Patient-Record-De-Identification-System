# 🏥 EHR De-Identification System (MVP)

A FastAPI-based application for **automatic de-identification of patient records**, designed to remove Personally Identifiable Information (PII) and replace it with realistic synthetic data for safe research usage.

---

## 🚀 Project Overview

Healthcare data is highly sensitive and cannot be easily shared due to privacy regulations. This project solves that problem by:

* Detecting PII using **Regex + NLP (spaCy)**
* Replacing sensitive data with **synthetic values**
* Preserving structure and usability of records

---

## 🧠 Features (MVP)

* ✅ FastAPI REST API
* ✅ Hybrid PII Detection

  * Regex (phone, email)
  * NLP (names, locations, dates)
* ✅ Anonymization Engine
* ✅ Synthetic Data Generation
* ✅ Swagger UI for testing

---

## 🏗️ Project Structure

```
ehr-deid-system/
│
├── app/
│   ├── main.py
│   ├── services/
│   │   ├── pii_detector.py
│   │   ├── anonymizer.py
│   │   ├── synthetic_generator.py
│   │   └── pipeline.py
│   │
│   ├── utils/
│   │   └── regex_patterns.py
│
├── venv/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Project

```
git clone <your-repo-url>
cd ehr-deid-system
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

#### Activate:

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install fastapi uvicorn spacy faker
```

---

### 4. Download NLP Model

```
python -m spacy download en_core_web_sm
```

---

### 5. Run the Server

Make sure you are in the **project root directory**

```
uvicorn app.main:app --reload
```

---

## 🌐 API Access

Once the server is running:

* Swagger UI (Interactive API Docs):
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* Base URL:
  👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📡 API Endpoints

### 🔹 1. Health Check

**GET /**

```
GET /
```

Response:

```json
{
  "message": "EHR De-Identification API is running"
}
```

---

### 🔹 2. De-identify Patient Record

**POST /deidentify**

```
POST /deidentify
```

#### Request Body:

```json
{
  "text": "Patient John Silva visited Colombo on 2024-05-10. Call 0771234567 or john@gmail.com"
}
```

---

#### Response Example:

```json
{
  "original_text": "Patient John Silva visited Colombo on 2024-05-10...",
  "deidentified_text": "Patient Nimal Perera visited Kandy on 1999-02-12..."
}
```

---

## 🔄 How It Works

1. Input text is received via API
2. PII Detection:

   * Regex → phone, email
   * NLP → name, location, date
3. Entities are extracted
4. Synthetic values are generated
5. Text is replaced safely
6. Clean data is returned

---

## ⚠️ Limitations (Current MVP)

* Not trained on healthcare-specific datasets
* May miss:

  * NIC numbers
  * Hospital IDs
  * Clinical codes
* English-only model

---

## 🚀 Future Improvements

* Integrate advanced PII detection engine
* Add Sri Lankan-specific patterns (NIC, phone formats)
* Train custom NLP model
* Support PDF/DOC uploads
* Add authentication & security layer
* Store processed records

---

## 🧑‍💻 Tech Stack

* FastAPI
* Python
* spaCy (NLP)
* Faker (Synthetic Data)
* Uvicorn (Server)

---

## 📌 Notes

This is an MVP focused on:

* Simplicity
* Modularity
* Extensibility

Built to evolve into a **production-grade healthcare data anonymization system**.

---

## 🤝 Contribution

Feel free to fork and improve the project.

---

## 📄 License

MIT License

add section as navalty 
