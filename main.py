def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(1)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.pause(1)
basic.forever(on_forever)
