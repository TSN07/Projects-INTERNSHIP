from stegano import lsb

print("1. Hide Message")
print("2. Reveal Message")
choice = input("Choose (1/2): ")

if choice == "1":
    msg = input("Enter secret message: ")
    lsb.hide("input image.png", message=msg).save("hidden.png")
    print("Message hidden inside 'hidden.png'")
elif choice == "2":
    secret = lsb.reveal("hidden.png")
    print("The hidden message is:", secret)
else:
    print("Invalid choice")