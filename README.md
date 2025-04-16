
# 📘 PROG8850 Group Project – Signoz Monitoring & MySQL Logs Visualization

## 🧠 Project Objective

This group project aims to monitor and analyze MySQL database activity using a fully containerized stack consisting of **Signoz**, **Clickhouse**, and **OpenTelemetry Collector**. The pipeline collects MySQL logs, sends them to Clickhouse, and displays visualizations and alerts on Signoz dashboards.

This README explains everything done so far and outlines what remains to be done. It also divides responsibilities clearly.

---

## ✅ Work Completed by Hema Priya (Me)

### ✔️ 1. Project Setup & Folder Structure

- Created local folder: `PROG8850-Group-Project`
- Created subfolders: `sql/`, `scripts/`, `.github/workflows/`
- Created and edited files using command prompt:
  - `sql/create_table.sql`, `add_column.sql`, `insert_data.sql`
  - `scripts/multi_thread_queries.py`
  - `.github/workflows/ci_cd_pipeline.yml`

### ✔️ 2. GitHub Repository Setup

- Initialized local git repository
- Linked to GitHub: https://github.com/hema8293/PROG8850-Group-Project.git
- Committed and pushed all files

### ✔️ 3. CI/CD GitHub Actions Pipeline

- Created and committed working `ci_cd_pipeline.yml` file
- Ran pipeline: deployed MySQL schema + executed Python script ✅
- Debugged errors: MySQL socket, Python name errors, thread issues

### ✔️ 4. Docker & Signoz Setup

- Installed Docker Desktop (Windows)
- Cloned Signoz deployment repo
- Pulled all required images
- Resolved port conflicts (8080) and started containers with:

```bash
docker-compose down
docker-compose up -d
```

- Verified containers: `signoz`, `clickhouse`, `otel-collector`, `query-service`, etc.

### ✔️ 5. ngrok Setup

- Logged into ngrok, started tunnel:

```bash
ngrok http 3301
```

- Shared ngrok URL to access Signoz from browser

### ✔️ 6. Debugging Signoz Errors

- Investigated and fixed:
  - Clickhouse TCP port not binding (9000 conflict)
  - otel-collector startup config errors
  - signoz-query-service crashing due to SQLite lock

---

## 🚧 Work Remaining (Can Be Split Among Group Members)

### 🧑‍💻 Member 2 – Log Simulation

- Simulate logs from MySQL using a script or CLI command
- Inject logs like:

```bash
echo "ERROR: MySQL timeout" >> /tmp/mysql.log
```

- Verify they appear in Signoz logs tab

### 📊 Member 3 – Create Dashboards in Signoz

- Access Signoz using ngrok link or `localhost:3301`
- Create a new dashboard with at least 3 widgets:
  - Error log trend (line chart)
  - Count of errors by time (bar chart)
  - Table of log messages

### 🚨 Member 4 – Setup Alerting in Signoz

- Navigate to **Alerts > Create Alert**
- Condition: Log count > 3 with keyword "ERROR"
- Add alert name, severity, and dummy notification rule
- Capture screenshots

### 📸 All Members – Final Screenshots

- Dashboard view
- Alerts page with triggered alerts
- Container view in Docker
- GitHub Actions run success
- ngrok URL exposed and accessible

---

## 🧪 Testing & Verification

- CI/CD pipeline: ✅ Passed
- Docker containers: ✅ Running successfully
- Signoz: ⚠️ Some services restarted—requires log retry
- ngrok: ✅ Active and accessible

---

## 🧩 Technologies Used

| Tool/Software         | Purpose                                 |
|----------------------|------------------------------------------|
| Docker               | Containerized the stack                  |
| Docker Compose       | Manage multi-container Signoz services   |
| GitHub Actions       | CI/CD pipeline for DB + Python scripts   |
| MySQL                | Simulated database                       |
| Signoz               | Observability dashboard                  |
| Clickhouse           | Store telemetry/log data                 |
| Python               | Multithreaded query simulator            |
| ngrok                | Public access to localhost dashboard     |

---

## 📂 Project Structure

```
PROG8850-Group-Project/
├── sql/
│   ├── create_table.sql
│   ├── insert_data.sql
│   └── add_column.sql
├── scripts/
│   └── multi_thread_queries.py
├── .github/workflows/
│   └── ci_cd_pipeline.yml
├── docker-compose.yaml
├── otel-collector-config.yaml
├── screenshots/
│   ├── dashboard.png
│   ├── alerts.png
│   ├── logs.png
│   └── github-success.png
└── README.md
```

---



## 👩‍💻 Group Members & Roles

| Member Name     | Role / Work Area                        |
|------------------|------------------------------------------|
| Hema Priya       | Docker, GitHub, Pipeline, Troubleshooting |
| Member 2         | Log Simulation, Test MySQL errors        |
| Member 3         | Dashboard in Signoz                      |
| Member 4         | Alerts, Screenshot compilation           |

---

## ✅ Submission Checklist

- [x] Functional CI/CD Pipeline
- [x] Dockerized Signoz stack
- [x] ngrok tunnel live
- [ ] Logs simulated and visible in UI
- [ ] Dashboard with widgets created
- [ ] Alert configured for log trigger
- [ ] All screenshots ready
- [ ] Final PDF and ZIP created

---

## 📌 Final Note

This project brings together Docker, observability, automation pipelines, and real-time log monitoring — giving us hands-on skills highly valued in DevOps and SRE roles.
