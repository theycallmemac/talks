# Simple Python Flask Containerized Application

Didn't give or even write this talk, that was all @CSmartt. I just wrote up the demo section of the talk, just a tiny flask app you could run with docker.

```bash
$ docker build -t username/flask-app .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 --name flask-app username/flask-app
```

