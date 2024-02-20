import uvicorn
import streamsync.serve
from fastapi import FastAPI, Response

root_asgi_app = FastAPI()
sub_asgi_app = streamsync.serve.get_asgi_app("./testapp", "run")

root_asgi_app.mount("/testapp", sub_asgi_app)

@root_asgi_app.get("/")
async def init():
    return Response("""
    <h1>Welcome to the App Hub</h1>
    """)

uvicorn.run(root_asgi_app,
    host="0.0.0.0",
    port=5328,
    log_level="warning",
    ws_max_size=streamsync.serve.MAX_WEBSOCKET_MESSAGE_SIZE)