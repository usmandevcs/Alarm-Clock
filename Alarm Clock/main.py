# Python Alarm Clock
# ==================
'''
This is a simple alarm clock application that allows you to set 
an alarm for a specific time. When the alarm goes off, it will 
play a sound to wake you up.
'''
import time
import datetime
import os
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    sound_file = os.path.join(os.path.dirname(__file__), "my_music.mp3")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
        if current_time == alarm_time:
            print("Wake up! It's time!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        time.sleep(1)  # Check the time every second

        # Optional: Add snooze and stop functionality
        # snooze = input("Do you want to snooze the alarm? (yes/no): ")
        # if snooze.lower() == "yes":
        #     snooze_time = 5  # Snooze for 5 minutes
        #     new_alarm_time = (datetime.datetime.strptime(alarm_time, "%H:%M:%S") + datetime.timedelta(minutes=snooze_time)).strftime("%H:%M:%S")
        #     print(f"Snoozing for {snooze_time} minutes. New alarm time: {new_alarm_time}")
        #     alarm_time = new_alarm_time
        # Optional: Add stop functionality
        # stop_alarm = input("Do you want to stop the alarm? (yes/no): ")
        # if stop_alarm.lower() == "yes":
        #     print("Alarm stopped.")
        #     is_running = False

if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm (HH:MM:SS): ")
    set_alarm(alarm_time)
