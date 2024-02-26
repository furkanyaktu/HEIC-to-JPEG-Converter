import os
from PIL import Image
from pillow_heif import register_heif_opener

banner = '''
 _  _ ___ ___ ___   _            _ ___ ___ ___    ___                     _                         
 | || | __|_ _/ __| | |_ ___   _ | | _ \ __/ __|  / __|___ _ ___ _____ _ _| |_ ___ _ _               
 | __ | _| | | (__  |  _/ _ \ | || |  _/ _| (_ | | (__/ _ \ ' \ V / -_) '_|  _/ -_) '_|              
 |_||_|___|___\___|  \__\___/  \__/|_| |___\___|  \___\___/_||_\_/\___|_|  \__\___|_|                
   ___              _          _   ___        ___         _              __   ___   _  _______ _   _ 
  / __|_ _ ___ __ _| |_ ___ __| | | _ )_  _  | __|  _ _ _| |____ _ _ _   \ \ / /_\ | |/ /_   _| | | |
 | (__| '_/ -_) _` |  _/ -_) _` | | _ \ || | | _| || | '_| / / _` | ' \   \ V / _ \| ' <  | | | |_| |
  \___|_| \___\__,_|\__\___\__,_| |___/\_, | |_| \_,_|_| |_\_\__,_|_||_|   |_/_/ \_\_|\_\ |_|  \___/ 
                                       |__/                                                          

    ".heic" uzantılı dosyalarınız ".jpeg" dosyasına dönüştürülüyor.                                 
_____________________________________________________________________________________________________
PROCESSING:
'''


print(banner)

register_heif_opener()

def heic_to_jpeg(heic_file_path, jpeg_file_path):
    with open(heic_file_path, 'rb') as f:
        heif_file = Image.open(f)
        heif_file.save(jpeg_file_path, "JPEG")

def convert_heic_to_jpeg_in_current_directory():
    current_directory = os.getcwd()  
    for filename in os.listdir(current_directory):
        if filename.lower().endswith('.heic'):
            heic_file_path = os.path.join(current_directory, filename)
            jpeg_file_path = os.path.splitext(heic_file_path)[0] + '.jpeg'
            heic_to_jpeg(heic_file_path, jpeg_file_path)
            print(f"Converted {heic_file_path} to {jpeg_file_path}")

if __name__ == "__main__":
    convert_heic_to_jpeg_in_current_directory()