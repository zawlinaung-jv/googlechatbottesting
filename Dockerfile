FROM python:3.10-slim

WORKDIR /app

# Dependency များ သွင်းခြင်း
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ကုဒ်များအားလုံးကို Container ထဲ ကူးထည့်ခြင်း
COPY . .

# Flask application ကို gunicorn ဖြင့် run ပါ (app:app ဆိုသည်မှာ app.py ဖိုင်ထဲမှ app object ကို ဆိုလိုသည်)
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]