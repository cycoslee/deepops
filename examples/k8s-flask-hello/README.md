"Hello, World" service running in Kubernetes
============================================

This example demonstrates how to build a simple "hello, world" service that will run in our DeepOps Kubernetes cluster.

The instructions below assume that:

* You've built and deployed a Kubernetes cluster using DeepOps.
    (If you haven't done this yet, see the [Kubernetes guide](../../docs/kubernetes-cluster.md).)
* You have `kubectl` installed on your workstation, and configured to interact with your cluster.
* You have Docker installed on your workstation, to build the new image.

The application we're going to deploy is a simple Python Flask web service, `examples/k8s-flask-hello/flask-hello.py`.
It defines a single HTTP endpoint, which just replies to any request with "Hello from {hostname}".
For example:

```
$ curl http://localhost:5000/
Hello from my-happy-host
```

Our service will run in a Docker container defined by `examples/k8s-flask-hello/Dockerfile`.

1. Pick a Docker registry where you want to store your images.
    [Docker Hub](https://hub.docker.com/) is the public registry provided by Docker, Inc., and will be used in this example.
    If you don't have an account on the Docker Hub, you'll need one to follow this example.
1. Build 
    ```
    $ cd examples/k8s-flask-hello/
    $ ls
    
    $ docker build -t registry.local/flask-hello .
    $ docker push registry.local/flask-hello
    ``` 
1. Push the image to a Docker registry.
    ```
    
    ```
