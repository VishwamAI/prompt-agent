import requests
import json
import os
import logging
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup

class DataCollectionAgent:
    def __init__(self, data_dir='data/', config_file='config/data_collection_config.json'):
        self.data_dir = data_dir
        self.config_file = config_file
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.load_config()
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename='data_collection.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.logger.error(f"Config file {self.config_file} not found.")
            self.config = {}

    def fetch_data_from_web(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching data from web: {e}")
            return None

    def parse_html(self, html_content, selectors):
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            data = {}
            for key, selector in selectors.items():
                element = soup.select_one(selector)
                data[key] = element.get_text(strip=True) if element else None
            return data
        except Exception as e:
            self.logger.error(f"Error parsing HTML content: {e}")
            return None

    def save_data(self, data, filename):
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w') as file:
            json.dump(data, file)
        self.logger.info(f"Data saved to {filepath}")

    def collect_data(self):
        for source in self.config.get('sources', []):
            if source['type'] == 'web':
                html_content = self.fetch_data_from_web(source['url'])
                if html_content:
                    data = self.parse_html(html_content, source.get('selectors', {}))
                    if data:
                        filename = f"{source['name']}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
                        self.save_data(data, filename)
            else:
                self.logger.error(f"Unknown source type: {source['type']}")
                continue

    def schedule_data_collection(self, interval_minutes=60):
        self.scheduler.add_job(self.collect_data, 'interval', minutes=interval_minutes)
        self.logger.info(f"Scheduled data collection every {interval_minutes} minutes")

    def auto_update(self):
        # Placeholder for auto-update logic
        self.logger.info("Auto-update functionality not yet implemented")

if __name__ == "__main__":
    agent = DataCollectionAgent()
    agent.schedule_data_collection()
    agent.collect_data()
