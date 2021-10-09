import requests
from os.path import dirname, exists
from os import makedirs


project_path = dirname(__file__)
data_dir = project_path + "/data"
if not exists(data_dir):
    makedirs(data_dir)


breed_url = "https://dog.ceo/api/breeds/list/all"
breed_response = requests.get(breed_url)
breed_dict = breed_response.json().get('message')
single_breed = [x for x in breed_dict if len(breed_dict.get(x)) == 0]
multi_breed = [i+"/"+j for i in breed_dict for j in breed_dict.get(i) if len(breed_dict.get(i)) > 0]
breed_lst = single_breed + multi_breed


def get_img_url(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images"
    img_response = requests.get(url)
    img_lst = img_response.json().get('message')
    if not exists(f"{data_dir}/{breed}"):
        makedirs(f"{data_dir}/{breed}")
    for i in img_lst:
        download_img(breed, i)


def download_img(breed, url):
    response = requests.get(url)
    with open(f"{data_dir}/{breed}/{url.split('/')[-1]}", "wb") as file:
        file.write(response.content)


for i in breed_lst:
    get_img_url(i)
