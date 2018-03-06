import os, time, threading


def hub():  # Firefox
    os.system('java -jar selenium-server-standalone-2.53.1.jar -role hub')


def node1():  # Chrome
    os.system('java -jar selenium-server-standalone-2.53.1.jar -role node -port 5555')


def node2():  # IE9
    os.system('java -jar selenium-server-standalone-2.53.1.jar -role node -port 5556')


def node3():  # IE
    os.system('java -jar selenium-server-standalone-2.53.1.jar -role node -port 6666')


def node4():  # IE
    os.system('java -jar selenium-server-standalone-2.53.1.jar -role node -port 6667')


def node5():  # IE
    os.system('java -jar selenium-server-standalone-2.53.1.jar -role node -port 6668')


h = threading.Thread(target=hub)
n1 = threading.Thread(target=node1)
n2 = threading.Thread(target=node2)
n3 = threading.Thread(target=node3)
n4 = threading.Thread(target=node4)
n5 = threading.Thread(target=node5)
