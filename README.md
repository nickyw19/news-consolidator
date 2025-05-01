# Project:
News Aggregator Email

# Description:
This program extracts the top 5 headlines from various news sources (e.g. CNN, Forbes, etc) on a daily basis,
and aggregate them into a single email (with duplicates removed and replaced with unique headlines). The goal
is to bring recipients up-to-date on the latest news from multiple sources in a bite-sized manner.

# Installation:
1. **Requirements needed**:
   - New York Times API Key: Create your API key using https://developer.nytimes.com/docs/articlesearch-product/1/overview
   - The Guardian API Key: Create your API key using https://open-platform.theguardian.com/documentation/
   - Emails: Create Sender and Recipient emails that you would like the program to use (if they don't currently exist)
   - App password for Sender: Generate this via your email provider's security settings
   
2. **Running the program via Github Actions**:
   - Fork the repository: Click the `Fork` button on the top right of this repository
   - Add Secrets: Add your API keys and emails as Secrets in Github actions (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
   - Set scheduler: In `.github/workflows/daily-script.yml`, edit the cron expression in line 5 to set your preferred schedule (https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules) 
   - Auto-execute program: Github Actions will automatically run the program based on this scheduled time
   
3. **Running the program locally**
   - Navigate to the directory: Open the Terminal and go to the directory where you want to place the cloned repository
   - Clone the repository: In the terminal, input `git clone https://github.com/nickyw19/news-consolidator.git` and press ENTER
   - Install required packages: In the terminal, input `pip install -r requirements.txt` and press ENTER 
   - Create environment variables: Create a `.env` file in the project directory with the same keys & values used as Secrets 
   - Run the program: Input `python Main.py` into the terminal and press ENTER

# Data Description:
The data was queried from multiple news sources via 2 methods: APIs and Webscraping. The headline and the url
were extracted for each article and, along with the name of the source, stored in a dictionary.