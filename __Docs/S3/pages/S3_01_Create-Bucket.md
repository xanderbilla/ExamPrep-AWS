[**Table of Contents**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/README.md) | [**Back to S3**](https://github.com/xanderbilla/ExamPrep-AWS/blob/main/__Docs/S3/Index.md)

## Managing S3 Using managment Console

### Create a bucket

**Step 1:** Go to AWS Services **>>** S3

**Step 2:** Choose a bucket name (must be unique throughout the AWS)

**Step 3:** Choose AWS Region

(Leave all the other setting to default - will play later)

**Step 4:** Click on Create Bucket

**Once the bucket is created we can see following information of a bucket in bucket list -** 

* **Bucket Name**
* **AWS Region**
* **Who can/can't Access**
* **Creation Date**

Once we get in bucket we can manage the bucket from there like properties, access points etc.

### Upload a file

**Step 5:** Upload a file (keeping all the option in default)

**Once the file is uploaded we can have multiple option to do with that file such as**

* **`Copy`**
* **`Move`**
* **`Rename`**
* **`Change to Public Access`**
* **`Edit Metadata`, etc**

## S3 using CLI

To interact with Amazon S3 using the Command Line Interface (CLI), follow these steps:

**Step 1:** Open your terminal or command prompt.

**Step 2:** Install the AWS CLI if you haven't already. You can find installation instructions in the AWS documentation.

**Step 3:** Configure the AWS CLI with your AWS credentials. You can use the `aws configure` command to set your access key, secret access key, default region, and output format.

**Step 4:** Once the AWS CLI is configured, you can start using S3 commands. 

```bash
aws s3 <Command> [<Arg> ...]
```

| Commands    | Description |
| -------------- | :---------  |
| `cp <SRC> <DST>`        | Copies a local file or S3 object to another location locally or in S3. |
| `ls`        | List S3 objects |
| `mb <BUCKET_NAME>`        | Creates an S3 bucket |
| `mv <SRC> <DST>`        | Moves a local file or S3 object to another location locally or in S3 |
| `presign <KEY>`   | Generate a pre-signed URL for an Amazon S3 object. This allows anyone who receives the pre-signed URL to retrieve the S3 object with an HTTP GET request.  |
| `rb  <BUCKET_NAME>`        | Deletes an empty S3 bucket. A bucket must be completely empty of objects and versioned objects before it can be deleted. However, the `--force` parameter can be used to delete the non-versioned objects in the bucket before the bucket is deleted.|
| `rm <KEY>`        | Deletes an S3 object. |
| `sync <SRC> <DST>`      | Syncs directories and S3 prefixes. Recursively copies new and updated files from the source directory to the destination. |
| `website`   | Set the website configuration for a bucket. |


We can use flags along with commands like -


| Flags      | Description |
| ---------- | :---------  |
| `--region` | Specify a specific region  |
| `--output` | Output format such as - `json`, `txt` etc. |

**and many more...**

### Examples

##### Create a bucket


```bash
aws s3 mb s3://mybucket
```

##### Copy a file


```bash
aws s3 cp test.txt s3://my-bucket/file-01.txt
```

##### Move a file


```bash
aws s3 mv s3://my-bucket/file-01.txt s3://my-bucket/foofoo/file-01.txt
```

##### Make file accessible for a interval of time


```bash
aws s3 presign s3://DOC-EXAMPLE-BUCKET/test2.txt --expires-in 604800
```



## Reference

[AWS | Official Docs](https://docs.aws.amazon.com/pt_br/cli/latest/reference/)