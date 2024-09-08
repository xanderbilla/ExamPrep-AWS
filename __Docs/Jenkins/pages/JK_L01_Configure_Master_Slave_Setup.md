[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to K8s**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/Jenkins/Index.md)

# Configure a Master-Slave setup over EC2 using Jenkins

### [Create EC2 Instances](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/EC2/pages/EC2_L01_Launch_An_Instance.md) (2 Instances named `master` and `slave`)

> You can also create an EC2 in a private subnet (must be in in the same VPC)

### Launch and connect the master EC2 Instance with your host-terminal (for example - powershell/CMD)

## Install and Configure Jenkins

#### Configuring Jenkins

**Step 1:** Open the public IP address with port 8080 - [**http://<YOUR_PUBLIC_IP_ADDRESS>:8080/**]()

> <mark>***If you are working using jenkins on your local PC use http://localhost:8080***

**Step 2:**  Unlock Jenkins by using the key. Get the password from `/var/lib/jenkins/secrets/initialAdminPassword` >> Click on Continue

![P1_STEP_20_IMG](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/P1_STEP_20_IMG.png)

**Step 3:** Install Suggesed Plusgins. The plugins will start installing automtically.

![P1_STEP_21_IMG](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/P1_STEP_21_IMG.png)

**Step 4:** Create User and Click on **Save and Continue**

![P1_STEP_22_IMG](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/P1_STEP_22_IMG.png)

**Step 5:** Configure Jenkins URL (used to access dashboard) >> Click **Save and Finish**

![P1_STEP_23.1_IMG](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/P1_STEP_23.1_IMG.png)

Finally Click on **Start Using Jenkins**

![P1_STEP_23.2_IMG](https://xanderbilla.s3.ap-south-1.amazonaws.com/Semester_V/__assets/P1_STEP_23.2_IMG.png)

**Step 6:** Go to Dashboard >> Manage Jenkins >> Nodes

**Step 7:** Click on **New Node** to create a node.

Enter the Node name and select Permanent Agent as a Type and click on Create.

**Step 8:** A new configuration page will open -

- Write a description (optional)
- Number of executors: 1
- Remote root directory: `/home/ubuntu` (If your slave noide is Ubuntu)
- Create a label
- For launch method: Select **Launch Agent Via SSH**
    - Host: Private IP Address of Slave Instance
    - Credentials: Select an existing credential / **Add >> Jenkins**
    - Host Key Verification Strategy: Manually trusted key Verification strategy

Click on **Save**

To Verify whether our slave is sucessfully configured. Go to **Dashboard >> Manage Jenkins >> Nodes >> Select the added node >> Log**. 

Click on log you will see a message that say `Agent successfully connected and online`

## Test the configuration

Now it's time to test our slave instance using a pipeline.

We will try to access and print some information using on Slave Instance using Jenkins which is running on Master Node.

**Step 9:** Go to the dashboard and Click on **New Item**.

Enter a Project name and select freestyle Project and click on Create.

**Step 10:** In the configuration page go to **Build Steps** Section and select `Execute Shell`

Enter the following command and hit **Apply** and then **Save**

```bash
public_ip=$(curl -s http://ifconfig.me)
hostname=$(hostname)
echo "Hosted on: $hostname"
echo "Public IP: $public_ip"
```

>This will print the Hostname and the Public IP Address of the machine.

**Step 11:** Go TO dashboard select the project and Click on **Build Now** >> Select a Build >> Click on **Console Output**

Output:

```
Started by user admin
Running as SYSTEM
Building remotely on jk-node-1 (jenkins-slave) in workspace /home/ubuntu/workspace/test-node
[test-node] $ /bin/sh -xe /tmp/jenkins8818104534851505157.sh
Hostname: ip-172-31-47-131
Public IP: 54.162.182.65
Finished: SUCCESS
```


# Author

[@xanderbilla](https://github.com/xanderbilla)
