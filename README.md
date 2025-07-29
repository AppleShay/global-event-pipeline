# 🌍 Global Event Pipeline

An automated ETL pipeline that fetches global news events from an external API, stores them in MongoDB, and exposes them through an API service. Scheduled to run weekly using `cron` for continuous updates.

---

## 🚀 Features

* **Automated ETL**: Extracts data from News API, transforms it, and loads into MongoDB.
* **Weekly Scheduling**: Cron job configured for automated weekly runs.
* **Containerized Deployment**: Uses Docker and Docker Compose for consistent builds.
* **REST API Access**: API service to retrieve stored events.
* **Log Management**: Automatic log rotation to prevent large file sizes.

---

## 📂 Project Structure

```
global-event-pipeline/
│
├── ansible/                  # (Optional) Deployment automation
├── api/                      # API service code
├── ci_cd/                    # CI/CD pipelines
├── config/                   # Configuration files (e.g., settings.yaml)
├── docker/                   # Dockerfiles and Compose config
├── etl/                      # ETL scripts
├── scripts/                  # Utility scripts (log rotation, cron jobs)
├── tests/                    # Unit and integration tests
├── .gitignore                
├── Dockerfile.api            # API container
├── Dockerfile.etl            # ETL container
├── docker-compose.yml        # Service orchestration
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
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

## 📌 Next Steps

* Add CI/CD pipeline (GitHub Actions / Ansible).
* Enhance API with filtering and pagination.
* Add unit and integration tests.

---

**Author:** Shaheryar (AppleShay)
**Repository:** [Global Event Pipeline](https://github.com/AppleShay/global-event-pipeline)
