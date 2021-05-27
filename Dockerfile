FROM python:3

WORKDIR /home/markelov/app_crypto

COPY PythonApplication1.py PythonApplication1.py
COPY my_text.txt my_text.txt
COPY my_proverb.txt my_proverb.txt

CMD [ "python", "./PythonApplication1.py" ] 