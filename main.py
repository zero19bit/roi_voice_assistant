import webbrowser
import subprocess
import talk_to_write_FA
import talk_to_write_TR
import talk_to_write_US
import os
import pyautogui
import platform


def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def open_program(command):
    try:
        os.system(command)
        print("در حال بازشدن...")
    except Exception as e:
        print(f"خطا در باز کردن برنامه: {e}")


def process_farsi():
    while True:
        text = talk_to_write_FA.talk_to_write_FA()
        if not text:
            print("دستور نامفهوم بود.")
            continue

        if "سلام" in text:
            print("""
----------------------------
|سلام                       |    
|من ایمم roi هست          |    
|من یک دستیار صوتی هستم  |    
|چطور می تونم کمکتون کنم |         
---------------------------""")

        elif "باز" in text and "کن" in text:
            print("چه برنامه‌ای؟")
            answer = talk_to_write_FA.talk_to_write_FA()
            if "گوگل" in answer:
                webbrowser.open("https://www.google.com")
            elif "پایتون" in answer:
                open_program("pycharm64.exe")
            elif "نوت‌پد" in answer:
                open_program("notepad.exe")
            elif "کامپیوتر" in answer or "پی سی" in answer:
                subprocess.Popen(["explorer", "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}"])
            elif "یوتیوب موزیک" in answer:
                webbrowser.open("https://music.youtube.com/")
            elif "یوتیوب" in answer:
                webbrowser.open("https://www.youtube.com/")
            elif "تلگرام" in answer:
                webbrowser.open("https://web.telegram.org/k/")
            elif "اینستاگرام" in answer:
                webbrowser.open("https://www.instagram.com/")
            elif "اسپاتیفای" in answer:
                webbrowser.open("https://open.spotify.com/")
            elif "ترمینال" in answer:
                open_program("start cmd")
            else:
                print("برنامه‌ای با این نام پیدا نشد.")

        elif "اسکرین‌شات" in text or "عکس گرفتن" in text:
            pyautogui.hotkey("win", 'shift', "s")

        elif "صدا" in text and ("بلند" in text or "زیاد" in text):
            pyautogui.hotkey('volumeup')

        elif "صدا" in text and ("کم" in text or "پایین" in text):
            pyautogui.hotkey('volumedown')

        elif "قطع صدا" in text or "بی‌صدا" in text or "مایوت" in text:
            pyautogui.hotkey('volumemute')

        elif "آهنگ" in text and ("بعد" in text or "بعدی" in text):
            pyautogui.hotkey('nexttrack')

        elif "آهنگ" in text and ("قبل" in text or "قبلی" in text):
            pyautogui.hotkey('prevtrack')

        elif "پخش" in text or "توقف" in text:
            pyautogui.hotkey('playpause')

        elif "زبان دیگر" in text:
            break

        elif "خاموش" in text:
            print("مطمئنی؟")
            answer = talk_to_write_FA.talk_to_write_FA()
            if "آره" in answer or "بله" in answer:
                exit()


def process_turkish():
    while True:
        text = talk_to_write_TR.talk_to_write_TR()
        if not text:
            print("Anlamadım.")
            continue

        if "merhaba" in text or "selam" in text:
            print("Merhaba! Ben Roi. Sesli asistanınızım. Size nasıl yardımcı olabilirim?")

        elif "aç" in text:
            print("Hangi program?")
            answer = talk_to_write_TR.talk_to_write_TR()
            if "google" in answer:
                webbrowser.open("https://www.google.com")
            elif "python" in answer:
                open_program("pycharm64.exe")
            elif "not defteri" in answer or "notepad" in answer:
                open_program("notepad.exe")
            elif "bilgisayar" in answer:
                subprocess.Popen(["explorer", "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}"])
            elif "youtube müzik" in answer:
                webbrowser.open("https://music.youtube.com/")
            elif "youtube" in answer:
                webbrowser.open("https://www.youtube.com/")
            elif "telegram" in answer:
                webbrowser.open("https://web.telegram.org/k/")
            elif "instagram" in answer:
                webbrowser.open("https://www.instagram.com/")
            elif "spotify" in answer:
                webbrowser.open("https://open.spotify.com/")
            elif "cmd" in answer or "komut istemi" in answer:
                open_program("start cmd")
            else:
                print("Program bulunamadı.")

        elif "ekran görüntüsü" in text:
            pyautogui.hotkey("win", 'shift', "s")

        elif "ses" in text and "yükselt" in text:
            pyautogui.hotkey('volumeup')

        elif "ses" in text and "kıs" in text:
            pyautogui.hotkey('volumedown')

        elif "sessiz" in text:
            pyautogui.hotkey('volumemute')

        elif "sonraki" in text:
            pyautogui.hotkey('nexttrack')

        elif "önceki" in text:
            pyautogui.hotkey('prevtrack')

        elif "oynat" in text or "duraklat" in text:
            pyautogui.hotkey('playpause')

        elif "diğer dil" in text:
            break

        elif "kapat" in text:
            print("Emin misiniz?")
            answer = talk_to_write_TR.talk_to_write_TR()
            if "evet" in answer or "tamam" in answer:
                exit()


def process_english():
    while True:
        text = talk_to_write_US.talk_to_write_US()
        if not text:
            print("I didn't catch that.")
            continue

        if "hello" in text or "hi" in text:
            print("Hello! I'm Roi, your voice assistant. How can I help you?")

        elif "open" in text:
            print("What program?")
            answer = talk_to_write_US.talk_to_write_US()
            if "google" in answer:
                webbrowser.open("https://www.google.com")
            elif "python" in answer:
                open_program("pycharm64.exe")
            elif "notepad" in answer:
                open_program("notepad.exe")
            elif "this pc" in answer:
                subprocess.Popen(["explorer", "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}"])
            elif "youtube music" in answer:
                webbrowser.open("https://music.youtube.com/")
            elif "youtube" in answer:
                webbrowser.open("https://www.youtube.com/")
            elif "telegram" in answer:
                webbrowser.open("https://web.telegram.org/k/")
            elif "instagram" in answer:
                webbrowser.open("https://www.instagram.com/")
            elif "spotify" in answer:
                webbrowser.open("https://open.spotify.com/")
            elif "cmd" in answer:
                open_program("start cmd")
            else:
                print("Program not found.")

        elif "screenshot" in text:
            pyautogui.hotkey("win", 'shift', "s")

        elif "volume up" in text:
            pyautogui.hotkey('volumeup')

        elif "volume down" in text:
            pyautogui.hotkey('volumedown')

        elif "mute" in text:
            pyautogui.hotkey('volumemute')

        elif "next" in text:
            pyautogui.hotkey('nexttrack')

        elif "previous" in text:
            pyautogui.hotkey('prevtrack')

        elif "play" in text or "pause" in text:
            pyautogui.hotkey('playpause')

        elif "other language" in text:
            break

        elif "turn off" in text:
            print("Are you sure?")
            answer = talk_to_write_US.talk_to_write_US()
            if "yes" in answer:
                exit()


def main():
    clear_terminal()
    while True:
        print("""
    Select language:
    1) Persian
    2) Turkish
    3) English
        """)
        language = input("Enter choice: ").strip().lower()

        if language in ['1', 'persian']:
            process_farsi()
        elif language in ['2', 'turkish']:
            process_turkish()
        elif language in ['3', 'english']:
            process_english()
