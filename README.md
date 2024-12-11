# 🏋️ Workout Tracker

## 🌟 Overview

The Workout Tracker is a Python application that utilizes the **Nutritionix API** to log your workouts and the **Sheety API** to store the data in a Google Sheet. Users can input their exercise details, and the app will calculate the duration and calories burned, then save the data for easy tracking.

## 🛠 Features
* **Exercise Logging:** Automatically calculates calories burned and duration based on user input.
* **API Integration:** Fetches exercise details using the Nutritionix API.
* **Data Storage:** Logs workouts in a Google Sheet via Sheety API.
* **Dynamic Date and Time Handling:** Automatically adds the current date and time to each workout entry.

## 📂 Project Structure


    .
    ├── main.py                 # Main Python script for tracking workouts
    ├── requirements.txt        # Project dependencies 
    ├── README.md               # Project documentation
## 🔧 Setup Guide

**Prerequisites**

* Python 3.x installed.
* API keys for Nutritionix and Sheety.
* A configured Google Sheet with the Sheety API.

**Installation**

1. Clone this repository:


    git clone https://github.com/matanohana433/workout-tracker.git
    cd workout-tracker
2. Create and activate a virtual environment (optional but recommended):

**Windows:**

    python -m venv venv
    venv\Scripts\activate
**macOS/Linux:**

    python3 -m venv venv
    source venv/bin/activate
3. Install dependencies:


    pip install -r requirements.txt
4. Set environment variables:

   * Create a .env file or set the variables manually:


    APP_ID=your_nutritionix_app_id
    API_KEY=your_nutritionix_api_key
    AUTH_TOKEN=your_sheety_auth_token
    SHEETY_API=your_sheety_project_id
## 🚀 Usage

1. **Run the Application:**


    python main.py
2. **Log an Exercise:**

* When prompted, enter your exercise (e.g., "ran 5km" or "biked for 30 minutes"):


      Tell me which exercise you did: ran 5km

* The application calculates calories burned and duration and saves the data to your Google Sheet.

3. **Check Your Google Sheet:**

* Verify the logged data, including:
    - Date
    - Time
    - Exercise name
    - Duration
    - Calories burned

## 🌟 Key Features

1. **Automated Logging:**
   * Automatically fetches exercise data and stores it in Google Sheets.
2. **Dynamic Date and Time:**
   * Adds the current date and time to each entry.
3. **Seamless Integration:**
   * Uses APIs for both data fetching and storage.

## 🚀 Future Enhancements

1. Add a user-friendly web or CLI interface.
2. Enable support for multiple users.
3. Include graphs and analytics for tracking trends.

## 📬 Contact

For questions or collaboration:

* **Email:** matanohana433@gmail.com
* **GitHub:** matanohana433