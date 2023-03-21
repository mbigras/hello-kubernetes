# App

> App app.py is for testing application delivery workflows—see https://www.hashicorp.com/resources/application-delivery-hashicorp.

## Getting started

The following procedure describes how to build and run app Docker container.

1. Install Docker—see [_Get Docker_](https://docs.docker.com/get-docker/).

1. Get the app code.

   ```
   git clone ...
   cd hello-kubernetes/app
   ```

1. Build app Docker image.

   ```
   docker build -t app .
   ```

1. Run app Docker container.

   ```
   docker run -it --name app -p 8080:80 app
   ```

   Your output should look like the following.

   ```
   $ docker run -it --name app -p 8080:80 app
   [2023-03-21 19:06:07 +0000] [1] [INFO] Starting gunicorn 20.1.0
   [2023-03-21 19:06:07 +0000] [1] [INFO] Listening at: http://0.0.0.0:80 (1)
   [2023-03-21 19:06:07 +0000] [1] [INFO] Using worker: sync
   [2023-03-21 19:06:07 +0000] [7] [INFO] Booting worker with pid: 7
   ```

   Consider the following details about that `docker run` command.

   1. The `--name app` option names your Docker container _app_. **Gotcha:** If you already have a container named _app_ on your machine (even if the container isn't running), then your `docker run` command will fail with an error message like `The container name "/app" is already in use by container`. You can remove that _app_ container with the `docker rm -f app` command. **Note:** To automatically remove your _app_ container when it stops, add the `--rm` option.
   1. The `-p 8080:80` binds port 8080 on your laptop to port 80 inside your container; therefore, you should send your test request to port 8080. **Gotcha:** Docker networking integration with macOS is confusing since the Docker daemon runs inside a Linux virtual machine on your laptop; therefore, use the explicit `-p/--publish` options instead of the `--network host` option.

1. In a new terminal, send a test GET HTTP request.

   ```
   curl localhost:8080
   ```

   Your output should look like the following.

   ```
   $ curl localhost:8080
   {
     "app": "app",
     "env": "docker-desktop",
     "features": "some,dev,features"
   }
   ```

1. In the terminal with your running container, stop your _app_ container.

   Press <kbd>Ctrl</kbd> + <kbd>C</kbd> keystroke.


1. Remove your _app_ container.

   ```
   docker rm app
   ```

   Your output should look like the following.

   ```
   $ docker rm app
   app
   ```
