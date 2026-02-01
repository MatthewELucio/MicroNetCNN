import wget
import json 
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def download(item):
    uuid, data = item
    url = data['image_url']
    file_name = f'{uuid}.jpg'
    try:
        wget.download(url, out='micronet_images/' + file_name, bar=None)
        return True
    except Exception:
        return False

def main():
    if not os.path.exists('micronet_images/'):
        os.makedirs('micronet_images/')
    with open('micronet_annotations.json', 'r') as f:
        annotations = json.load(f)

    items = list(annotations.items())
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(tqdm(executor.map(lambda x: download(x), items), total=len(items)))

if __name__ == '__main__':
    main()