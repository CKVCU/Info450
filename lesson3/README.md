Here’s a clean, polished, GitHub‑ready **Markdown README** for your API examples. It’s structured, clear, and beginner‑friendly while still showing exactly what your code does.

---

# 🐍 Introduction to APIs with Python  
A hands‑on walkthrough using `requests` to pull real data from public APIs.

This guide demonstrates how to:
- Make GET requests  
- Parse JSON responses  
- Work with public APIs (Cat Facts, World Cup data, GitHub JSON files, Weather APIs)  
- Perform simple data analysis on API results  

---

## 📦 Requirements  
Make sure you have the `requests` library installed:

```bash
pip install requests
```

---

## 🐱 Cat Facts API  
A simple API that returns random cat facts.

```python
import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()

data['fact']
data['length']
```

**What this does:**  
- Sends a GET request  
- Converts the response to JSON  
- Extracts the fact text and its character length  

---

## ⚽ World Cup API (OpenFootball JSON)  
Pulling match data for the 2026 World Cup.

```python
import requests

url = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"
response = requests.get(url)
data = response.json()

data['matches']
first_match = data['matches'][0]
match_55 = data['matches'][55]
match_55['score']['ft'][0]
```

**What this does:**  
- Loads a JSON file directly from GitHub  
- Accesses match data  
- Extracts full‑time scores for a specific match  

---

## 🗂️ Using Your Own GitHub Repo as an API  
Any raw JSON file on GitHub can be used like an API.

```python
import requests

url = "https://raw.githubusercontent.com/CKVCU/Info450/main/parts.json"
response = requests.get(url)
data = response.json()

data['parts'][1]['name']
```

**What this does:**  
- Reads your `parts.json` file  
- Accesses the second item’s name  

---

## 🌤️ Historical Weather API (Open‑Meteo)  
Fetching historical max temperatures for New York City.

```python
import requests

url = "https://historical-forecast-api.open-meteo.com/v1/forecast"

params = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "start_date": "2025-06-20",
    "end_date": "2025-06-26",
    "daily": "temperature_2m_max",
    "timezone": "auto"
}

response = requests.get(url, params=params)
data = response.json()

temps = data['daily']['temperature_2m_max']
```

### 🔍 Simple Analysis

```python
print("Max value is", max(temps))
min(temps)
max(temps)

range = max(temps) - min(temps)
range

sum(temps) / len(temps)
```

**What this does:**  
- Retrieves daily max temperatures  
- Calculates min, max, range, and average  

---

## 📘 Summary  
This README covers how to:

✔ Make API requests  
✔ Parse JSON  
✔ Work with public datasets  
✔ Use GitHub as a lightweight API  
✔ Perform basic data analysis on API results  

You now have a solid foundation for working with APIs in Python.

---

If you want, I can also:  
- Add screenshots  
- Add a table of contents  
- Turn this into a Jupyter Notebook  
- Add error handling and best practices  

Just tell me what you want next.
