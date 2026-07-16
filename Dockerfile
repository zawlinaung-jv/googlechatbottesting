FROM python:3.10-slim

WORKDIR /app

# Dependency များ သွင်းခြင်း
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ကုဒ်များအားလုံးကို Container ထဲ ကူးထည့်ခြင်း
COPY . .

# Bot ကို Gunicorn ဖြင့် Run ပါ (Port 10000 ကို Render အတွက် အသုံးပြုပါ)
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]