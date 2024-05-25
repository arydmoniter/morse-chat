def on_received_number(receivedNumber):
    if receivedNumber == 0:
        music.play_tone(262, music.beat(BeatFraction.SIXTEENTH))
    else:
        music.play_tone(262, music.beat(BeatFraction.HALF))
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(226)