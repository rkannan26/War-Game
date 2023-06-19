from tkinter import *
import random

import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()



root.title("War Game")
root.geometry("1000x700")


def resize_cards(card):
    our_card_img = Image.open(card)
    our_card_resize_image = our_card_img.resize((150, 218))

    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

    return our_card_image

def shuffle():
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)

    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')


    global dealer
    global player
    global dscore
    global pscore
    dealer = []
    player = []
    dscore = []
    pscore = []


    dealer_card = random.choice(deck)
    deck.remove(dealer_card)
    dealer.append(dealer_card)

    global dealer_image
    dealer_image = resize_cards(f'C:/Users/email/PycharmProjects/PNG-cards-1.3/{dealer_card}.png')

    dealer_label.config(image = dealer_image)



    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)

    global player_image
    player_image = resize_cards(f'C:/Users/email/PycharmProjects/PNG-cards-1.3/{player_card}.png')

    player_label.config(image=player_image)



    root.title(f'War Game - {len(deck)} Cards Left')

    score(dealer_card, player_card)
def score(dealer_card, player_card):
    dealer_card = int(dealer_card.split("_", 1)[0])
    player_card = int(player_card.split("_", 1)[0])

    if dealer_card == player_card:
        score_label.configure(text="Tie! Play Again!")
    elif dealer_card > player_card:
        score_label.configure(text="Dealer Wins!")
        dscore.append("x")
    else:
        score_label.configure(text="Player Wins!")
        pscore.append("x")

    root.title(f'War Game - {len(deck)} Cards Left |   Dealer : {dscore.count("x")}   Player: {pscore.count("x")}')





def deal_cards():
    try:
        dealer_card = random.choice(deck)
        deck.remove(dealer_card)
        dealer.append(dealer_card)
        global dealer_image
        dealer_image = resize_cards(f'C:/Users/email/PycharmProjects/PNG-cards-1.3/{dealer_card}.png')

        dealer_label.config(image=dealer_image)

        player_card = random.choice(deck)
        deck.remove(player_card)
        player.append(player_card)
        global player_image
        player_image = resize_cards(f'C:/Users/email/PycharmProjects/PNG-cards-1.3/{player_card}.png')

        player_label.config(image=player_image)
        root.title(f'War Game - {len(deck)} Cards Left')
        score(dealer_card, player_card)
    except:
        if dscore.count("x") == pscore.count("x"):
            root.title(f'War Game - Game Over! Tie! {dscore.count("x")} to {pscore.count("x")}')
        elif dscore.count("x") > pscore.count("x"):
            root.title(f'War Game - Game Over! Dealer Wins! {dscore.count("x")} to {pscore.count("x")}')
        else:
            root.title(f'War Game - Game Over! Player Wins! {pscore.count("x")} to {dscore.count("x")}')




my_frame = customtkinter.CTkFrame(root, width = 100)
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

score_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 22), text_color= "red")
score_label.pack(pady=20)

shuffle_button = customtkinter.CTkButton(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = customtkinter.CTkButton(root, text="Get Cards", font=("Helvetica", 14), fg_color= "blue", command=deal_cards)
card_button.pack(pady=10)




shuffle()


root.mainloop()
