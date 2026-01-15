# weather-data-engineering-project

🌦️ Weather Data Engineering Pipeline

An end-to-end Data Engineering project that ingests real-time weather data using APIs, streams it via Apache Kafka, stores it in AWS S3 using a Medallion Architecture (Bronze–Silver–Gold), and processes it using Apache Spark on Databricks Free Edition.

This project is designed to simulate a real-world production pipeline while working within free-tier limitations.

📌 Project Architecture
Weather API
   ↓
Kafka Producer (Python)
   ↓
Kafka Topic
   ↓
Kafka Consumer (Python)
   ↓
AWS S3 (Bronze Layer)
   ↓
Databricks (Spark Processing)
   ↓
Silver Layer (Cleaned Data)
   ↓
Gold Layer (Aggregated Data)
   ↓
SQL Analytics & Visualization



🧰 Tech Stack
Category	                Technologies
Programming	              Python
Cloud Storage	            AWS S3
Streaming	                Apache Kafka
Compute	                  AWS EC2
Containerization	        Docker
Data Processing	          Apache Spark (Databricks Free Edition)
Analytics	                Databricks SQL
Architecture	            Medallion (Bronze–Silver–Gold)



📁 Repository Structure
weather-data-engineering/
│
├── producer/
│   └── producer.py              # Fetches weather data & sends to Kafka
│
├── consumer/
│   └── consumer.py              # Consumes Kafka data & stores in S3
│
├── ingestion/
│   └── weather_api_ingestion.py # Direct API → S3 ingestion (Stage 1)
│
├── databricks/
│   ├── bronze_to_silver.py      # Spark transformations
│   ├── silver_to_gold.py        # Aggregations
│   └── analysis.sql             # SQL queries for analytics
│
├── docker/
│   └── docker-compose.yml       # Kafka setup
│
├── data/
│   └── sample_weather.jsonl     # Sample dataset (for Databricks Free)
│
└── README.md




🔹 Stage 1: Data Ingestion (API → S3)
🎯 Goal

Collect raw weather data from an external API and store it securely in AWS S3.

🔧 Steps

Create S3 Bucket
weather-data-project-<unique-id>


Create folders

bronze/   # raw JSON data
silver/   # cleaned data
gold/     # aggregated data


Create IAM User

Programmatic access
AmazonS3FullAccess
Python Ingestion Script
Uses requests to fetch weather data
Uses boto3 to upload JSON files into S3 (bronze)

📌 Why S3?
S3 acts as a data lake, providing durability, scalability, and low cost.





🔹 Stage 2: Streaming Layer (Kafka)
🎯 Goal

Introduce real-time streaming to decouple ingestion and storage.

🔧 Steps

Launch EC2 Instance
Ubuntu t3.micro
Install Docker
Kafka runs inside Docker containers
Kafka Producer
Fetches weather data from API
Sends messages to Kafka topic
Kafka Consumer
Reads messages from Kafka topic
Stores each record as JSON in S3 bronze folder

📌 Why Kafka?

Buffers data
Prevents data loss
Decouples producers and consumers

⚠️ Note:
Due to Databricks Free Edition limitations, Kafka → Spark ingestion is simulated. Data is manually uploaded for Spark processing.





🔹 Stage 3: Data Processing (Spark + Databricks)
🎯 Goal

Transform raw data into analytics-ready datasets.

🔧 Steps
1. Bronze Layer

Raw JSON/JSONL data uploaded manually into Databricks

2. Silver Layer

Flatten nested JSON
Convert timestamps
Remove invalid or null records

3. Gold Layer

Aggregated metrics:
Average temperature per city per day

📌 Why Medallion Architecture?
Separates raw, cleaned, and business-ready data
Improves data quality and maintainability




📊 Analytics & Visualization

SQL queries run on Gold tables

Databricks SQL Editor used
Dashboards created using Databricks UI

Examples:
Daily average temperature trends
City-wise comparisons




🔍 Observability (Conceptual)

Row counts and basic metrics tracked
Demonstrates understanding of data quality monitoring
MLflow concepts applied where possible (limited in Free Edition)


🚀 Future Enhancements

Full S3 ↔ Databricks integration
Automated scheduling using Airflow
Real-time Spark Structured Streaming
Alerts on data quality issues



🏁 Conclusion

This project demonstrates a practical, industry-aligned Data Engineering workflow, showcasing:

API ingestion
Streaming pipelines
Cloud storage
Spark-based transformations
Analytics-ready outputs

Despite free-tier constraints, the pipeline mirrors real production systems and is suitable for Data Engineering interviews and portfolios.




