from pypresence import Presence
import time

with open('client_id.txt', 'r') as f: # Read the client ID from a file. You'll have to make one yourself as its unsafe to put it in the code.
    client_id = f.read() # Set the client ID to the contents of the file
    
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="Lookie Lookie", details="A test of qwertyquerty's Python Discord RPC wrapper, pypresence!"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds