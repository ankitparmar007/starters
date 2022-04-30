from telethon import TelegramClient, events

api_id = 1220132
api_hash = 'bce9981f5e11687d0674531e1ca6f9b1'

teleclient = TelegramClient('qodditest', api_id, api_hash)

source_list = ['givemedata']

print("program running")

@teleclient.on(events.NewMessage(chats=source_list))
async def my_event_handler(event):
    print("teleclient events called")
    msg = event.message.message
    print(f"{msg = }")
    await teleclient.send_message("givemedata2",msg)

def run():
    print("run called")
    teleclient.start()
    teleclient.run_until_disconnected()

run()