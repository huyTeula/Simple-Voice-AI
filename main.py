import speech_recognition
import pyttsx3
from datetime import date, datetime

# Khởi tạo trình nói
robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty('voices')
for voice in voices:
    robot_mouth.setProperty('voice', voice.id)

# Khởi tạo trình nghe
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
you = ""

while True:
    print("Robot: Do you want to speak or type? (say/type)")
    mode = input("Mode (say/type): ").strip().lower()  # Người dùng chọn chế độ

    if mode == "say":
        with speech_recognition.Microphone() as mic:
            print("Robot: I'm listening...")
            audio = robot_ear.record(mic, duration=3)

        try:
            you = robot_ear.recognize_google(audio)
        except:
            you = ""
    elif mode == "type":
        you = input("You: ")

    print("You: " + you)

    if you == "":
        robot_brain = "聞こえません。もう一度試してください。"
    elif "hello" in you:
        robot_brain = "Hi! Huy"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%d %B, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H:%M:%S")
    elif "bye" in you:
        robot_brain = "さよなら"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "理解できない。"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
