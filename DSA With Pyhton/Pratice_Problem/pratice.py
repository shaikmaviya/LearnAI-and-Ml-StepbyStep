import pywhatkit
import time

phone_number = "+916305742176"

try:
    # Send "Sorry" 10 times
    for i in range(10):
        pywhatkit.sendwhatmsg_instantly(phone_number, "Sorry", wait_time=10, tab_close=True, close_time=2)
        print(f"Sent 'Sorry' message {i+1}/10")
        time.sleep(5)

    # Send "Tu kiku asa karti hai"
    pywhatkit.sendwhatmsg_instantly(phone_number, "Tu kiku asa karti hai", wait_time=10, tab_close=True, close_time=2)
    print("Sent 'Tu kiku asa karti hai'")
    time.sleep(5)

    # Send "Next mai duri night message kartu tujay"
    pywhatkit.sendwhatmsg_instantly(phone_number, "mai puri night message kartu tujay", wait_time=10, tab_close=True, close_time=2)
    print("Sent 'mai puri night message kartu tujay'")

except Exception as e:
    print("An error occurred:", e)
