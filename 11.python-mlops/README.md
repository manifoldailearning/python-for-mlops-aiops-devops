# Set up EC2 Instance

Ensure port 80 is enabled
```
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo systemctl start docker
sudo service docker status
sudo groupadd docker
sudo usermod -a -G docker ec2-user
newgrp docker
docker —-version

# create ECR with name: my-flask-app
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 866824485776.dkr.ecr.us-east-1.amazonaws.com
```

```bash

curl -X POST -H "Content-Type: application/json" \
     -d '{"data": [[5.1, 3.5, 1.4, 0.2]]}' \
     http://127.0.0.1:5000/predict


curl -X POST -H "Content-Type: application/json" \
     -d '{"data": [[5.1, 3.5, 1.4, 0.2]]}' \
     http://54.172.91.243/predict
```