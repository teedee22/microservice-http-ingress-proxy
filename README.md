# HTTP Proxy (ingress)

## Summary
Outer proxy entry to system.
Proxy receives a payload via http and publishes onto NATS

![Interaction Diagram](./docs/interaction-diagram.png)

## Endpoints
| Endpoint | REST | NATS subject | Description |
|---|---|---|---|
|/ | GET | n/a | *returns a healthcheck message* |
| /new | POST | foobar | *Passes through to nats channel foobar, which python worker (sleepy worker) picks up*
| /new2 | POST | foobar2 | *python worker calls python API from this route* |

## Payload
```json
{
    "message": "your message",
    "count": 4,
    "id": 0
}
```

## k8s deployment

```bash
kubectl apply -f nats-k8s.yaml
kubectl apply -f proxy-k8s.yaml
```

**Minikube note:**

If using minikube, you'll need tunnel to make the loadbalancer work
```bash
minikube tunnel
```

you can also run the dashboard from:
```bash
minikube dashboard
```