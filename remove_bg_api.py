# Requires "requests" to be installed (see python-requests.org)
import requests
import os
# import move from move_bgr
# from move_bgr import move


def bgr(path, output):
    lis = os.listdir(path)
    for i in lis:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(path+i, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'h49NxYVhLTuRzuXzzzM8usij'},
        )
        if response.status_code == requests.codes.ok:
            with open(output+i, 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    path = '/home/user/Downloads/drive-download-20200522T084538Z-001/videoplayback/'
    lis = os.listdir(path)
    out = '/home/user/Downloads/drive-download-20200522T084538Z-001/videoplayback_bgr/'
    bgr(path, out)
    # move()