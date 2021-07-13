from cv2 import imencode

def numpy_to_img(numpy_img):
    return imencode(".jpeg", numpy_img)[1].tostring()