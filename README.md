# 🎟️ BookMySeat – Serverless Seat Booking App

A modern **serverless seat booking system** powered by **AWS Lambda**, **API Gateway**, and **DynamoDB**.  
It automatically sends **confirmation emails** to both the user and admin upon successful booking.  

---

## 🧠 Overview

BookMySeat allows users to book seats online easily.  
Once a user submits the form, the data is stored in **DynamoDB**, and both the **user** and **admin** receive a confirmation email.  

### ✨ Key Features
- ✅ Serverless architecture (no servers to manage)
- 💾 Stores booking info in **DynamoDB**
- 📧 Sends confirmation to **user** and **admin**
- 🔒 Secure credentials via **Lambda environment variables**
- 🌍 CORS enabled for public frontend access
- 🎨 Simple & responsive HTML/CSS frontend

---

## 🏗️ Architecture

[Frontend HTML Form]
│
▼
[API Gateway Endpoint] ---> [AWS Lambda Function] ---> [DynamoDB Table]
│
├──> Send Email to User
└──> Send Email to Admin


---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | AWS Lambda (Python 3.9) |
| **Database** | DynamoDB |
| **API** | API Gateway |
| **Email Service** | SMTP (Gmail App Password) |
| **Hosting** | S3 / Netlify / GitHub Pages |

---

## 🧩 Prerequisites

Before you begin, ensure you have:
- ✅ An **AWS Account**
- ✅ **IAM Role** with Lambda + DynamoDB permissions
- ✅ **Python 3.9+** installed
- ✅ A **Gmail App Password** (not normal password)

---

## 🚀 Setup Instructions

## 🐍 AWS Lambda Setup

1. Go to **AWS Console → Lambda → Create Function**
2. Select:
   - **Author from Scratch**
   - Name: `BookMySeatFunction`
   - Runtime: **Python 3.9**
3. Create / Select an **IAM Role** and attach:
   - `AmazonDynamoDBFullAccess`
   - `AmazonSESFullAccess` (or allow SMTP externally)
4. After creation, open the function and go to:
   **Configuration → Environment Variables**
5. Add the following keys:

| Key | Description |
|-----|-------------|
| `ADMIN_EMAIL` | Email to receive booking alerts |
| `SMTP_USER` | Gmail address used for sending emails |
| `SMTP_PASSWORD` | Gmail **App Password** (NOT regular password) |

6. Upload your Lambda function code file and **Save**.
7. Set **Handler Name**: `lambda_function.lambda_handler`

---

## 🌐 API Gateway Setup

1. Open **API Gateway** from AWS Console.
2. Click **Create API**
3. Choose: **HTTP API** (recommended)
4. Name it: `BookMySeatAPI`
5. Click **Next**
6. Add Integration:
   - **Integration Type:** Lambda
   - Select: `BookMySeatFunction`
7. Create a Route:

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/book` | Submits booking form data |

8. Deploy your API to a Stage:
   - Stage Name: `dev`

9. Copy the **Invoke URL** generated:
---
👩‍🏫 **Guided and Supported by [Trupti Mane Ma’am](https://github.com/iamtruptimane)**  
---


Big Thanks to [Piyush Dalvi](https://github.com/dalvipiyush07) for valuable contributions, testing, and setup assistance throughout this project. 🚀

👨‍💻 **Author:**  
**Shivam Garud**  
🧠 *DevOps & Cloud Enthusiast*  
💼 *Automating deployments, one pipeline at a time!*  
🌐 [GitHub Profile](https://github.com/Shivamgarud8)
🌐 [Medium blog](https://medium.com/@shivam.garud2011)
