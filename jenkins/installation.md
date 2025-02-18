To install Jenkins in Docker, follow these steps:

### **Step 1: Install Docker**

Before setting up Jenkins in Docker, make sure Docker is installed on your machine. If it's not installed, follow these steps to install Docker:

1. **For Linux:**  
   Follow the installation guide on the [official Docker site](https://docs.docker.com/engine/install/).

2. **For Windows/Mac:**  
   Download Docker Desktop from [here](https://www.docker.com/products/docker-desktop) and follow the installation instructions.

### **Step 2: Pull the Jenkins Docker Image**

1. Open a terminal/command prompt.
2. Pull the official Jenkins image from Docker Hub using the following command:

```bash
docker pull jenkins/jenkins
```

This will pull the latest stable Jenkins image (`lts` stands for Long Term Support).

### **Step 3: Run Jenkins in a Docker Container**

1. Once the image is pulled, run the Jenkins container with the following command:

```bash
docker run --name jenkins -d -p 8080:8080 -p 50000:50000 jenkins/jenkins
```

- `--name jenkins`: Specifies the container name.
- `-d`: Runs the container in detached mode.
- `-p 8080:8080`: Exposes Jenkins on port 8080.
- `-p 50000:50000`: Exposes the port for Jenkins agents.

### **Step 4: Access Jenkins UI**

1. After the container starts, you can access Jenkins through your browser by navigating to:

```
http://localhost:8080
```

2. The first time you access Jenkins, it will ask for the **Unlock Jenkins** key.

### **Step 5: Retrieve the Unlock Key**

1. To retrieve the Jenkins unlock key, use the following command:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

2. Copy the key output from the terminal and paste it into the unlock screen in your browser.

### **Step 6: Set Up Jenkins**

1. Once unlocked, you'll be prompted to install suggested plugins or select specific plugins.
2. Follow the setup wizard to complete the installation and create your first admin user.

### **Step 8: To Stop and Remove Jenkins Container (If Needed)**

To stop and remove the Jenkins container, you can run:

```bash
docker stop jenkins
docker rm jenkins
```

This will stop and remove the Jenkins container from Docker.

---
