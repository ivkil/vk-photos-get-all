# vk_photos_get_all

Download VK photos belonging to a user or community


## Usage

1) Get VK [User Token][1]. [Access rights][2] required: **photos**.
```python
access_token = "{ACCESS_TOKEN}"
```
2) Set VK albums download location:
```python
path = "{PATH_TO_ALBUMS}/{}/"
```
3) Specify ID of a user or community that owns the photos:
```python
def main():
    get_all_photos({OWNER_ID})
```
4) Run `main.py` script.


## Built With

* [Requests: HTTP for Humans][3]

[1]: https://vk.com/dev/access_token
[2]: https://vk.com/dev/permissions
[3]: http://docs.python-requests.org/