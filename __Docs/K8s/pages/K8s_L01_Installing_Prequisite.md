[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to K8s**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/K8s/index.md)

# Setup a Virtual Machine

**Step 1:** Download & install a [**VMWare Workstation**](https://blogs.vmware.com/workstation/2024/05/vmware-workstation-pro-now-available-free-for-personal-use.html)

**Step 2:**  Download [**Ubuntu 22.04**](https://releases.ubuntu.com/jammy/) (ISO File) or [**Ubuntu 20.04**](https://releases.ubuntu.com/focal/).

**Step 3:** Create a Virtual Machine using above ISO File with following configuration (min requirement):

- **CPU**: 2 Core
- **Memory**: 2 GB
- **Storage**: 30 GB

**Step 4:** Install the Ubuntu on Virtual Machine.

## Install Docker & Kubernetes

**Step 5:** Once Installed. Launch a terminal in Linux and install Docker and Kubernetes. To install docker -

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

**Step 6:** Install Kubernetes and MicroK8s

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

**Step 7:** Install MicroK8s

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

**Step 8:** Allow the following ports in all every node including master node -

`19001`, `16443`, `10250`, `10255`, `25000`, `12379`, `10257`, `10259`, `10248` to `10256`, `4789`, `2380`, `1338`

```bash
sudo iptables -A INPUT -p tcp --dport 19001 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 16443 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 10250 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 10255 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 25000 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 12379 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 10257 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 10259 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 10248:10256 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 4789 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 2380 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 1338 -j ACCEPT
```

To verify the allowed ports - 

```bash
sudo iptables -L -n | grep "ACCEPT"
```

**Step 9:** Start MicroK8s service and check the status.

```bash
sudo microk8s start 
microk8s status --wait-ready
```

**Step 10:** Enables the MicroK8s dashboard, a web-based user interface for managing Kubernetes clusters.

```bash
microk8s enable dashboard 
```

**Step 11:** Enables DNS within MicroK8s, allowing services to be accessed by their DNS names rather than IP addresses.

```bash
microk8s enable dns
```

**Step 12:** Enables a container registry within MicroK8s, providing a place to store and manage container images.

```bash
microk8s enable registry
```

**Step 13:** Enables Istio, a service mesh platform for managing and securing microservices.

```bash
sudo microk8s enable community
microk8s enable istio
```

**Step 14:** Lists information about the nodes (worker machines) in the MicroK8s cluster, including their status, IP addresses, and other details.

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

### <mark>**You must been complete step 1 to Step 14 before moving forward**</mark>

**Step 15:** Go to <mark>**Master Node**</mark> and add the worker node. To add a worker node generate a token

```bash
mictok8s add-node
```

**Step 16:** Go to <mark>**Worker Node**</mark> and run the command that is generated in output

```bash
microk8s join <MASTER_NODE_IP>:25000/<TOKEN>
```

- *Make sure to run the `microk8s join once at a time and one node at a time and do not run it simultaneously on multiple node*

- *To join the multiple worker nodes in a cluster, the command `mictok8s add-node` should be run on the worker node one by one, once a node join the cluster.*

## Verification and installing K8s services

To verify the nodes in a cluster. Go to master node and run -

```bash
microk8s kubectl get nodes
```

Install the services. To do so - 

```bash
microk8s enable metallb helm3 prometheus rback
```

- **Rback** is the role-based access control plugin that is used to provide the access to the users. It is used to provide the access to the users based on the roles.

- **Helm3** is the package manager for the Kubernetes. It is used to install the packages on the Kubernetes.

- **Metallb** is the load balancer for the Kubernetes. It is used to provide the load balancing to the Kubernetes.

- **Prometheus** is the monitoring tool for the Kubernetes. It is used to monitor the Kubernetes.


Verify all the services by running -

```bash
microk8s kubectl get svc --all-namespaces
```

#### To run the dashboard run the following command and copy the token

```bash
sudo microk8s dashboard-proxy
```

Naviagte to [https://127.0.0.1:10443](https://127.0.0.1:10443) in the browser and paste the token to open Kubernetes Dashbaoard 


## Additional Notes:**

- The specific output of `microk8s kubectl get nodes` will vary depending on the number and configuration of nodes in your cluster.
- The `microk8s dashboard-proxy` command typically runs in the background and can be accessed by opening a web browser and navigating to the specified URL.

### You can perform this lab using the pre-written script

```bash
wget https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/resources/Lab_01.sh > /dev/null 2>&1
chmod +x Lab_01.sh
./Lab_01.sh
```

Output:

```
[✓]  Remove old Docker packages
[✓]  Add Docker GPG key
[✓]  Add Docker repository
[✓]  Install Docker
[✓]  Start and enable Docker
[✓]  Install Kubernetes tools
[✓]  Install MicroK8s
[✓]  Allow required ports in the firewall
[✓]  Verify firewall rules
[✓]  Configure MicroK8s


Setup Completed!
```

# Author

[@xanderbilla](https://github.com/xanderbilla)