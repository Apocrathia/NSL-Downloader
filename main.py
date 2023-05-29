#!/opt/homebrew/bin/python3

import os
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Fetch the HTML content of the NASA sound library page
URL = "https://www.nasa.gov/connect/sounds/index.html"
driver.get(URL)

# Wait for the page to fully render
wait = WebDriverWait(driver, 10)  # Timeout after 10 seconds
wait.until(EC.presence_of_element_located((By.ID, "content")))

# Get the fully rendered HTML content
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the 'a' tags with the 'href' attribute
links = soup.find_all('a', href=True)

print(f"Found {len(links)} links")

# Create a regex pattern to match URLs ending with .mp3 or .wav on nasa.gov
regex_pattern = re.compile(r'^https?://(?:www\.)?nasa\.gov/.+?\.(?:mp3|wav)$')

# Filter the links based on the regex pattern
audio_links = [link for link in links if regex_pattern.match(link['href'])]

print(f"Found {len(audio_links)} audio_links")

# Download and save the audio files
download_directory = "nasa_sounds"
os.makedirs(download_directory, exist_ok=True)

for link in audio_links:
    # Get the hyperlink text
    hyperlink_text = link.text

    # Get the file extension from the href attribute
    file_extension = re.search(r'\.(mp3|wav)$', link['href'])
    file_extension = file_extension.group(0)

    # Clean the hyperlink text by removing any invalid characters
    cleaned_text = re.sub(r'[\\/*?:"<>|]', '', hyperlink_text)

    # Combine the cleaned hyperlink text with the file extension
    file_name = f"{cleaned_text}{file_extension}"
    download_path = os.path.join(download_directory, file_name)

    # Download and save the audio file
    response = requests.get(link['href'], stream=True)
    with open(download_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print(f"Downloaded {file_name}")

# Close the Selenium WebDriver
driver.quit()
