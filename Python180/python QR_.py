# movies=[]
# mov1=input("Enter first movi:")
# mov2=input("Enter second movi:")
# mov3=input("Enter 3th movies:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)
import qrcode

# Define data to be encoded in the QR code
data = "https://www.linkedin.com/in/ayush-website205822248/"

# Generate QR code
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image or display it
img.save("example_qrcode.png")  # Save the image
img.show()  # Display the image
