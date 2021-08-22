# Vallox to influxdb via telegraf.

Docker instance to query a Vallox HVAC machine and send operational values with
telegraf to a influxdb.

## Setup

Create a .env file with your environments config, e.g.

```
VALLOX_HOST=10.0.0.220
INFLUXDB_HOST="influxdb.com:8086"
INFLUXDB_DB=db0
INFLUXDB_USER=user
INFLUXDB_PASS=password
```

## Run

```
docker-compose build
docker-compose up
```
