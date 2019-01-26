# audio main
# description still to be done

from aud_recordtofile import aud_recordtofile
# import constants -> path of audiofile , maildata

while TRUE:
    noise_detected = FALSE
    # is there any significant noise?
    # plan: use a special raspberry sensor via GPIO
    # any sleeps her or what is done in case of very long noises
    noise_detected = aud_listen()
    if noise_detected = TRUE:
        # record noise for some time and write it to file
        # record time in seconds
        # ?? no error messages?
        noiserec = aud_recordtofile(PATH, RECORDLEN)
        # send email
        aud_sendalarm(noiserec)
        # ok, job done - listen again after
        # ?? later: prevent sending to many mails
