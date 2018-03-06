import os, time, threading


def kill():  # Firefox
    os.system('taskkill /f /im java.exe')
