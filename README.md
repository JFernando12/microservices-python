Add domains to C:\Windows\System32\drivers\etc\hosts
127.0.0.1 rabbitmq-manager.com
127.0.0.1 mp3converter.com

Install ingress-nginx:
Site: https://kubernetes.github.io/ingress-nginx/deploy/#quick-start
URL: kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.12.1/deploy/static/provider/cloud/deploy.yaml

Create rabbitMQ Queues in: rabbitmq-manager.com
username: guest
password: guest