import psutil
from pypresence import Presence
import time
import random

with open('client_id.txt', 'r') as f: # Read the client ID from a file. You'll have to make the file yourself as its unsafe to put it in the code.
    client_id = f.read() # Set the client ID to the contents of the file

RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Connect to the discord API


# Set a while loop to true to run the code forever.
while True:
    # Generate a random number to make the presence have random encounters that have the chance to change every 15 seconds. Make sure you one set to a higher chance if you want it to exist more often.
    encounter = random.randint(1,1000)
    if encounter <= 20 and encounter > 10:
        
        # Save which encounter was selected so that it can be shown in the console
        set_encounter = "Scary Eyebrow"
        
        RPC.update(
            
            large_image="eyebrow", # Set the large image to the one you uploaded to the dev portal
            large_text="woah", # Set the large image text to something so it shows when you hover over it
            
            buttons=[{ # Set the buttons up to show and link somewhere, you can have up to 2 buttons.
                "label": "Click To RUN",  # Set the button label to some text so the user knows what it does
                "url": "https://www.youtube.com/watch?v=W6oQUDFV2C0" # Set the button URL to something so it links to whatever you want
                }, 
                {"label": "Click to Cry",
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                }], 
            
            details="You must choose. . .", state="Select an option. . .")  # Set the presence
    elif encounter <= 10:
        
        # Save which encounter was selected so that it can be shown in the console
        set_encounter = "Petpatpetpetpat"
        
        RPC.update(
            
            large_image="pfpable", # Set the large image to the one you uploaded to the dev portal
            large_text="Lookit the scremmer! This one is a rare encounter!", # Set the large image text to something so it shows when you hover over it
            
            buttons=[{ # Set the buttons up to show and link somewhere, you can have up to 2 buttons.
                "label": "Click to petpatpetpetpat",  # Set the button label to some text so the user knows what it does
                "url": "https://www.youtube.com/watch?v=ES9kFax89MA" # Set the button URL to something so it links to whatever you want
                }, 
                {"label": "Click to b0nk",
                "url": "https://www.youtube.com/watch?v=ZXK427oXjn8"
                }], 
            
            details="A wild scremmer appeared!", state="What will you do with this...") # Set the presence
    else:
        # Most likely encounter
        
        # Save which encounter was selected so that it can be shown in the console
        set_encounter = "Default"
        
        # Get CPU and RAM Usage for display
        cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
        mem = psutil.virtual_memory() # Get RAM Usage
        mem_per = round(psutil.virtual_memory().percent,1) # Simplify RAM Usage
        
        RPC.update(
            
            large_image="breb", # Set the large image to the one you uploaded to the dev portal
            large_text="A big screm", # Set the large image text to something so it shows when you hover over it
            
            buttons=[{ # Set the buttons up to show and link somewhere, you can have up to 2 buttons.
                "label": "Click To Screm",  # Set the button label to some text so the user knows what it does
                "url": "https://www.youtube.com/watch?v=zk1mAd77Hr4" # Set the button URL to something so it links to whatever you want
                }, 
                {"label": "Genuine Happiness",
                "url": "https://www.youtube.com/watch?v=BST9qwdhQAY"
                }], 
            
            details="CPU: "+str(cpu_per)+"%", state="RAM: "+str(mem_per)+"%")  # Set the presence 
    
    print(f"The random number is {encounter}. Presence updated to the: {set_encounter} encounter") # Print to the console that the presence has been updated
    
    time.sleep(15) # Set a sleep timer so discord doesn't rate limit you for pretty much dossing their servers