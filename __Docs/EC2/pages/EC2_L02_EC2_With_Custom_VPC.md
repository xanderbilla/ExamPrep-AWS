[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to EC2**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/EC2/index.md)

# EC2 with custom VPC



## Create VPC

**Step 1:** Select a nearest region **>>** Go to AWS Services **>>** VPC

**Step 2:** A dashboard will appear showing overview of VPC. 

[Image]

**Step 3:** Click on **Create VPC** >> **VPC Only**

**Step 4:** Provide the following details

- VPC Name
- CIDR Address (e.g: `11.0.0.0/16`)
- Tags (Optional)

**Step 5:** Click on **Create VPC** 

(You'll be able to see the details of created VPC)

Click on **Your VPC** in left pane. In the VPC page you will able to see the following - 

- VPC name
- VPC ID
- State
- CIDR v4
- CIDR v6
- associated RTB
etc.

## Create Subnets

**Step 6:** In the left navigation pane click on Subnets >> **Click on create subnet**.

[Image]

**Step 7:** Select the VPC in which we want to create a Subnet.

**Step 8:** Provide the following details -

- Subnet name
- Subnet CIDR address
- Availability zone

**Step 8:** Click on create subnet


## Create an Internet Gateway

**Step 9:** In the left navigation pane click on Internet Gateway >> **Click on create Internet Gateway**.

[Image]

**Step 10:** Provide the Internet Gateway name

**Step 11:** Click on create Internet Gateway

The created intenet gateway details page will open.

**Step 12:** Click on **Actions** >> **Attach to VPC** >> Select the VPC in which we want to attach

## Create Route table

**Step 13:** In the left navigation pane click on Route Table >> **Click on create Route Table**.

[Image]

**Step 14:** Provide the Route Table name and the VPC in whoch we want to associate with

**Step 15:** Click on create Route Table

The created Route table details page will open.

**Step 16:** In the **Routes** tab (bottom of page) >> **Edit Routes**

**Step 17:** Route page will open. Click on Add routes. Choose the `0.0.0.0/0` as destination and choose the created IGW (in step 11) as target.

**Step 18:** Save changes. 

**Step 19:** In the **Subnet Association** tab (bottom of page) >> **Edit Subnet Association** >> Select the subnet which we want to associate with that route table and save the changes.

**Repeat the step 13 to 19 to create Private Route table (skipping the step 17 and 18)**

## Create NAT Gateway

**Step 20:** In the left navigation pane click on NAT Gateway >> **Click on create NAT Gateway**.

[Image]

**Step 21:** Provide the following details - 

- NAT Gateway name
- Subnet in which to create the NAT gateway (must be public)
- Connectivity type (must be public)
- Allocate an Elastic IP Address (use if exisiting)

**Step 22:** Click on create NAT Gateway

**Step 23:** Open Route Table page >> Select the private route table

**Step 24:** Route page will open. Click on Add routes. Choose the `0.0.0.0/0` as destination and choose the created NAT Gateway as target.

**Step 25:** Save changes. 

## Create a custom Security Group

In the left side panel of VPC page. Go to Security > Security Group

**Step 1:** Click on create Security Group

**Step 2:** Provide the followinf information -

- Security Group name
- Description (optional)
- VPC
- Add Inbound/Outbound Rules

[Image]

**Step 3:** Click on create security group


## [Create an EC2 instance using the above Custom VPC](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/EC2/pages/EC2_L01_Launch_An_Instance.md)

Create two EC2 instances as following


| Instance    | Subnet  |
| :---------: | :------ |
| Instance-01 | Public  |
| Instance-02 | Private |

Try Connect your private EC2 using `Instance-01`

**To store the key pairs use S3**