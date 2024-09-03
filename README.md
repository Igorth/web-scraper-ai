# AI Web Scraper

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0-orange)
![Selenium](https://img.shields.io/badge/Selenium-4.0-yellow)
![Langchain](https://img.shields.io/badge/Langchain-0.1-green)
![Ollama LLM](https://img.shields.io/badge/Ollama%20LLM-Enabled-blue)
[![Test Coverage](https://img.shields.io/badge/Test%20Coverage-100%25-brightgreen)](https://pytest.org/)
[![CI/CD](https://github.com/Igorth/web-scraper-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/Igorth/web-scraper-ai/actions)

## Overview

The **AI Web Scraper** is a Python-based application that uses Streamlit for the frontend, 
Selenium for web scraping, and Ollama's LLM for natural language processing. 
The application allows users to scrape websites, extract content, and parse it based on a provided description.

## Resources

[Video](https://www.youtube.com/watch?v=Oo8-nEuDBkk)

## Features

- **Web Scraping:** Leverages Selenium to scrape dynamic content from websites.
- **Content Cleaning:** Processes and cleans the scraped HTML content using BeautifulSoup.
- **Natural Language Parsing:** Uses Langchain with Ollama LLM to parse the content based on user input.
- **Streamlit Interface:** Provides a user-friendly interface for entering URLs, viewing content, and running parsing operations.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/Igorth/web-scraper-ai
cd ai-web-scraper
```
2. Set up a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables by creating a `.env` file:
```bash
touch .env
```

5. Add your Selenium WebDriver path:
```commandline
SBR_WEBDRIVER=<path-to-your-webdriver>
```
## Usage
To start the application, run:
```bash
streamlit run main.py
```

## How It Works
- **Input:** Enter a website URL to scrape.
- **Scraping:** Click "Scrape Site" to fetch and display the website's content.
- **Parsing:** Provide a description of what you want to parse from the content.
- **Result:** The parsed data is displayed according to the provided description.

## Testing
The project uses `pytest` for testing. To run the tests:
```bash
pytest
```

## Continuous Integration
This project is set up with GitHub Actions for CI/CD. The pipeline runs tests on every push to the `main` 
branch and ensures that all tests pass before deploying.