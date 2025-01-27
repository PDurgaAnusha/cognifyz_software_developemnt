import requests
from bs4 import BeautifulSoup

def fetch_job_postings(url):
    """Fetch and parse job postings from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status
        soup = BeautifulSoup(response.content, "html.parser")

        # Modify these selectors to match the structure of the target website
        job_titles = soup.find_all("h2", class_="job-title")  # Example selector
        company_names = soup.find_all("div", class_="company-name")  # Example selector

        jobs = []
        for title, company in zip(job_titles, company_names):
            jobs.append({
                "title": title.text.strip(),
                "company": company.text.strip(),
            })
        return jobs
    except Exception as e:
        print(f"Error: {e}")
        return None


def display_jobs(jobs):
    """Present job postings in a user-friendly format."""
    if not jobs:
        print("No job postings found.")
        return

    print("\nJob Postings:")
    for i, job in enumerate(jobs, start=1):
        print(f"{i}. {job['title']} at {job['company']}")


def main():
    print("Welcome to the Interactive Web Scraper!")
    while True:
        print("\nMenu:")
        print("1. Fetch job postings")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            url = input("Enter the website URL to scrape (e.g., https://example.com/jobs): ")
            print("Fetching data, please wait...")
            jobs = fetch_job_postings(url)
            display_jobs(jobs)
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
