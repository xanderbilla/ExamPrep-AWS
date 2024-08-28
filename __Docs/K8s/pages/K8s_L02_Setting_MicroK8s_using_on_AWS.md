[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to K8s**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/K8s/index.md)

# Setting MicroK8s using on AWS

## Setup a Virtual Machine

**Step 1:** Login to [**AWS Management Console**](https://aws.amazon.com/console/) >> Services >> EC2 >> **Launch Instance**

<mark>**You can also use your AWS Sandbox Environment**

**Step 2:**  Create a Virtual Machine using following configuration.

- Instance Name
- Application and OS Images: **Ubuntu**
- Instance Type: **t2.medium**
- Key Pair (use if exisitng)
- Network Setting: **Create [custom VPC](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/EC2/pages/EC2_L02_EC2_With_Custom_VPC.md) / Use default - It's upto you** 

**Step 3:** Leave the remaining to default and click on `Launch Instance`

(AWS will start creating an instance)

**Step 4:** Click on **View instance** 

<mark>Wait util the **2/2 checks passed** </mark>

**Step 5:** Once you click on **Instance ID** you will get an **Instance Summary** Page for that particular instance. Which has every detail of that instance.

![Instance Summary](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/K8s_L02_Step_5.png)


**Step 6:** Click on **Connect** button >> SSH Client.

![Connect](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/K8s_L02_Step_6.png)

**Step 7:** Open and naviagte to the key pair where you have downloaded in your PC terminal. 

```bash
chmod 400 <KEY_PAIR_FILE>
```

Connect the EC@ using SSH and the key pair

```bash
ssh -i <KEY_PAIR> username@<INSTANCE_DNS/IP_ADDRESS>
```

**Step 8:** Set up a password for the user using passwd command along with the username.

```bash
sudo passwd ubuntu
```

**Step 9:** Edit sshd_config file.

```bash
sudo nano /etc/ssh/sshd_config
```

Find the Line containing `#PasswordAuthentication yes` and omit `#` from that line

`PasswordAuthentication yes`

**(Optional)** If you want to set up `root` login, find `#PermitRootLogin prohibit-password` and omit `#` from that line. Also, change its value from `prohibit-password` to `yes`

`PermitRootLogin yes`

After this changes save file and exit.

**Step 10:** Restart SSH service

```bash
service ssh restart
```

## Install Docker & Kubernetes

**Step 11:** To install docker -

Remove existing installation.

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove -y $pkg; done
```

Add Docker's official GPG key:

```bash
sudo apt-get update -y
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Add the repository to Apt sources:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y
```

Install Docker

```bash
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Start and enable the Docker service:

```bash
sudo systemctl enable --now docker
```

Create a `hello-world` container

```bash
sudo docker run hello-world
```

**Step 12:** Install Kubernetes and MicroK8s

**Install kubectl**

Install GPG Keys/Certificates

```bash
sudo apt-get update
# apt-transport-https may be a dummy package; if so, you can skip that package
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg

# If the folder `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
# sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring

# This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list   # helps tools such as command-not-found to work correctly
```

Install `kubectl`

```bash
sudo apt-get update
sudo apt-get install -y kubectl
```

**Step 13:** Install MicroK8s

```bash
sudo snap install microk8s --classic --channel=1.31
```

Adding user to `microk8s` group so user can manage and interact with the Kubernetes cluster.

```bash
sudo usermod -a -G microk8s $USER
mkdir -p ~/.kube
chmod 0700 ~/.kube

su - $USER
```

**Step 14:** Start MicroK8s service and check the status.

```bash
sudo microk8s start 
microk8s status --wait-ready
```

**Step 15:** Enables the MicroK8s dashboard, a web-based user interface for managing Kubernetes clusters.

```bash
microk8s enable dashboard 
```

**Step 16:** Enables DNS within MicroK8s, allowing services to be accessed by their DNS names rather than IP addresses.

```bash
microk8s enable dns
```

**Step 17:** Enables a container registry within MicroK8s, providing a place to store and manage container images.

```bash
microk8s enable registry
```

**Step 18:** Enables Istio, a service mesh platform for managing and securing microservices.

```bash
sudo microk8s enable community
microk8s enable istio
```

**Step 19:** Lists information about the nodes (worker machines) in the MicroK8s cluster, including their status, IP addresses, and other details.

```bash
microk8s kubectl get nodes
```

**Descriptions for each line in the output of `microk8s kubectl get nodes`:**

- **NODE NAME:** The name of the node.
- **STATUS:** The current status of the node, such as `Ready` or `NotReady`.
- **ROLES:** The roles assigned to the node, such as `control-plane` or `worker`.
- **AGE:** The age of the node since it joined the cluster.
- **VERSION:** The version of Kubernetes running on the node.
- **INTERNAL-IP:** The internal IP address of the node within the cluster.
- **EXTERNAL-IP:** The external IP address of the node, if applicable.

### <mark>**You must complete step 1 to Step 19 before moving forward**</mark>

### Update Security Group & Open K8s dashboard

We need to **update Inbound Rules of Security Group and add Port 10443**.

![Security Group](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/K8s_L02_Step_21.png)

#### To run the dashboard run the following command and copy the token

```bash
sudo microk8s dashboard-proxy
```

Naviagte to **https://<PUBLIC_IP>:10443** (In my case it's [**https://3.10.142.53:10443**](https://3.10.142.53:10443)) in the browser and paste the token to open Kubernetes Dashbaoard 

<mark>If you're using Virtual Machine use localhost loopbakc i.e., **127.0.0.1** instead of **<PUBLIC_IP>**</mark>

### Additional Notes:**

- The specific output of `microk8s kubectl get nodes` will vary depending on the number and configuration of nodes in your cluster.
- The `microk8s dashboard-proxy` command typically runs in the background and can be accessed by opening a web browser and navigating to the specified URL.


