This is a Raspberry Pi project about the photo taking.

# Server
Server need to be running on a device with camera enabled.
To run the server:

```
cd server
./camera_server.py [--ip] [--port]
```

Once server received connection request, it will take a photo and send
client through a tcp socket.


# Client
To run the client:

```
cd client
./camera_client.py [--ip] [--port]
```

Client will receive an image file from server
