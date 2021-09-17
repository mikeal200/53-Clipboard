import pyperclip
from pynput.keyboard import Key, Listener
from datetime import date

running = True

today = date.today()
today = today.strftime("%x")
today = today.replace('/', '.')
today = today.replace('0', '', 1)

while running:
    def on_press(key):
        if key == Key.f2:
            pyperclip.copy("from Covid related log")
        if key == Key.f6:
            pyperclip.copy("Closing list received " + today)
        if key == Key.f4:
            pyperclip.copy("Processed")
        if key == Key.f9:
            pyperclip.copy("Processed. Date fixed")
        if key == Key.f10:
            pyperclip.copy("Someone in file, keep on list")
        if key == Key.menu:
            pyperclip.copy("Hardstop, keep on list")
        if key == Key.media_volume_mute:
            pyperclip.copy("Exp. Date shows.")
        if key == Key.media_volume_down:
            pyperclip.copy("in Completed Loans, did not process")
        if key == Key.media_volume_up:
            pyperclip.copy("in Post Closing, did not process")
        if key == Key.alt_l:
            pyperclip.copy("Attention Fulfillment, please read!  Running All/Running One/or Repricing the loan will need to be executed by Secondary Marketing.  Do not perform these actions on this loan.  Please send an email to SecondaryMarketingInquiry.Cincinnati@53.com and specify the product and interest rate required.  This applies to reselecting the same rate and product as well.\n"

            "\nSales partners if you are seeing this message when the loan is still in origination/opening continue to send the request via our Mortgage Loan Change Request form. This applies to reselecting the same rate and product as well.")    

    with Listener(on_press=on_press) as listener:
        listener.join()

