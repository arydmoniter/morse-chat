radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        music.playTone(262, music.beat(BeatFraction.Sixteenth))
    } else {
        music.playTone(262, music.beat(BeatFraction.Half))
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(0)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(1)
})
radio.setGroup(226)
