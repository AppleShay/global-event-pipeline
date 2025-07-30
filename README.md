# 🌍 Global Event Pipeline

An end-to-end ETL pipeline that fetches global news events from APIs, processes them, and stores them in MongoDB.  
Built with **Docker**, orchestrated with **docker-compose**, scheduled using **cron**, and fully automated with **GitHub Actions CI/CD** to DockerHub.

---

## 🚀 Features

- **ETL Automation**: Fetches events from the News API and stores in MongoDB.
- **Scheduled Runs**: Weekly cron job triggers ETL automatically.
- **Containerized Deployment**: All components run inside Docker containers.
- **Continuous Integration (CI)**: Automatically builds and tests on every push.
- **Continuous Deployment (CD)**: Automatically pushes Docker image to DockerHub.
- **Log Management**: Automated log rotation.

---

## 🛠 Tech Stack
- **Python** (FastAPI, Requests, PyMongo, NLTK, PyYAML)
- **MongoDB** (Data Storage)
- **Docker & docker-compose**
- **GitHub Actions** (CI/CD)
- **Cron** (Scheduling)

---

## 📂 Project Structure

```
global-event-pipeline/
│── ansible/ # Deployment automation (future)
│── api/ # API service
│── ci_cd/ # CI/CD configurations
│── config/ # Configurations (settings.yaml)
│── docker/ # Dockerfiles and docker-compose
│── etl/ # Extract, Transform, Load scripts
│── scripts/ # Utility scripts (log rotation, etc.)
│── tests/ # Test cases
│── .github/workflows/ # GitHub Actions CI/CD configs
│── requirements.txt # Python dependencies
│── docker-compose.yml # Multi-service orchestration
│── README.md # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AppleShay/global-event-pipeline.git
cd global-event-pipeline
```

### 2️⃣ Build & Run Containers

```bash
cd docker
docker compose build --no-cache
docker compose up
```

---

## ⏳ Scheduling with Cron

The ETL pipeline is scheduled to run weekly using a cron job:

```cron
0 9 * * 1 cd /mnt/b/DE/global-event-pipeline/docker && docker compose run etl
```

Logs are written to `/mnt/b/DE/global-event-pipeline/etl_weekly.log` and rotated automatically by the log rotation script.

---

## 🛠 Log Rotation

A custom log rotation script is included to prevent large log file sizes:

```bash
bash scripts/log_rotate.sh
```

This script automatically compresses and timestamps old logs when they exceed the configured size.

---

## 📡 API Access

Once the pipeline runs, the API is available at:

```
http://localhost:8000/events
```

It serves stored event data from MongoDB.

---

## 🔄 CI/CD Pipeline
CI: Runs tests and builds Docker images on every push.

CD: Pushes the Docker image to DockerHub automatically.

DockerHub Image:
```
docker pull appleshay/global-event-pipeline:latest
docker run appleshay/global-event-pipeline:latest
```

---
## 📌 Future Enhancements
- Versioned releases on DockerHub (v1.0.0, v1.1.0, etc.)

- Automated cloud deployment (AWS, GCP, or Swedish Science Cloud)

- Enhanced data analytics on ingested events
---

**Author:** Shaheryar (AppleShay)
**Repository:** [Global Event Pipeline](https://github.com/AppleShay/global-event-pipeline)
