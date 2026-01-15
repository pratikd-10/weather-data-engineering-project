import boto3
import requests
import json
from datetime import datetime

# ==========================================
# 1. CONFIGURATION (Fill these in!)
# ==========================================
ACCESS_KEY = "--------"
SECRET_KEY = "--------"
BUCKET_NAME = "weather-data-project-uniqueid" # e.g., weather-project-12345
REGION = "us-east-1" # Use the region you chose for your bucket

# ==========================================
# 2. FETCH: Get data from the API
# ==========================================
# This URL fetches current weather for London
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=True"

def fetch_data():
    print(f"[{datetime.now()}] Fetching data from API...")
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: {response.status_code}")

# ==========================================
# 3. DROP: Upload data to AWS S3
# ==========================================
def upload_to_s3(data):
    # Initialize the S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION
    )
    
    # We create a unique filename using the current timestamp
    filename = f"bronze/weather_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    print(f"[{datetime.now()}] Uploading to S3: {filename}...")
    
    # Convert Python dictionary to a JSON string
    json_data = json.dumps(data)
    
    # Upload to the 'bronze' folder
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json_data
    )
    print("✅ Successfully dropped to S3!")

# ==========================================
# 4. EXECUTION
# ==========================================
if __name__ == "__main__":
    try:
        raw_data = fetch_data()
        upload_to_s3(raw_data)
    except Exception as e:
        print(f"❌ Error: {e}")