# import cv2
# import io
# import socket
# import struct
# import time
# import pickle
# import zlib
#
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('localhost', 8080))
# #connection = client_socket.makefile('wb')
#
# cam = cv2.VideoCapture(1)
#
# cam.set(3, 360);
# cam.set(4, 360);
#
#
# encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
# img_counter = 0
# while True:
#     ret, frame = cam.read()
#     result, frame = cv2.imencode('.jpg', frame, encode_param)
#     data = pickle.dumps(frame, 0)
#     size = len(data)
#     print("{}: {}".format(img_counter, size))
#     img_counter += 1
#     client_socket.sendall(struct.pack(">L", size) + data)
#     #client_socket.sendall(data)
#
# cam.release()