from requests_html import HTMLSession

def scrape_dynamic_page(url):
    """
    Scrapes a dynamic web page using requests_html, demonstrating its ability
    to render JavaScript content. This capability is crucial for modern web
    scraping, as many websites load content dynamically after the initial HTML
    is fetched.
    """
    session = HTMLSession()
    print(f"Attempting to fetch and render: {url}")
    try:
        r = session.get(url)
        # The article discusses 'Scrapling' as a modern library for handling
        # complex web scraping challenges, including dynamic content.
        # requests_html, used here as a stand-in, demonstrates this by rendering
        # JavaScript, which traditional scrapers (like BeautifulSoup alone) miss.
        r.html.render(sleep=1, scrolldown=0) # Render JavaScript, wait a bit for content to load
        print("Page rendered successfully.")

        # Extract data after JavaScript has executed and content is available
        title_element = r.html.find('title', first=True)
        title = title_element.text if title_element else 'No Title'
        quotes = r.html.find('.quote')

        print(f"\n--- Page Title: {title} ---")
        print(f"Found {len(quotes)} quotes:")
        for i, quote in enumerate(quotes[:5]): # Limit to first 5 for brevity
            text_element = quote.find('.text', first=True)
            author_element = quote.find('.author', first=True)
            tags = [tag.text for tag in quote.find('.tag')]
            
            text = text_element.text if text_element else 'N/A'
            author = author_element.text if author_element else 'N/A'

            print(f"  Quote {i+1}:")
            print(f"    Text: {text}")
            print(f"    Author: {author}")
            print(f"    Tags: {', '.join(tags)}")
            print("-" * 20)
        
        if not quotes:
            print("No quotes found. This might indicate an issue with rendering or selectors.")

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    # This URL (quotes.toscrape.com/js/) is specifically designed to load
    # quotes via JavaScript, making it an ideal target to demonstrate the
    # necessity and capability of modern, JS-rendering scrapers.
    target_url = "http://quotes.toscrape.com/js/"
    scrape_dynamic_page(target_url)
