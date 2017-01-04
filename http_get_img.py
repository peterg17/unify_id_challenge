import requests


if __name__=='__main__':
    #example URL: "https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new"
    total_response = ""
    for i in range(0,4):
        payload = {'num': '10000', 'min': '0', 'max': '255', 'col': '1', 'base': '10', 'format': 'plain', 'rnd':'new'}
        r = requests.get('https://www.random.org/integers', params=payload)
        response = r.text
        total_response += response
        code = r.status_code
        print(code)

    payload = {'num': '9152', 'min': '0', 'max': '255', 'col': '1', 'base': '10', 'format': 'plain', 'rnd':'new'}
    r = requests.get('https://www.random.org/integers', params=payload)
    response = r.text
    total_response += response
    code = r.status_code
    print(code)

    with open("random_nums.txt", "w") as f:
        f.write(total_response)
