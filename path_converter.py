import pyperclip, os, time

def path_converter():
    print("Running path converter ... (press Ctrl+C quit)")

    # Use to record last copy content, prevent to repeat.
    last_paste = ''

    try:
        while True:
            # Get the clipboard content.
            current_paste = pyperclip.paste()

            # Check if the content change and if it's a path.
            if current_paste != last_paste and ('\\' in current_paste or '/' in current_paste):

                # change the path
                if '//' in current_paste:
                    new_path = current_paste.replace('\\', '/')
                    direction = "Windows - Mac/通用"
                else:
                    new_path = current_paste.replace('/', '\\')
                    direction = "Mac/通用 - Windows"

                # put back clipboard
                if new_path != current_paste:
                    pyperclip.copy(new_path)

                    # renew the last copy
                    last_paste = new_path
                    print(f"Turn [{direction}]: {new_path}")
            
            # Pause 1 s
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n The program quit")

# run the program
path_converter()


                 
                

            

