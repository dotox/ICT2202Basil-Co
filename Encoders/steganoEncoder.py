from stegano import lsb

    secret = lsb.hide("./input.PNG","This is hidden with Stegano")
    secret.save("./hidden_Stegano.png")
    print("DONE")