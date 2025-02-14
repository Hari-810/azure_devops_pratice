Here’s a step-by-step guide to containerizing your Python app (`age_calc_docker`) using Docker.

---

### **Step 1: Install Docker (If Not Installed)**

If Docker is not installed, download and install it from [Docker's official website](https://www.docker.com/get-started/).

After installation, verify it by running:

```sh
docker --version
```

---

### **Step 2: Log in to Docker Hub (Optional)**

If you want to push your image to Docker Hub, log in:

```sh
docker login
```

Enter your Docker Hub username and password.

---

### **Step 3: Navigate to Your Project Directory**

Move into your project directory:

```sh
cd path/to/age_calc_docker
```

---

### **Step 4: Create a `Dockerfile`**

Inside `age_calc_docker`, create a file named `Dockerfile` (without an extension) and add the following content:

```dockerfile
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
```

---

### **Step 5: Build the Docker Image**

Run the following command inside `age_calc_docker`:

```sh
docker build -t age_calc_image .
```

This will create an image named `age_calc_image`.

---

### **Step 6: Run the Docker Container**

App requires ports (e.g., for a Flask API), expose them like this:

```sh
docker run -p 5000:5000 --name age_calc_container age_calc_image
```

Run your container using If doesn't need port:

```sh
docker run --name age_calc_container age_calc_image
```

- `--name age_calc_container`: Assigns a name to the container.
- `age_calc_image`: Uses the image built in step 5.

---

### **Step 7: Check Running Containers**

Open another terminal and run:

To see running containers:

```sh
docker ps
```

To check all containers (including stopped ones):

```sh
docker ps -a
```

---

### **Step 8: Stop and Remove a Container**

To stop a running container:

```sh
docker stop age_calc_container
```

To remove the container:

```sh
docker rm age_calc_container
```

---

### **Step 9: Push Image to Docker Hub (Optional)**

If you want to push the image to Docker Hub:

1. Tag the image:
   ```sh
   docker tag age_calc_image your_dockerhub_username/age_calc_image
   ```
2. Push the image:
   ```sh
   docker push your_dockerhub_username/age_calc_image
   ```

Now, others can pull and run it using:

```sh
docker pull your_dockerhub_username/age_calc_image
docker run --name age_calc_container your_dockerhub_username/age_calc_image
```

---

### **Step 10: Clean Up Unused Resources (Optional)**

Remove unused images:

```sh
docker image prune -a
```

Remove all stopped containers:

```sh
docker container prune
```

---
