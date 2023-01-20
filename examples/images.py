from pypresence import Presence
import time

"""
You need to upload your image(s) here:
https://discord.com/developers/applications/<APP ID>/rich-presence/assets
"""

with open('client_id.txt', 'r') as f: # Read the client ID from a file. You'll have to make one yourself as its unsafe to put it in the code.
    client_id = f.read() # Set the client ID to the contents of the file
RPC = Presence(client_id=client_id)
RPC.connect()

# Make sure you are using the same name that you used when uploading the image, then you can set an alternate option for the text that shows when you hover over the image.
RPC.update(large_image="hungy", large_text="HUMBGHRY",
            small_image="small-image", small_text="Small Text Here!")

while 1:
    time.sleep(15) #Can only update presence every 15 seconds