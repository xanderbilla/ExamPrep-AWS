[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to EC2**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/K8s/Index.md)

## Setup a Virtual Machine

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

**Step 8:** Checks the status of MicroK8s.

```bash
microk8s status --wait-ready
```

**Step 9:** Enables the MicroK8s dashboard, a web-based user interface for managing Kubernetes clusters.

```bash
microk8s enable dashboard
```

**Step 10:** Enables DNS within MicroK8s, allowing services to be accessed by their DNS names rather than IP addresses.

```bash
microk8s enable dns
```

**Step 11:** Enables a container registry within MicroK8s, providing a place to store and manage container images.

```bash
microk8s enable registry
```

**Step 12:** Enables Istio, a service mesh platform for managing and securing microservices.

```bash
sudo microk8s enable community
microk8s enable istio
```

**Step 13:** Lists information about the nodes (worker machines) in the MicroK8s cluster, including their status, IP addresses, and other details.

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

**Step 14:** Starts the MicroK8s dashboard proxy, which allows access to the dashboard from outside the cluster.

```bash
sudo microk8s dashboard-proxy
```

### Additional Notes:**

- The specific output of `microk8s kubectl get nodes` will vary depending on the number and configuration of nodes in your cluster.
- The `microk8s dashboard-proxy` command typically runs in the background and can be accessed by opening a web browser and navigating to the specified URL.


