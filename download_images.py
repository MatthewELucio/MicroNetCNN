import wget 
import json 

def main():
    with open('micronet_annotations.json', 'r') as f:
        annotations = json.load(f)
    for uiud, data in annotations.items():
        url = data['image_url']
        file_name = "file" + str(data['id']) + ".jpg"
        wget.download(url, out='micronet_images/' + file_name)



if __name__ == '__main__':
    main()