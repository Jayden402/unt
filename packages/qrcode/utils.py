import qrcode


def make_qrcode(name, url):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    # img.save(name)
    path = f"D://ubuntu/unt/static{name}"
    img.save(path)
    f = open(path, 'rb')
    pic_data = f.read()
    return pic_data
