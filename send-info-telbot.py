import requests

msg = input("your message: ")

http = requests.get(f"https://api.telegram.org/bot7937463970:AAGrbswdXbiYXge1CMttUWQaAi347o4mnrQ/sendmessage?chat_id=5277103165&text={msg}")

print(http.content.decode())

# "api.telegram.org/bot7937463970:AAGrbswdXbiYXge1CMttUWQaAi347o4mnrQ/sendmessage?chat_id=5277103165&text=salam"
