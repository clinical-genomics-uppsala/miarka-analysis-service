FROM rockylinux/rockylinux:8.10

RUN yum -y update 
RUN yum -y upgrade
RUN yum -y install python3.12
RUN yum -y install python3.12-pip 

RUN mkdir -p /opt/miarka-analysis-service/ 

COPY ./ /opt/miarka-analysis-service/

WORKDIR /opt/miarka-analysis-service/

RUN pip3 install backports.ssl_match_hostname 

RUN pip3 install -r requirements.txt

RUN python3.12 setup.py install

ENTRYPOINT ["miarka-analysis-ws","--config","./config/","--port","8080","--debug"]

