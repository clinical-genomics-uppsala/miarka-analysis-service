# miarka-analysis-service
Repository for building/testing a microservice that can perform necessary file operations and start a snakemake pipeline on miarka.

Getting Started
===============
Download 
--------
```
git clone git@github.com:clinical-genomics-uppsala/miarka-analysis-service.git
cd miarka-analysis-service
```

Create environment 
-------------------
Create a virtual environment and install arteria and tornado.
```
virtualenv venv -p python3.10
source venv/bin/activate
pip3 install -r requirements.txt
```
Installation
------------
```
python setup.py install
```

Start service
-------------
```
analysis-ws --config config/ --port 8080 --debug
```

Get version and make sure service is up
-------------
```
curl http://localhost:8080/api/1.0/version
```

Start "analysis"
-------------
```
curl -X POST -w '\n' --data '{"wp": "wp1", "analysis": "GMS560", "inbox_path": "/path/to/inbox/"}' http://localhost:8080/api/1.0/start
```

Set-up using the Dockerfile
-------------
```
docker build -f miarka-analysis-service.Dockerfile -t miarka-analysis-service .

docker run --name miarka-analysis-service \
-v ./scripts:/opt/miarka-analysis-service/scripts \
-d -p 8080:8080 miarka-analysis-service:latest
```
(To see the service log, omit the -d-flag.)

Use `docker inspect` to find the IP of your running container to use in the commands below.

```

curl http://172.17.0.2:8080/api/1.0/version

curl -X POST -w '\n' --data '{"wp": "wp1", "analysis": "GMS560", "inbox_path": "/path/to/inbox/"}' \
http://172.17.0.2:8080/api/1.0/start
```