# Interest Rate Scraper for ICICI Bank

This Scrapy spider scrapes interest rate information from ICICI Bank's website and stores it in a MongoDB database.

## Prerequisites

- Python 3.x
- Scrapy
- pymongo

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/rajatgoel179/icici-interest-scraper.git
   cd icici-interest-scraper
   
## Usage
1. Modify the ICICISpider class in the spiders/icici_spider.py file to adjust the URLs and parsing logic if needed.

2.Run the scraper using the following command:
scrapy runspider spiders/icici_spider.py

3. The script will start crawling the ICICI Bank website, extract interest rate data, and store it in a MongoDB database.

## MongoDB Configuration
Ensure you have MongoDB installed and running. Configure the MongoDB connection in the insert_to_mongodb method of the ICICISpider class.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

