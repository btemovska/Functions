#write a function that will take care of the formatting a text

def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dump,")
banner_text("Don't be silly champ,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")

# ********************************************************************************
# **                 Always look on the bright side of life...                  **
# **                        If life seems jolly rotten,                         **
# **                    There's something you've forgotten!                     **
# **             And that's to laugh and smile and dance and sing,              **
# **                                                                            **
# **                      When you're feeling in the dump,                      **
# **                           Don't be silly champ,                            **
# **            Just purse your lips and whistle - that's the thing!            **
# **              And... always look on the bright side of life...              **
# ********************************************************************************