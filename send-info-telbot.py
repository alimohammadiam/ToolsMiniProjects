import requests

# "api.telegram.org/bot7937463970:AAGrbswdXbiYXge1CMttUWQaAi347o4mnrQ/sendmessage?chat_id=5277103165&text=salam"

msg = input("your message: ")

url = f"https://api.telegram.org/bot7937463970:AAGrbswdXbiYXge1CMttUWQaAi347o4mnrQ/sendmessage?chat_id=5277103165&text={msg}"

# http = requests.get(url)
#
# print(http.content.decode())

mydata = {
    "UrlBox": url,
    "AgentList": "Internet Explorer",
    "VersionList": "HTTP/1.1",
    "MethodList": "GET"
}

http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=mydata)


