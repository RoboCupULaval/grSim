#!/usr/bin/python

import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 7755


def move_robot(team, id, x, y):

    if team == "yellow":
        id += 6

    MESSAGE = struct.pack("IIff", 1, id, x, y)
    send(MESSAGE)


def move_ball(x, y):

    MESSAGE = struct.pack("Iff", 0, x, y)
    send(MESSAGE)


def move_camera(x, y, z, heading, pitch, roll):

    MESSAGE = struct.pack("Iffffff", 4, x, y, z, heading, pitch, roll)
    send(MESSAGE)

def lock_camera_ball():

    MESSAGE = struct.pack("I", 2)
    send(MESSAGE)


def lock_camera_robot(team, id):

    if team == "yellow":
        id += 6

    MESSAGE = struct.pack("II", 3, id)
    send(MESSAGE)


def send(MESSAGE):

    print("UDP target IP:", UDP_IP)
    print("UDP target port:", UDP_PORT)
    print("message:", MESSAGE)

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def move_to_kickoff():
    for i in range(1, 6):
        move_robot("yellow", i, 20+i, 20+i)
        move_robot("blue", i, 10+i, 10+i)

    move_robot("yellow", 0, 2.5, 0)
    move_robot("blue", 0, -0.5, 0)
    move_robot("blue", 1, -0.5, 1)
    move_robot("blue", 2, -0.5, -1)
    move_ball(0, 0)
    #move_camera(-2, 0, 1, 0, 0, 0)
    #lock_camera_robot("blue", 0)

if __name__ == '__main__':
    move_to_kickoff()
