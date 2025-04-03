# Project:
Top News Aggregator Email

# Description:
This program extracts the top 5 headlines from various news sources (e.g. CNN, Forbes, etc) on a daily basis,
and aggregate them into a single email (with duplicates removed and replaced with unique headlines). The goal
is to bring recipients up-to-date on the latest news from multiple sources in a bite-sized manner.

# Installation:
1. **Navigate to the directory**: Go to the directory where you want to place the cloned repository (if you're not already there). Use the `cd` command to navigate to your preferred folder.
2. **Clone the repository**: git clone https://github.com/nickyw19/news-consolidator.git
3. **Other requirements needed**:
   - **Create API Keys**:
     - New York Times API Key: Create your API key using https://developer.nytimes.com/docs/articlesearch-product/1/overview
     - The Guardian API Key: Create your API key using https://open-platform.theguardian.com/documentation/
   - **Configure Email-sending Settings**:
     - Input the email addresses for recipient(s)) and sender in the `NewsConstructor.py` file .
     - For the sender’s email, you'll need to generate an app password via your email provider's security settings.
   - **Set Up Environment Variables:**
     - Open the `NewsAPI.py` and `NewsConstructor.py` files.
     - Use **Ctrl+F** (or Command+F) to search for `os.getenv` in both files and input your values in the appropriate places
4. **Run the project**: Open the files in an IDE or input `python main.py` into the terminal and hit ENTER

# Additional Setup (Optional)
Setup Cron (Time-based job scheduler) to run the program on a frequent basis using https://www.uptimia.com/learn/schedule-cron-jobs-in-python#:~:text=Schedule%20Python%20Scripts%20with%20Cron&text=Create%20a%20Python%20Script%3A%20First,crontab%20%2De%20in%20the%20terminal

# Data Description:
The data was queried from multiple news sources via 2 methods: APIs and Webscraping. The headline and the url
were extracted for each article and, along with the name of the source, stored in a dictionary.