import io
from PIL import Image


def numpy_to_img(numpy_img):
    img = Image.fromarray(numpy_img)
    img_byte_arr = io.BytesIO()

    img.save(img_byte_arr, format="JPEG")

    return img_byte_arr.getvalue()

    # return imencode(".jpeg", numpy_img)[1].tostring()
