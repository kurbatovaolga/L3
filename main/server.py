
import socket

import cv2
import pickle
import numpy as np
import struct
import zlib
from flask_opencv_streamer.streamer import Streamer

HOST=''
PORT = 8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(1)
print('Socket now listening')

conn,addr=s.accept()

MASK = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

port = 8080
require_login = False
streamer = Streamer(port, require_login)

video_capture = cv2.VideoCapture('http://cam1.infolink.ru/mjpg/video.mjpg') #193/123/226/39 - камера с сайта, который дал Кузнецов
while True:
    _, frame = video_capture.read()

    frame = cv2.medianBlur(frame, 3)
    frame = cv2.filter2D(frame, -1, MASK)
    _, frame = cv2.threshold(frame, 10, 255, cv2.THRESH_BINARY_INV)
    streamer.update_frame(frame)

    if not streamer.is_streaming:
        streamer.start_streaming()
    # было в примере, но вроде и без этого работает
    # cv2.waitKey(30)





#  здесь код твоего друга
#  HOST=''
# PORT = 8485
#
# port1 = 8090
# port2 = 8091
# port3 = 8092
# require_login = False
#
# streamer1 = Streamer(port1, require_login)
# streamer2 = Streamer(port2, require_login)
# streamer3 = Streamer(port3, require_login)
#
#
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print('Socket created')
#
# s.bind((HOST,PORT))
# print('Socket bind complete')
# s.listen(1)
# print('Socket now listening')
#
# conn,addr=s.accept()
#
# print('Connected with' + str(addr))
# def detectPeople(gray):
#     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#     #face_cascade = cv2.CascadeClassifier('hand.xml')
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10))
#     for (x, y, w, h) in faces:
#         cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 0), 2)
#         cv2.putText(gray, "Ya vas kategori4eski privetstvuyu", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (30, 105, 210), 1)
#
# def detectCat(gray):
#     face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
#     for (x, y, w, h) in faces:
#         cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 0), 2)
#         cv2.putText(gray, "Cat", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 3, (30, 105, 210), 6)
#
#
#
# payload_size = struct.calcsize(">L")
# print("payload_size: {}".format(payload_size))
# data = b""
#
# while True:
#     while len(data) < payload_size:
#         data += conn.recv(4096)
#
#     #print("Done Recv: {}".format(len(data)))
#     packed_msg_size = data[:payload_size]
#     data = data[payload_size:]
#     msg_size = struct.unpack(">L", packed_msg_size)[0]
#     #print("msg_size: {}".format(msg_size))
#     while len(data) < msg_size:
#         data += conn.recv(4096)
#     frame_data = data[:msg_size]
#     data = data[msg_size:]
#     frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
#     frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
#     detectPeople(frame)
#     #detectCat(frame)
#     streamer1.update_frame(frame)
#     streamer2.update_frame(frame)
#     #streamer3.update_frame(frame)
#
#     if not streamer1.is_streaming:
#         streamer1.start_streaming()
#
#     if not streamer2.is_streaming:
#         streamer2.start_streaming()
#
#     #if not streamer3.is_streaming:
#     #    streamer3.start_streaming()
#     #cv2.imshow('ImageWindow',frame)
#     cv2.waitKey(30)