FROM python:3.9-alpine
RUN echo 'NBCTF{SSTI_1s_fUn_I_c4nT_w4iT_Th3y_Inv3nT_Pyth0n}' > /flag.txt
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src .
RUN python create_and_fill_bdd.py
CMD flask run --host=0.0.0.0 --port=1337
