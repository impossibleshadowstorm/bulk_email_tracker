# Bulk Email Tracker

Bulk Email Tracker is a project that allows users to send emails to multiple recipients and track whether the emails have been opened. The project consists of a Django backend and a React frontend, both of which are containerized using Docker.

## Getting Started

To start the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/impossibleshadowstorm/bulk_email_tracker
   cd bulk-email-tracker
   ```

2. **Create a `.env` file:**
   - In both the `frontend` and `backend` directories, create a `.env` file.
   - Check for the required environment variables in the `env.sample` file and add your secrets to the `.env` file.

3. **Build and start the project:**
   ```bash
   docker-compose build
   docker-compose up
   ```

## Features

- Send emails to multiple users.
- Track email status (sent or opened) in the database.

## Database Tracking

- When an email is sent, its status is recorded as **sent** in the database.
- If a user opens the email, the status is updated to **opened**.

