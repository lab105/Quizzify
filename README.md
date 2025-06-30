# Quizzify

## Overview

This repository contains the web app described in the paper “To Solicit or Not to Solicit? Impact of AI Assistance Delivery Mechanisms on Decision-Making”. 

Using this experimental platform, we conducted a study with 232 subjects who were divided into three treatments: those receiving no AI assistance, those receiving AI assistance upon request ("solicited"), and those receiving automatic AI assistance ("unsolicited"). Subjects faced Cognitive Reflection Test (CRT) and mathematics questions while being subjected to intentionally misleading AI advice to gauge how different delivery mechanisms affected their decision-making process. 

Despite retaining many of the original features, we have modified the web app to ensure maximum customizability and facilitate the implementation of new experimental designs. 

![image](https://github.com/user-attachments/assets/0785c615-db25-4fca-82ee-51ff41d38e33)

## Platform Features

1. Question Set Customization: You can upload your own sets of questions tailored to your specific study needs. This flexibility supports a variety of quiz formats, including multiple-choice, true/false, and short-answer questions.
2. AI Assistance Integration: The platform allows for the integration of AI assistance, which can be configured to provide suggestions, explanations, and other forms of help to participants. 
3. Comprehensive Data Logging: The platform logs all relevant data points, including but not limited to:
   - Demographic Data: Information about the participants such as age, gender, educational background, etc.
   - Quiz Interactions: Every answer selected by the participant, along with timestamps of when each action was taken (e.g., "prompt", "continue", "start").
   - Timing Information: Detailed logs of the time spent on each question, which can be crucial for analyzing decision-making processes.
4. Post-Quiz Surveys: After completing the quiz, participants can be directed to complete surveys. These surveys can gather additional data on participants' experiences, perceptions of the AI assistance, and other relevant subjective measures.
5. Data Export and Analysis: You can easily export the collected data in various formats for further analysis. The platform ensures that data is well-organized and accessible, facilitating efficient and effective analysis.

## Technologies

- [Python](https://www.python.org/) - The heart of our backend logic
- [Django](https://www.djangoproject.com/) - A high-level Python web framework
- [Django REST framework](https://www.django-rest-framework.org/) - Powerful toolkit for building Web APIs
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) - For seamless containerization and orchestration
- [Nginx](https://www.nginx.com/) - High-performance web server and reverse proxy
- [SQLite](https://www.sqlite.org/) - Lightweight, serverless database engine
- [React](https://reactjs.org/) - For building dynamic user interfaces (in associated frontend projects)

## Setup

### Pre-requisites

Before you begin, ensure you have the following:

- A server or VM running Ubuntu 22.04 LTS
- Docker and Docker Compose installed
- A domain name pointing to your server's IP address
- Git for version control

### Recommended VM Configuration

For optimal performance, we recommend:

- RAM: 2GB (minimum)
- CPU: 1 vCPU (minimum)
- Storage: 20GB
- Open ports: 80 (HTTP), 443 (HTTPS), 22 (SSH)

### Getting Started: API Server

#### Clone the Repository

```bash
git clone https://github.com/lab105/HCI_Project.git
cd HCI_Project/hci_infra_codebase
```

#### Set Up SSL Certificates

Secure your server with SSL:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.example.com
```

After obtaining certificates, stop the global Nginx service:

```bash
sudo systemctl stop nginx
```

#### Configuration Updates

Customize the following files:

1. `backend/hci_backend/hci_backend/settings.py`:

   - Update `ALLOWED_HOSTS` with your domain
   - Modify `CORS_ORIGIN_WHITELIST` and `CSRF_TRUSTED_ORIGINS` with frontend domains

2. `backend/nginx/nginx.conf`:
   - Set `server_name` to your domain
   - Update SSL certificate paths

#### Build and Run the Application

Launch your HCI infrastructure:

```bash
docker-compose up -d --build
```

#### Accessing the Application

- Backend API: `https://yourdomain.example.com/api/`
- Admin interface: `https://yourdomain.example.com/admin/`

To stop the application:

```bash
docker-compose down
```

### Deploying the Frontend

For a smooth frontend deployment experience, we recommend using SaaS platforms like [Vercel](https://vercel.com/) or [Netlify](https://www.netlify.com/).

1. **Update API URL**: Remember to update the API URL in your frontend apps to point to your backend API server. You can find all the necessary environment variables in the `.env` file of each frontend app folder. If you're deploying through Vercel or Netlify, you can add these environment variables in their respective platforms.

2. **Secure Headers**: Don't forget to update the `vercel.json` or `netlify.toml` file to set up secure headers in the routing rules. Replace the sample domain name with the valid domain name mapped to your server.
