
# PROG8850 Group Project – Signoz Monitoring for MySQL Logs

## 📌 Project Overview

This project involves setting up a real-time monitoring stack using **Signoz**, **Clickhouse**, and **OpenTelemetry Collector**. The stack collects logs (simulated MySQL logs), sends them to a telemetry pipeline, and visualizes them in the Signoz dashboard with alerting and external access via ngrok.

---

## 🧰 Software/Tools Used

| Tool/Software         | Purpose                                             |
|----------------------|-----------------------------------------------------|
| Docker               | Containerization of all components                  |
| Docker Compose       | Define and manage multi-container apps             |
| Signoz               | Observability tool to visualize logs/metrics        |
| Clickhouse           | Backend columnar DB for telemetry data              |
| OpenTelemetry Coll.  | Collector for processing and exporting logs         |
| ngrok                | Expose local Signoz server to public                |
| Simulated MySQL Logs | To demonstrate monitoring setup                     |
| CMD/Terminal         | To run all setup and docker commands                |

---

## 🧩 Architecture Flow

1. Simulated MySQL logs are generated.
2. OpenTelemetry Collector reads and processes the logs.
3. The logs are exported to Clickhouse.
4. Signoz queries Clickhouse to display logs in its UI.
5. The Signoz dashboard is exposed to the web via **ngrok**.

---

## 📁 Project Structure

```
PROG8850-Group-Project/
├── docker-compose.yaml
├── otel-collector-config.yaml
├── screenshots/
│   ├── all-screenshots.png
├── README.md
└── group-report.pdf
```

---

## ⚙️ Setup Instructions

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/PROG8850-Group-Project.git
cd PROG8850-Group-Project
```

### ✅ Step 2: Create Configuration File

Create `otel-collector-config.yaml` with:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

exporters:
  clickhouse:
    endpoint: tcp://clickhouse:9000
    database: signoz_traces
    username: default
    password: ""
    tls:
      insecure: true

processors:
  batch:

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [clickhouse]
```

### ✅ Step 3: Run Docker Compose

```bash
docker-compose down --volumes --remove-orphans
docker-compose up -d
```

Check all services using:

```bash
docker ps
```

---

## 🔍 Access Signoz

- Default UI: [http://localhost:3301](http://localhost:3301)
- With ngrok:

```bash
ngrok http 3301
```

Copy the public ngrok link to access Signoz from outside.

---

## 📦 Simulate Logs

You can simulate logs from your terminal or Python script.

```bash
echo "ERROR: DB query timeout at 2025-04-16 15:00:01" >> /tmp/mysql.log
```

Use OpenTelemetry to collect and forward them into Signoz.

---

## 📊 Dashboard and Alerts

1. Access the Signoz UI.
2. Navigate to **Dashboards** > Create a new panel.
3. Add 2–3 widgets (e.g., error count, log trend).
4. Go to **Alerts**, and set a rule for error keyword.

---

## ✅ Task Completion

- [x] All containers deployed via Docker
- [x] Configuration for telemetry pipeline
- [x] Logs collected and visualized in Signoz
- [x] Dashboard created with 3 visualizations
- [x] Alert set for "ERROR" logs
- [x] External access via ngrok working

---

## 👥 Group Members

- Hema Priya – Container Setup, Collector Config
- Member 2 – Log Simulation & Alert Setup
- Member 3 – Dashboard Panels & Report
- Member 4 – Screenshots & Submission

---

## 📄 Submission Checklist

- ✅ `docker-compose.yaml`
- ✅ `otel-collector-config.yaml`
- ✅ Screenshots of Dashboard + Alerts + Logs
- ✅ PDF Report (`group-report.pdf`)
- ✅ `README.md`

---

## 🏁 Conclusion

This project helped us learn real-time monitoring, telemetry pipelines, containerization, and alerting using open-source tools. It simulates real industry DevOps use cases using Signoz and Docker.
