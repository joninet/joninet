import requests

def get_image_aspect_ratio(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        width, height = image.size
        return width / height
    else:
        return None


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
    aspect_ratio = get_image_aspect_ratio(url)
    print(aspect_ratio)
