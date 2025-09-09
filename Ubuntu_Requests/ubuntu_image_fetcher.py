import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = []
    while True:
        url = input("Please enter the image URL(or 'done' to finish): ")
        if url.lower() == 'done':
            break
        urls.append(url)
    
    directory = "Fetched_Images"
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {directory}: {e}")
        return
    
    downloaded_hashes = set()
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
                downloaded_hashes.add(file_hash)
        
    for url in urls:
        print(f"Attempting to fetch: {url}")

        allowed_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg')
        if not urlparse(url).path.lower().endswith(allowed_extensions):
            print("URL does not appear to be a direct link to a supported image file. Skipping...")
            continue

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko), Chrome/91.0.4472.124 Safari/537.36"
            }
            
            head_response = requests.head(url, timeout=5, headers=headers)
            head_response.raise_for_status()

            content_type = head_response.headers.get('Content-Type', '')
            if 'image' not in content_type:
                print(f"Server response indicates content is not an image (Content-Type: {content_type}). Skipping.")
                continue

            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()

            file_hash = hashlib.sha256(response.content).hexdigest()
            if file_hash in downloaded_hashes:
                print(f"This image has already been downloaded. Skipping to avoid duplication.")
                continue

            parse_url = urlparse(url)
            filename = os.path.basename(parse_url.path)
            if not filename or '.' not in filename:
                filename = f"downloaded_image_{len(downloaded_hashes)}.jpg"
            
            filepath = os.path.join(directory, filename)

            with open(filepath, 'wb') as f:
                f.write(response.content)

            downloaded_hashes.add(file_hash)

            print(f"Successfully fetched: {filename}")
            print(f"Image saved to {filepath}")
        
        except requests.exceptions.RequestException as e:
            print(f"Connection or download error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
    print(f"\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()