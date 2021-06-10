FROM python:3

WORKDIR /home/markelov/app_crypto

COPY Unittests.py Unittests.py
COPY my_text.txt my_text.txt
COPY my_proverb.txt my_proverb.txt

CMD [ "python", "./Unittests.py" ] 