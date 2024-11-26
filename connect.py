import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected to the server!")
    await sio.disconnect()

@sio.event
async def disconnect():
    print("Disconnected from the server!")

async def start_connection():
    try:
        await sio.connect('https://kit.digitalauto.tech', wait_timeout=10)
        print("Connected successfully!")
        await sio.wait()
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    print("Container running")
    asyncio.run(start_connection())
