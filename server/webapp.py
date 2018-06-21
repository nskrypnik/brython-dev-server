import queue
from asyncio import sleep
from aiohttp import web
from .watchdog import RESTART_QUEUE

index_html = open('./client/index.html', 'rb').read()

async def index(request):
    return web.Response(body=index_html, content_type='text/html')

async def ws_restart_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    '''
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())
    '''

    while True:
        await sleep(1)
        try:
            if RESTART_QUEUE.get_nowait():
                print('Restarting app')
                await ws.send_str('restart')
        except queue.Empty:
            pass

    print('websocket connection closed')

    return ws

def start_web_server():
    app = web.Application()
    app.add_routes([
        web.get('/', index),
        web.get('/ws/restart', ws_restart_handler),
        web.static('/src', './client')
    ])

    web.run_app(app, port=8081)
