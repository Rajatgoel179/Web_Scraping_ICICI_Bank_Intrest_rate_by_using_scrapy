import scrapy
import pymongo
from scrapy.crawler import CrawlerProcess

class ICICISpider(scrapy.Spider):
    name = "bank"
    start_urls = ['https://www.icicibank.com/interest-rates?ITM=nli_cms_intrest_rate_footer_link#interest-rates']

    def parse(self, response):
        # Process the starting URL table
        self.parse_table(response)

        # Find and follow the links you're interested in
        links_to_follow = response.xpath('//li/a[@class="ic-more"]')
        for link in links_to_follow:
            link_text = link.xpath('normalize-space(.)').get()
            link_url = link.attrib['href']
            yield response.follow(link_url, self.parse_table, meta={'link_text': link_text})

    def parse_table(self, response):
        link_text = response.meta.get('link_text', 'unknown')
        tables = response.xpath('//table')

        for idx, table in enumerate(tables):
            rows = table.xpath('.//tr')
            table_data = []

            for row in rows:
                cols = row.xpath('.//th | .//td')
                row_data = [col.xpath('normalize-space(.)').get() for col in cols]
                table_data.append(row_data)

            # Remove rows with no data
            table_data = [row for row in table_data if any(field.strip() for field in row)]

            # Insert data into MongoDB
            self.insert_to_mongodb(link_text, idx+1, table_data)

            print(f"Data from {link_text} Table {idx+1} inserted into MongoDB")

    def insert_to_mongodb(self, link_text, table_idx, table_data):
        # MongoDB connection parameters
        client = pymongo.MongoClient("mongodb+srv://rajatgoel179:rajat123@cluster0.datihvo.mongodb.net/")
        db = client["icici_bank_data"]
        collection_name = f"{link_text}_table_{table_idx}"
        collection = db[collection_name]

        # Insert data into the collection
        for row in table_data:
            data = {'columns': row}
            collection.insert_one(data)

        # Close the MongoDB connection
        client.close()

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(ICICISpider)
    process.start()