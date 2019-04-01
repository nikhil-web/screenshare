import cv2

class VideoCamera_two(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        # self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.video = cv2.VideoCapture('12.mkv')
        
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        quality = 50 # quality 0 to 100. default:95
        ret, jpeg = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        return jpeg.tobytes()
