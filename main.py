import os
import shutil

import requests

# VK User Token (https://vk.com/dev/authcode_flow_user)
access_token = ""
# VK albums download location in format "YOUR_PATH/{}/"
path = os.path.expanduser("~/Downloads/VK photos/{}/")


def main():
    get_all_photos("ID of a user or community that owns the photos")


def get_all_photos(owner_id):
    url = "https://api.vk.com/method/photos.getAll"
    offset = 0
    count = 200
    while True:
        req = requests.get(url, params={"owner_id": owner_id, "extended": 0, "offset": offset, "count": count,
                                        "photo_sizes": 1, "need_hidden": 1, "v": 5.64,
                                        "access_token": access_token})
        req.raise_for_status()
        r = req.json()
        if "error" in r:
            print("API error: {}".format(r["error"]["error_msg"]))
            break
        items = r["response"]["items"]
        if not items:
            break
        for item in items:
            album_id = item["album_id"]
            sizes = item["sizes"]
            if sizes:
                src = sizes[-1]["src"]
                save_photo(album_id, src)
        offset += count


def save_photo(album_id, src):
    print("Downloading photo from {}".format(src))
    r = requests.get(src, stream=True)
    if r.status_code == requests.codes.ok:
        directory = path.format(album_id)
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = src.rsplit('/', 1)[-1]
        photo_path = directory + filename
        with open(photo_path, "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            print("{} was saved".format(filename))


if __name__ == "__main__":
    main()
