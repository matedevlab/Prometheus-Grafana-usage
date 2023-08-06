# Deploying an Application with Kubernetes and monitoring it with Prometheus and Grafana

This guide walks you through the process of deploying an application with Kubernetes using Minikube as your cluster, setting up Prometheus and Grafana for monitoring, and visualizing application data. I have already dockerized the application and uploaded it to my Docker Hub repository, so you don't have to worry about that. However, if you're interested in the application itself or the base of a Docker image, you can check out the 'Dockerfile' and 'app.py'.

## Task 1: Install Docker

1. Follow the guide to [Install Docker](https://docs.docker.com/engine/install/).

## Task 2: Deploy Resources with Kubernetes

1. Install `kubectl` by following the Kubernetes [installation guide](https://kubernetes.io/docs/tasks/tools/).
2. Install Minikube using [these instructions](https://minikube.sigs.k8s.io/docs/start/).
3. Start Minikube: Run `minikube start`.
4. Deploy your application using Kubernetes: Run `kubectl apply -f myapp-deployment.yaml`.

## Task 3: Visualize Application Data

1. Run `minikube tunnel` to create a network tunnel to your Minikube cluster.
2. Install Helm by following the [installation guide](https://helm.sh/docs/intro/install/).
3. Add the Prometheus Helm repository: `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`.
4. Update the Helm repositories: `helm repo update`.
5. Install Prometheus using Helm: `helm install --values=prometheus-values.yaml prometheus prometheus-community/prometheus`.
6. Add the Grafana Helm repository: `helm repo add grafana https://grafana.github.io/helm-charts`.
7. Update the Helm repositories: `helm repo update`.
8. Install Grafana using Helm: `helm install --values=grafana-values.yaml grafana grafana/grafana`.

## Task 4: Access Monitoring and Visualize Data

Run `kubectl get svc` to find the external IP of your application(myapp-service), Grafana(grafana), and Prometheus(prometheus-server).

Access Prometheus Monitoring:
- Open a web browser and type the external IP of the prometheus-server.
- Click on the "Status" option in the navigation menu.
- Click on "Targets" to view the target status.
- Search for "myapp". If you can see it marked as "UP," your application is healthy.
- Click on "Graph" next to the "Status" in the navigation menu.
- Start typing "my" and choose "myapp_requests_total" from the suggestions.
- Next to the "Table", select "Graph" as the visualization type.
- Click "Execute" on the right side. You will see a graph displaying the total requests from the myapp-service_external_ip/metrics endpoint.

Access Grafana and Import Dashboard:
- In your browser, type the external IP of the grafana server.
- Log in using the username "admin."
- Retrieve your Grafana admin password by running this command in your terminal: `kubectl get secret grafana -o=jsonpath='{.data.admin-password}' | base64 --decode`
- Copy the password without the '%' at the end.
- In Grafana, click on the top left toggle menu.
- Click on "Connections".
- Search for "Prometheus" and click on it.
- In the HTTP URL field, enter the URL of the prometheus-server: http://the_external_ip_of_prometheus-server.
- Save and exit the configuration.
- Click on "Dashboards" in the side menu.
- Click on "New" to create a new dashboard.
- Click on "Import" to import a dashboard.
- Copy the ID of the dashboard from this link: [dashboard_id](https://grafana.com/grafana/dashboards/11663-k8s-cluster-metrics/).
- Go back to Grafana and paste the copied dashboard ID.
- Click "Load" to load the dashboard.
- Under the "prometheus" option, select your previously created datasource named "Prometheus" (default name unless you changed it).
- Click "Import" and your dashboard is now available for visualization.
You're done! Your application data can now be monitored and visualized using Grafana.

## Conclusion

By following these steps, you have successfully deployed an application with Kubernetes, set up Prometheus and Grafana for monitoring, and visualized application data.
