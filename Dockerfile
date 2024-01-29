FROM python:3.11

WORKDIR /

COPY load_data.py .
COPY Wine_Analysis.ipynb .
COPY Challenge_Wine_Clustering.pdf .

RUN mkdir /data

RUN pip install requests==2.31.0 pandas==2.1.1 numpy==1.24.3 matplotlib==3.7.2 seaborn==0.12.2 scikit-learn==1.3.0 flask==2.2.5 jupyter

EXPOSE 5000

CMD ["bash", "-c", "python load_data.py & sleep 10 && jupyter nbconvert --to notebook --inplace --execute Wine_Analysis.ipynb"]