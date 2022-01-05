import requests


r = requests.get('http://127.0.0.1:5000/')
data = r.json()

print(f"There are {data['people']} people. {data['cats']} of them have a cat, and {data['dogs']} of them have a dog")

if __name__ == '__main__':
    data = {
        'pens':12,
        'pencils':'eight'
    }
    r = requests.post('http://127.0.0.1:5000/send_me_data', data=data)
    print(r.text)