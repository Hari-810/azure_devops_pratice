### **Bridge Network (Default in Docker)**

The **bridge network** is the default networking mode in Docker when you run a container without specifying a network. It allows containers to communicate with each other internally while also enabling external access through **port mapping** (`-p` option).

#### **Key Features:**

- Containers within the same bridge network **can communicate** using container names.
- External access is possible using **port mapping** (e.g., `-p 5000:5000`).
- It acts as a **virtual router**, providing network isolation from the host system.

#### **Use Case:**

- Best for **standalone applications** like web servers, APIs, and database containers that need controlled external access.
- Ideal for local development and testing environments.

#### **Example Commands:**

1. **Check existing networks:**
   ```sh
   docker network ls
   ```
2. **Inspect the bridge network:**
   ```sh
   docker network inspect bridge
   ```
3. **Run a container on the default bridge network:**
   ```sh
   docker run -d -p 5000:5000 --name my_app_container my_app_image
   ```
4. **Connect multiple containers on the bridge network:**
   ```sh
   docker network create my_bridge
   docker run -d --network my_bridge --name app1 my_app_image
   docker run -d --network my_bridge --name app2 my_app_image
   ```
