# GPS Fleet Anomaly Detector

A Python-based telematics data analysis tool that simulates vehicle tracking data and detects driving anomalies such as harsh braking events and speeding violations.

## What It Does

- **Simulates realistic GPS telematics data** from multiple vehicles
- **Detects driving anomalies**: speeding events, harsh braking, unusual patterns
- **Generates fleet health reports** with actionable insights
- **Includes automated testing suite** with pytest
- **Containerized with Docker** for easy deployment

## Project Structure
```
fleet-analyzer/
├── data_generator.py      # Generate simulated vehicle telematics data
├── analyzer.py            # Anomaly detection and health report generation
├── test_analyzer.py       # Unit tests with pytest
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container configuration
└── README.md             # This file
```

## Quick Start

### Prerequisites
- Python 3.8+
- pip
- Docker (optional)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/techo-anant/gps-fleet-anomaly-detector.git
cd gps-fleet-anomaly-detector
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Run tests**
```bash
pytest test_analyzer.py -v
```



### Usage

1. **Generate telematics data**
```bash
python generate_vehicle_data.py
```
This creates `fleet_data.csv` with simulated GPS data for 5 vehicles.

2. **Run anomaly detection**
```bash
python analyzer.py
```

### Docker Usage

**Build the image:**
```bash
docker build -t gps-fleet-anomaly-detector .
```

**Run the container:**
```bash
docker run gps-fleet-anomaly-detector
```


Output example:
```json
{
  "total_vehicles": 5,
  "speeding_events": 12,
  "harsh_brakes_by_vehicle": {
    "ID-000": 3,
    "ID-001": 5,
    "ID-002": 2,
    "ID-003": 4,
    "ID-004": 1
  }
}
```

## Data Format

The simulated telematics data includes:

| Field | Description | Example |
|-------|-------------|---------|
| `vehicle_id` | Unique device identifier | GO-001 |
| `timestamp` | Data collection time | 2024-02-13 14:30:45 |
| `latitude` | GPS latitude | 43.6532 |
| `longitude` | GPS longitude | -79.3832 |
| `speed_kph` | Vehicle speed in km/h | 85.3 |
| `harsh_brake_event` | Boolean flag for harsh braking | True/False |

## Features

### Anomaly Detection
- **Speeding Detection**: Flags vehicles exceeding configurable speed thresholds
- **Harsh Braking Analysis**: Counts and reports sudden deceleration events
- **Per-Vehicle Health Scoring**: Aggregated metrics for fleet management

### Data Generation
- Realistic GPS coordinate drift
- Random speed variations with edge cases
- Configurable anomaly injection rates
- Supports multiple vehicle simulation

### Testing
- Unit tests for core analysis functions
- Test data generation for isolated testing
- Pytest fixtures for repeatable tests

## Technical Stack

- **Python 3.11**: Core language
- **pandas**: Data manipulation and analysis
- **pytest**: Test framework
- **Docker**: Containerization

## Use Cases

This project demonstrates skills relevant to:
- **Embedded IoT device testing** (simulating hardware output)
- **Telematics data pipelines** (processing GPS/sensor data)
- **Software-in-the-Loop (SIL) testing** (testing without physical devices)
- **Fleet management systems** (real-time anomaly detection)

## Acknowledgments

Inspired by real-world telematics systems and fleet management platforms.

---

**I built this in short project as a demonstration of rapid prototyping and embedded systems testing skills. My primary experience with production embedded systems is with Glendor Inc. (private repository).**