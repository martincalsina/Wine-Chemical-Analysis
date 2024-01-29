from flask import Flask
import requests
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/download_csv')
def download_csv():

    api_url = "https://storage.googleapis.com/the_public_bucket/wine-clustering.csv"

    script_dir = os.path.dirname(os.path.realpath(__file__))

    download_path = os.path.join(script_dir, "data", "wine-clustering.csv")
    
    response = requests.get(api_url)

    if response.status_code == 200:

        csv_data = BytesIO(response.content)

        with open(download_path, 'wb') as f:
            f.write(csv_data.getvalue())

        return f'The data was correctly downloaded in {download_path}'
    else:
        
        return "There was an error trying to download the data", 500

if __name__ == '__main__':
    app.run(debug=True)
