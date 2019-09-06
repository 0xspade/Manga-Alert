#!/usr/bin/python3
import datetime, cfscrape, requests

x = datetime.datetime.now()
key="" ## Create your own bot api_key to BotFather in Telegram
id="" ## Find your Telegram ID >> google is your friend

current_date = x.strftime("%Y/%m/%d")
manga=[["One Piece","https://w10.mangafreak.net/Manga/One_Piece"], ["One Punch Man","https://w10.mangafreak.net/Manga/Onepunch_Man"]]

def string(text):
    return str(b'%s', encoding='utf-8', errors='strict') %format(text)

def alert(manga_url, date):
    scraper = cfscrape.create_scraper()
    request = scraper.get(manga_url)
    date = string(date)
    req = string(request.content)
    datex = "<tr>"+date+"</tr>"
    if datex in req:
        return True
    else:
        return False


def send_alert(id, api_key, message):
    api_key = string(api_key)
    id = string(id)
    message = string(message)

    url="https://api.telegram.org/bot"+api_key+"/sendmessage"
    data={"chat_id":id,"text":message}
    requests.get(url, data=data)

for manga_url in manga:
    title=manga_url[0]
    url=manga_url[1]
    if alert(url, current_date) is True:
        send_alert(id, key, "[+]"+current_date+"[+]\r\nThere is a New episode in "+title+"\r\n"+url)
    elif alert(url, current_date) is False:
        send_alert(id, key, "No New Episode for "+title)
    else:
        send_alert(id, key, "An Error Occured")
