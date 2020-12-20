#!/usr/bin/python
#coding: UTF-8
#open source
#created by Tegar ID
#silahkan di pelajari:)

#import module
import pytube
from pytube import YouTube as yutub
from time import sleep
from terminaltables import SingleTable as tabel
from os import system as _

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"    # kode warna
B = "\033[1;34m"
P = "\033[1;35m"
C = "\033[1;36m"
W = "\033[1;37m"
O = "\033[0m"
RB = "\033[1;41m"


# banner
logo = """
\t{}██████╗░██╗░░██╗████████╗██╗░░░██╗
\t██╔══██╗██║░██╔╝╚══██╔══╝╚██╗░██╔╝
\t██║░░██║█████═╝░░░░██║░░░░╚████╔╝░
\t{}██║░░██║██╔═██╗░░░░██║░░░░░╚██╔╝░░
\t██████╔╝██║░╚██╗░░░██║░░░░░░██║░░░
\t╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░
\t      {}[{} DK TOOLS YOUTUBE {}{}]

{}Creator {}: {}Tegar ID
{}Versi   {}: {}0.1
""".format(R,W,W,RB,O,W,C,W,Y,C,W,Y)

# aktivitas download video
def youtube():
    try:
        yt = yutub(link)
        print("\n{}* {}Judul Vidio {}= {}".format(Y,B,W,G)+yt.title)
        sleep(1)
        print("{}* {}ID Vidio {}= {}".format(Y,B,W,G)+yt.video_id)
        sleep(1)
        print("{}* {}Durasi Vidio(s) {}={}".format(Y,B,W,G),yt.length)
        sleep(1)
        print("{}* {}Viewer Vidio {}={}".format(Y,B,W,G),yt.views)
        sleep(1)
        print("{}* {}Rating Vidio {}={}".format(Y,B,W,G),yt.rating)
        sleep(1)
        print("{}* {}Batasan Usia {}={}".format(Y,B,W,G),yt.age_restricted)
        sleep(1)
        print("{}* {}Deskripsi {}= {}\n".format(Y,B,W,G))
        data = [
            [''+yt.description],
            ]
        table = tabel(data)
        print(table.table)
        sleep(1)
    except KeyboardInterrupt:
        exit()
    except Exception:
        sleep(1)
        print("{}[{}!{}] {}Link Invalid, periksa lagi link yang anda masukan".format(W,R,W,R))
        _("python yt.py")

    choice = input("{}* {}Apakah anda mau mendownload nya? (y/n) {}: {}".format(Y,B,W,G))
    for i in choice:
        if i == "y" or i == "Y":
            continue
        else:
            exit()
            _("clear")
            print("{}Keluar Program".format(B))
            sleep(1)
    try:
        resu = input("\n{}* {}Kualitas tinggi(H)/Kualitas rendah(L) (H/L) : {}".format(Y,B,W,G))
    except KeyboardInterrupt:
        exit()

    if resu == "H" or resu == "h":
        print(G)
        print(_("pytube {} -t /sdcard --itag=22".format(link)))
        print(O)
    elif resu == "L" or resu == "l":
        print(G)
        print(_("pytube {} -t /sdcard --itag=18".format(link)))
        print(O)
    else:
        exit()

if __name__ == "__main__":
    _("clear")
    print(logo)
    print(50*"{}=".format(G))
    link = input("{}* {}Link Youtube {}= {}".format(Y,B,W,R))
    print(50*"{}=".format(G))
    youtube()
