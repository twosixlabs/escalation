docker build -t escalation-server .
docker tag escalation-server snovotney/escalation-server:0.7.8
docker push snovotney/escalation-server
