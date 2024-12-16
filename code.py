import qrcode

website_link = input("Enter the website link: ")
website_name = input("Enter the website name: ")

qr = qrcode.QRCode(version =1, box_size = 5, border =5)
qr.add_data(website_link)
qr.make()

image = qr.make_image(fill_color = 'black', back_color = 'white',border_width = 5, border_color = 'black')
image.save(f"{website_name}.png")
