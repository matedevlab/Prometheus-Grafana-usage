# Tinker Tailor Docker Spy

## Story

Basically, you got the million dollar idea. It is an application that you made in codecool a while back. However, as every application needs to run somewhere constantly, and as they require a a bigger amount of resources, your laptop just won't cut it. And that is why you're thinking about moving it to cloud. Managing projects on a bigger scale requires cooperation. Even from people you don't know! Using packages from other open source projects could accelerate your progress quite a bit. So you should use other people's packages for Kubernetes deployments. As you can't do those with the default Kubernetes configuration files, how you might ask? The answer is Helm.

## What are you going to learn?

- How to dockerize your application
- Host your application on k8s
- How to build a monitoring stack for your app in k8s
- Use helm effectively to install software to your cluster

## Tasks

1. Dockerize an application from any of your projects. It could be any backend project with an endpoint, that can handle requests, and gives back a response.
    - The application runs successfully inside the container.

2. Upload your image to a registry. 
    - The image can be found in the registry.

3. Create a k8s yaml config file for your application, and deploy it to the cluster, along with Prometheus and Grafana.
    - Your application, Prometheus, Grafana are in a running state inside the cluster.

4. Configure your metrics stack to monitor your application, and check it along with your app.
    - The monitoring information about your application can be successfully checked, and your app also returns a response after calling the endpoint.

5. Upgrade your k8s config files to use Helm
    - Your application, Prometheus, Grafana are in a running state inside the cluster.

## General requirements

None

## Hints

- Use EKS instead of minikube for making sure that you don't have to host your cluster locally
- Use ECR for your repository to store your images
- With Helm, you don't need the source code of the package to install it on your cluster. E.g. you can install Prometheus with ```helm upgrade --install prometheus prometheus-community/prometheus```
- If you need to include your own variables as arguments to a Helm package, you can use the ```-f``` flag. E.g. ```helm upgrade --install prometheus prometheus-community/prometheus -f values-$BUILD_ENVIRONMENT.yaml```
- Similar to the ```-f``` flag, you can also include arguments straight from the command line, as opposed to from a yaml file with the ```--set``` flag.

## Background materials

- <i class="far fa-exclamation"></i> [Grafana dashboards](https://grafana.com/grafana/dashboards)
- <i class="far fa-exclamation"></i> [Introduction to Helm page](project/curriculum/materials/pages/devops/introduction-to-helm.md)
- <i class="far fa-book-open"></i> [Helm chart template](https://helm.sh/docs/chart_template_guide/)
- <i class="far fa-exclamation"></i> [Helm vs Kubectl](https://medium.com/@RedBaronDr1/helm-vs-kubectl-5aaf2dba7d71)
