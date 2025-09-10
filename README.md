
# Car Price Predictor 🚗💸

ML-powered API for predicting used car prices. Built with **Python**, **FastAPI**, and **scikit-learn**, packaged in **Docker** with optional **Redis caching** and **Prometheus monitoring**.

---

## 🔍 Overview
- REST API for real-time predictions  
- Model serialized with `joblib`  
- Interactive docs at `/docs` (Swagger UI)  
- Runs easily with **Docker Compose**  

---

## ⚡ Quickstart

### Local
```bash
git clone https://github.com/Mihir945/car-price-predictor.git
cd car-price-predictor
pip install -r requirements.txt
uvicorn app.main:app --reload
````

### With Docker Compose (recommended 🚀)

Just one command builds and runs everything (API + optional Redis):

```bash
docker-compose up --build


## 🧾 Example Request

```json
POST /predict

```

Response:

```json
{ "predicted_price": 350000 }
```

---

## 🛠 Tech Stack

* Python, FastAPI, scikit-learn, joblib
* Docker, Docker Compose, Redis (optional), Prometheus (optional)

---

## 📬 Contact

Maintainer: **Mihir945**
📧 Email: *[mihirk860@gmail.com]*




