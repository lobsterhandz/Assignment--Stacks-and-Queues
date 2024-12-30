class BrowsingHistory:
    def __init__(self):
        # Initialize an empty stack to store browsing history
        self.history = []

    # Add a new page to the stack
    def add_page(self, url):
        if not isinstance(url, str) or not url.strip():
            raise ValueError("URL must be a non-empty string.")
        self.history.append(url)
        print(f"Page added: {url}")

    # Remove the last visited page from the stack
    def remove_page(self):
        if not self.is_empty():
            removed_page = self.history.pop()
            print(f"Page removed: {removed_page}")
            return removed_page
        else:
            print("No pages to remove. Browsing history is empty.")
            return None

    # Check the number of pages in the browsing history
    def total_pages(self):
        count = len(self.history)
        print(f"Total pages viewed: {count}")
        return count

    # Check if the browsing history is empty
    def is_empty(self):
        empty = len(self.history) == 0
        print(f"Browsing history empty: {empty}")
        return empty

    # Display all pages in the browsing history
    def display_history(self):
        if self.is_empty():
            print("Browsing history is empty.")
        else:
            print("Browsing History:")
            for page in reversed(self.history):
                print(page)


# Testing the implementation
if __name__ == "__main__":
    try:
        # Create a BrowsingHistory object
        browser = BrowsingHistory()

        # Add pages
        browser.add_page("https://www.google.com")
        browser.add_page("https://www.github.com")
        browser.add_page("https://www.python.org")

        # Display history
        browser.display_history()

        # Check total pages
        browser.total_pages()

        # Remove a page
        browser.remove_page()

        # Display updated history
        browser.display_history()

        # Check if history is empty
        browser.is_empty()

    except Exception as e:
        print(f"Error: {e}")
