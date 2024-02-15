import pygame
import time
import speech_recognition as sr


def play_song(song_url):
    pygame.mixer.init()
    pygame.mixer.music.load(song_url)
    pygame.mixer.music.play()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    paused = False  # Flag to track whether the song is paused
    listen_enabled = False  # Flag to control when to listen

    while True:  # Infinite loop to keep listening
        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)

            if "stop" in command:
                pygame.mixer.music.stop()
                print("Song stopped.")
                if not paused:
                    # If not paused, exit the loop
                    break
            elif "pause" in command:
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                    print("Song paused.")
                else:
                    print("Song is already paused.")
            elif "unpause" in command or "resume" in command:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("Song continued.")
                else:
                    print("Song is already playing.")
            elif "hello" in command:
                listen_enabled = True  # Enable listening when "hello" is detected
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")

        if listen_enabled:
            time.sleep(0.1)  # Adjust this sleep time as needed

    print("Exiting program.")


def play_music(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        print(f"Playing {file_path}")
        pygame.mixer.music.play()

        # Allow the music to play for the duration of the song
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except pygame.error as e:
        print(f"Error: {e}")

    finally:
        pygame.mixer.quit()


# play_song(r'C:\Users\koks\Desktop\jarvis\sad songs\sad1.mp3')
# play_music(r'C:\Users\koks\Desktop\jarvis\happy songs\happy.mp3')
