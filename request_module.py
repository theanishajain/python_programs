import requests
response = requests.get("Https://github.com/repos/kubernetes/kubernetes/pulls")
data = response.json()
print(data)

