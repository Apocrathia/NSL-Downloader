# NASA Sounds Downloader

This project is a script that downloads audio files from the NASA sounds library page. It uses Selenium and BeautifulSoup to fetch the HTML content, parse the links, and download the audio files.

## Features

- Scrapes the NASA sounds library page for audio links
- Filters links based on the presence of .mp3 or .wav file extensions
- Downloads and saves audio files locally

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- Requests
- WebDriver Manager

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/yourrepository.git
```

2. Change to the project directory:

```
cd yourrepository
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

Run the script using the following command:

```
python nasa_sounds_downloader.py
```

This will download the audio files to a directory named "nasa_sounds" in the project directory.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.
