docker build -t escalation-server .
docker tag escalation-server snovotney/escalation-server:0.9.1
docker push snovotney/escalation-server
