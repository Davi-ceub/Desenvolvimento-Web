import requests

# 1 IP
# resp =requests.get("https://httpbin.org/ip")
# print(resp.status_code, resp.json())

# 2 imagem
# resp = requests.get("https://httpbin.org/image/jpeg")
# with open("imagem.jpg","wb") as file :
#     file.write(resp.content)

# 3 HTML
# resp = requests.get("https://httpbin.org/html")
# print("TEXT:",resp.text[:5000],"...")

# 4 BASE 64
# resp=requests.get("https://httpbin.org/base64/VGVzdGFuZG8gMSwgMiwgMy4uLg==")
# print(resp.text)

#5 get com query
# resp = requests.get(url="https://jsonplaceholder.typicode.com"+"/comments?postId=1")
# for c in resp.json():
#     print(c)

# 6 post
# url = "https://jsonplaceholder.typicode.com/posts"

# dados = {
#     "title": "Teste API",
#     "body": "Primeiro post com requests",
#     "userId": 123
# }

# resposta = requests.post(url, json=dados)

# print("Status Code:", resposta.status_code)
# print("Resposta do servidor:")
# print(resposta.json())