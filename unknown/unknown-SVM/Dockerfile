FROM python:3.11.2
WORKDIR /code
COPY main.py .
COPY requirements.txt /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt-get update && apt-get install -y gcc python3-dev libffi-dev 
RUN pip install pandas 
RUN pip install scikit-learn

EXPOSE 8008

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8008"]
