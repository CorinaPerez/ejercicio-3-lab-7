import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')
led2 = board.get_pin('d:11:o')
while True:
    analog_value = analog_input.read()
    print(analog_value)
    led.write(1)
    led2.write(1)
    if analog_value is not None:
        if analog_value > 0.80:
            led.write(1)
            time.sleep(0.30)
            led2.write(0)
            time.sleep(0.30)
            led.write(0)
            time.sleep(0.30)
            led2.write(1)
            time.sleep(0.30)
    else:
        time.sleep(1.0)