# NessusVisualizer
A plotly dash web app to visualise Nessus report.

## Setup locally

```
$ make venv

$ source .env/bin/activate

$ make dependencies
```

## Start

```
$ python app.py

Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'app'
 * Debug mode: on
```

## Docker

```
$ docker build -t nessus_visualizer:0.1.0 .
$ docker run -p 80:8050 nessus_visualizer:0.1.0 .
```