[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to K8s**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/K8s/index.md)


# Launch an application using 

Step **1**: Launch a Linux Terminal (Either on [AWS](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/K8s/pages/K8s_L01_Installing_Prequisite.md) or [Local Virtual Machine](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/K8s/pages/K8s_L02_Setting_MicroK8s_using_on_AWS.md))

## Create a web application (using Flask)

**Step 2:** Create a directory `my-project` and navigate to the created directory.

```bash
mkdir my-project
cd my-project
```

**Step 3:** Create 3 files using `touch` - 

| File Name        | Description                           | 
| :--------------- | :----------------------------------- | 
| `app.py`           | An entry page for our application |
| `requirements.txt` | Define the required package to run our application |
| `dockerfile`       | Contains all the commands a user could call on the command line to assemble an image.|

Verify the created file

```bash
ls -l
```

**Output:**

```
total 0
-rw-r--r--. 1 ec2-user ec2-user 0 Aug 31 04:49 app.py
-rw-r--r--. 1 ec2-user ec2-user 0 Aug 31 04:49 dockerfile
-rw-r--r--. 1 ec2-user ec2-user 0 Aug 31 04:49 requirements.txt
```

**Step 4:** Navigate to each iles and write the associated code to define our application and other commands

> **You can find the entire code [here](https://github.com/xanderbilla/ExamPrep-AWS/tree/main/assets/CSE363/labs/Lab_03/my-project) for this lab**

**Step 4.1:** Navigate to `app.py` and edit the file using `nano` 

```py
from flask import Flask

app = Flask(__name__)

# __name__ is a special variable in Python that is used to determine whether the script is being run on its own or being imported from another module.

# create web oage to display Hello World!

@app.route('/') 
# This is a decorator that tells Flask what URL should trigger the function that follows it.
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__': # This is to ensure that the server only runs if the script is 
    # executed directly.
    app.run(host='0.0.0.0', port=5000)
```

**Step 4.2:** Save and Exit.

**Step 4.3:** Navigate to `requirements.txt` and edit the file using `nano`

```requirements
flask
```
## Create a `dockerfile`

**Step 4.3:** Navigate to `dockerfile` and edit the file using `nano`

```dockerfile
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the web server will listen on
EXPOSE 5000

ENV FLASK_ENV=production
# Set the command to run the web server
CMD ["python", "app.py"]
```
## Build and run `docker` image

Step **5**: To build an image using the created `dockerfile`

```bash
docker build -t my-app .
```

The docker image of our created application is created.

To Verify

```bash
docker images --filter reference=my-app
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

## Additional Notes

- If you're using AWS EC2 make sure to update your Security group inbound rule that allow Port 5000 to `0.0.0.0/0`

- Other useful docker commands that can be used are 

| Command          | Description                           | 
| :--------------- | :------------------------------------ |
| `docker run <IMAGE_NAME>`      | Create a docker container.
| `docker ps`      | Lists only the running containers.
| `docker ps -a`   | Lists all containers, including running, stopped, and exited ones |
| `docker rmi -f <IMAGE_ID>`     | Lists only the running containers.
| `docker rm <CONTAINER_ID`      | Lists only the running containers.

### You can perform this lab using the pre-written script

```bash
wget https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/resources/Lab_03.sh > /dev/null 2>&1
chmod +x Lab_03.sh
./Lab_03.sh
```

Output:

```
[✓] Create project directory
[✓] Create required files
[✓] Write code in app.py
[✓] Write requirements in requirements.txt
[✓] Write code in dockerfile
[✓] Build and run Docker image
```

# Author

[@xanderbilla](https://github.com/xanderbilla)
