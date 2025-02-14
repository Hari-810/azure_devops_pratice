To set up Docker networking with two Python containers running Flask, I'll guide you through:

1. **Logging in to Docker**
2. **Writing Flask apps for two containers**
3. **Creating a Docker network**
4. **Building and running the containers**
5. **Networking the containers** (Linking, exposing ports, and routing)

---

## **Step 1: Log in to Docker**

If you are using Docker Hub, log in using:

```sh
docker login
```

Enter your credentials when prompted.

---

## **Step 2: Create Flask Applications**

We'll create two Flask applications:

- **App 1 (Container 1)** will be the main app and will make requests to **App 2 (Container 2)**.
- **App 2 (Container 2)** will return a response.

The Python files (`app1.py` and `app2.py`) should be in **separate folders** because each Flask app has its own Dockerfile and runs independently in its own container.

---

### **Recommended Folder Structure**

```
docker-networking/
│-- app1/
│   ├── app1.py
│   ├── requirements.txt
│   ├── Dockerfile
│
│-- app2/
│   ├── app2.py
│   ├── requirements.txt
│   ├── Dockerfile
```

### **Why Separate Folders?**

1. **Isolation:** Each service should be built and managed independently.
2. **Docker Context:** Each `Dockerfile` should only copy the relevant app files.
3. **Scalability:** If you later use **Docker Compose**, separating services will make it easier to manage.

### **App 1 (app1.py)**

```python
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("http://app2:5001/data")  # Calling App 2
    return f"Response from App 2: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### **App 2 (app2.py)**

```python
from flask import Flask

app = Flask(__name__)

@app.route('/data')
def data():
    return "Hello from App 2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

---

## **Step 3: Create Dockerfiles for Both Apps**

Each app will need its own `Dockerfile`.

### **Dockerfile for App 1**

Create `Dockerfile` in the **app1** folder:

```dockerfile
# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app1.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app1.py"]
```

### **Dockerfile for App 2**

Create `Dockerfile` in the **app2** folder:

```dockerfile
# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app2.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5001

# Run the application
CMD ["python", "app2.py"]
```

---

## **Step 4: Create a Requirements File**

Both apps need Flask and Requests. Create `requirements.txt` for both:

```txt
flask
requests
```

---

## **Step 5: Create a Docker Network**

Docker containers need to communicate, so create a custom network:

```sh
docker network create mynetwork
```

---

## **Step 6: Build and Run the Containers**

Navigate to each folder and build the images:

### **Build App 1:**

```sh
cd app1
docker build -t app1 .
```

### **Build App 2:**

```sh
cd ../app2
docker build -t app2 .
```

Now, run the containers and connect them to `mynetwork`:

### **Run App 2 first (backend service)**

```sh
docker run -d --name app2 --network mynetwork -p 5001:5001 app2
```

### **Run App 1 (frontend, calling App 2)**

```sh
docker run -d --name app1 --network mynetwork -p 5000:5000 app1
```

---

## **Step 7: Testing the Connection**

Now, access App 1 in your chrome/edge browser:

```
http://localhost:5000
```

It should return:

```
Response from App 2: Hello from App 2!
```

---

## **Step 8: Verify Networking**

Check if both containers are connected:

```sh
docker network inspect mynetwork
```

---

### **Key Networking Concepts Demonstrated**

✅ **Linking Containers:** Using `docker network` instead of `--link`  
✅ **Exposing Container Ports:** `EXPOSE` and `-p 5000:5000`, `-p 5001:5001`  
✅ **Routing Between Containers:** `requests.get("http://app2:5001/data")`

---

To push your Docker networking setup to **Docker Hub**, follow these steps:

---

## **Step 1: Log in to Docker Hub**

Ensure you're logged into Docker:

```sh
docker login
```

Enter your **Docker Hub username** and **password** when prompted.

---

## **Step 2: Create a Docker Hub Repository**

Go to [Docker Hub](https://hub.docker.com/) and **create two repositories**:

- `app1`
- `app2`  
  Both repositories will store the images for our Flask apps.

---

## **Step 3: Tag Docker Images**

Docker images need to be tagged correctly before pushing. The format is:

```sh
docker tag <local-image> <dockerhub-username>/<repo-name>:<tag>
```

### **Tag App 1:**

```sh
docker tag app1 <your-dockerhub-username>/app1:latest
```

### **Tag App 2:**

```sh
docker tag app2 <your-dockerhub-username>/app2:latest
```

Replace `<your-dockerhub-username>` with your actual **Docker Hub username**.

---

## **Step 4: Push Images to Docker Hub**

Now, push both images to Docker Hub:

### **Push App 1**

```sh
docker push <your-dockerhub-username>/app1:latest
```

### **Push App 2**

```sh
docker push <your-dockerhub-username>/app2:latest
```

---

## **Step 5: Run Containers from Docker Hub**

Anyone can now pull and run the images using:

### **Pull Images**

```sh
docker pull <your-dockerhub-username>/app1:latest
docker pull <your-dockerhub-username>/app2:latest
```

### **Run Containers on a Network**

```sh
docker network create mynetwork

docker run -d --name app2 --network mynetwork -p 5001:5001 <your-dockerhub-username>/app2:latest
docker run -d --name app1 --network mynetwork -p 5000:5000 <your-dockerhub-username>/app1:latest
```

Now, accessing `http://localhost:5000` will route requests from App 1 to App 2! 🎉

Would you like to **Docker Compose** this setup for easier deployment? 🚀
