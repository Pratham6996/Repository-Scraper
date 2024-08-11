# GitHub Repository Scraper 

This Python script scrapes GitHub repositories and extracts relevant information such as the repository name, username, star count, and the URL to the repository. The extracted data is stored in an Excel file.

## Features

- Scrapes multiple pages of repositories on GitHub.
- Extracts repository details including username, repository name, star count, and URL.
- Saves the data into a well-structured Excel file.
- Automatically handles pagination to scrape data from multiple pages.

## Getting Started

Follow the instructions below to set up and run the scraper locally.

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Required Python libraries: `requests`, `pandas`, `beautifulsoup4`, `lxml`

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/repository-scraper-java.git

2. Navigate to the project directory:

   ```bash
   cd repository-scraper-java

3. Install the required Python packages:

   ```bash
   pip install requests pandas beautifulsoup4 lxml

## Usage

To scrape GitHub repositories related to Java and save the data to an Excel file:

1. **Run the Java script**:
   ```bash
   Java.py

### Script Functionality

- The script fetches HTML content from multiple pages of the Java topic on GitHub.
- It uses BeautifulSoup to parse the HTML and extract repository details.
- Details extracted include:
  - **Username**: The GitHub username of the repository owner.
  - **Repository name**: The name of the repository.
  - **Stars**: The number of stars the repository has.
  - **URL**: The URL to the repository.
- The data is compiled into a pandas DataFrame.
- The DataFrame is cleaned and reformatted as needed.
- Finally, the DataFrame is saved into an Excel file named `Git_Pro_E2S_Java.xlsx`.

## Built With

- Python
- BeautifulSoup4 - For web scraping
- Requests - For handling HTTP requests
- Pandas - For data manipulation and exporting to Excel

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.

## Acknowledgments

- Thanks to the open-source community for the tools and libraries used in this project.
- Inspired by the need to analyze popular Java repositories on GitHub.
