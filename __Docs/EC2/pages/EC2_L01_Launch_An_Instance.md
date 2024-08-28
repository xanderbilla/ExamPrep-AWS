[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to EC2**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/EC2/index.md)

# Managing EC2 Using managment Console

## Create an EC2 instance

**Step 1:** Select a nearest region **>>** Go to AWS Services **>>** EC2

**Step 2:** A dashboard will appear shoing overview of EC2 instance. 

**Step 3:** Click on Instaces in the side panel / **Resources**

**Step 4:** An EC2 Instances pages will open from where we can manage and perform acions over instances,

**Step 5:** Click on **Launch Instance**. A new launch instance page will open

**Step 6:** Provide the following details - 

- Instance Name
- Operating System
- Architecture
- Instance type
- Create a key pair (use existing)
- Use default Network Setting/Security Group **(for now)**
- Configure the storage (according to your need)

For network setting (If custom VPC is created)

**Step 6.1:** Click on **Edit** in **Network Setting** section.

**Step 6.2:** Select the custom VPC and subnet.

**Step 6.3:** Enable auto assign public IP address  

**Step 6.4:** Select **Existing Security Group** >> select the created security group

To create a key pair click on Create a new key pair **>** Enter a new name for your key pair and chose the key type (PEM or RSA). And download in your local machine

**Step 7:** Click on **Launch Instance** 

(AWS will start creating an instance)

**Step 8:** Click on **View instance** 

<mark>Wait util the **2/2 checks passed** </mark>

In the Instance page you will able to see the following - 

- Inastace name
- Instance ID
- Instance type
- State
- Public IP Address
- Private IP Address
- Availability zone
etc.

**Step 9:** Once you click on **Instance ID** you will get an **Instance Summary** Page for that particular instance. Which has every detail of that instance.


**Step 10:** Click on **Connect** button

**Step 10:** We will see many options to connect with our instance. 

**Step 11:** Open and naviagte to the key pair where you have downloaded in your terminal. 

```bash
chmod 400 <KEY_PAIR_FILE>
```

Connect the EC@ using SSH and the key pair

```bash
ssh -i <KEY_PAIR> username@<INSTANCE_DNS/IP_ADDRESS>
```

