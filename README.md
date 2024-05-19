# BeyondChats Python Gen-AI Developer Assignment

## Overview
This repository contains the Python script for the BeyondChats assignment. The task was to fetch data from a paginated API, identify response-source pairs, and return citations in a specified format. The project includes a Django-based web interface for user interaction.

## Features
- Fetches data from a paginated API.
- Analyzes the response and sources to identify citations.
- Returns citations in the specified format.
- User-friendly web interface using Django.

## Requirements
- Python
- Django
- `requests` library

## Usage
Script Usage
- The script will fetch data from the specified API, process the responses and sources, and output the citations.
  
# API Endpoint
The API endpoint used: https://devapi.beyondchats.com/api/get_message_with_sources
The script handles pagination and processes each page of results.

## Setup
### Cloning the Repository
First, clone the repository from GitHub and navigate into the project directory using these commands:

# 1. clone Project
git clone https://github.com/yerram-karthik/beyondchats.git
cd beyondchats

# 2. Apply Migrations
   Apply the initial migrations to set up the database:
   
   'python manage.py migrate'

# 3.Running the Django Server
  Start the Django development server:
  
  'python manage.py runserver'

# 4.Access the Web Interface
  Open your web browser and navigate to:
  
  'http://127.0.0.1:8000/'

## OUTPUT
![image](https://github.com/yerram-karthik/beyondchats/assets/136573431/e56e3c1a-2b1f-4813-99bb-4a6a7455df6e)

https://github.com/yerram-karthik/beyondchats/assets/136573431/67e9d04d-2b1f-4a56-830e-05008d63b2ec


 






