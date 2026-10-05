# Demo

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Run with Docker

```bash
docker build -t devops-agent:local .
docker run --rm -p 8080:8080 devops-agent:local
```

## Deploy with manifests

```bash
kubectl apply -f manifests/deployment.yaml
kubectl get pods,svc -l app=devops-agent
```

## Deploy with Helm

```bash
helm upgrade --install devops-agent ./helm/devops-agent
```
