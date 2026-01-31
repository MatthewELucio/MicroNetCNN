import wget 
import json 
import os

def main():
    if not os.path.exists('micronet_images/'):
        os.makedirs('micronet_images/')
    with open('micronet_annotations.json', 'r') as f:
        annotations = json.load(f)
    for uiud, data in annotations.items():
        url = data['image_url']
        file_name = "file" + str(data['id']) + ".jpg"
        try:
            wget.download(url, out='micronet_images/' + file_name)
        except Exception as e:
            pass

if __name__ == '__main__':
    main()