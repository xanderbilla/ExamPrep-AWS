[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to K8s**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/K8s/index.md)

# Creating a service and deploying using docker

Following the **[Lab 03](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/K8s/pages/K8s_L03_Launch_An_Application_Using_Container.md)** we are going to create a service and attach it to our application

- It will be an update in our application

### Prerequisite 

The updated folder hierarchy will look like - 

```
my-project/
├── app.py
├── dockerfile
├── requirements.txt
└── template
    └── login.html
```

**Points to remember**

- There will be change in `app.py` only becauyse it contains the backend and we are adding a new serviceof whihc our application is unaware of.

### Update the directory

Navigate inside your working directory (`my-project` in my case)

```bash
mkdir template
touch template/login.html
```

### Create/Edit a login page

Create a login page or find the entire code [here](https://github.com/xanderbilla/ExamPrep-AWS/tree/main/assets/CSE363labs/Lab_04/my-project/template)

```bash
nano template/login.html
```

### Create/Edit backend (`app.py`)

Write your logic or find the entire code [here](https://github.com/xanderbilla/ExamPrep-AWS/tree/main/assets/CSE363labs/Lab_04/my-project)

```bash
nano app.py
```

### Re-build and run `dockerfile`

To build an image using the created `dockerfile`

```bash
docker build -t my-app:v2 .
```

>To avoid the naming conflict either delete the existing image or tag that image with version (used in this scenario)

The docker image of our created application is created.

To Verify

```bash
docker images --filter reference=my-app:v2
```

**Output:**

```
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
my-app        latest    0cf333799ced   2 seconds ago   136MB
```

**Step 6:** Create a docker container using `my-app` image

```bash
docker run -p 5000:5000 --name production my-app
```

The container is running at port `5000`.

To Verify

```bash
docker ps -a
```

**Output:**

```
CONTAINER ID   IMAGE         COMMAND           CREATED              STATUS                          PORTS      NAMES
c5ed7ca66713   my-app        "-p 5000:80"      2 minutes ago        Created                         5000/tcp   prod
```

**Step 7:** Open your local web browser and open the following accordingly - 

| Command          | Description                           | 
| :--------------- | :------------------------------------ |
| Local Virtual Machine | [`http://127.0.0.1:5000`](http://127.0.0.1:5000) or [`http://localhost:5000`](http://localhost:5000) or `http://<YOUR_VM_IP_ADDRESS>:5000` |
| AWS EC2         | `http://<PUBLIC_IP_ADDRESS>:5000` |

![Output](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/K8s_L03_Step_7.png)


# You can perform this lab using the pre-written script

```bash
wget https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/resources/Lab_04.sh > /dev/null 2>&1
chmod +x Lab_04.sh
./Lab_04.sh
```

Output:

```
[OK] Create project directory
[OK] Create required files
[OK] Write code in app.py
[OK] Write requirements in requirements.txt
[OK] Write code in dockerfile
[OK] Build and run Docker image
```

# Additional Notes

- If you're using AWS EC2 make sure to update your Security group inbound rule that allow Port 5000 to `0.0.0.0/0`

- Other useful docker commands that can be used are 

| Command          | Description                           | 
| :--------------- | :------------------------------------ |
| `docker run <IMAGE_NAME>`      | Create a docker container.
| `docker ps`      | Lists only the running containers.
| `docker ps -a`   | Lists all containers, including running, stopped, and exited ones |
| `docker stop <CONTAINER_ID>`   | Stop the running docker container |
| `docker rm <CONTAINER_ID`      | Lists only the running containers.
| `docker rmi -f <IMAGE_ID>`     | Lists only the running containers.

# Author

[@xanderbilla](https://github.com/xanderbilla)
