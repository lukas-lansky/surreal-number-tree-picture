#!/usr/bin/python3

from py2mp import *

startmp()

top = 0.5
lines = []
for j in range(10):
    lines.append([])
    for i in range(20-j):
        if j > 0 and i == 0: top -= 1/(j+1)
        else: top -= (3/5)**j*(7/8)**i
        lines[j].append(top)
        line((-7.5, top), (7.5, top), width=.5, dashed=True)

def textit(wh, pos):
    dicti = {
        "": ("0", "top"),
        "+": ("1", "urt"),
        "++": ("2", "urt"),
        "+++": ("3", "urt"),
        "-": ("-1", "ulft"),
        "-+": ("-{1\over 2}",),
        "--": ("-2", "ulft"),
        "---": ("-3", "ulft"),
        "+-": ("1 \over 2", "lft"),
        "+--": ("1 \over 4", "lft"),
        "+-+": ("3 \over 4",),
        "++-": ("1{1\over 2}",),
        "+-++": ("7\over 8",),
        "+-+-": ("5\over 8",),
        "+--+": ("3\over 8",),
        "+---": ("1\over 8",),
        "+*+": ("\omega+1",),
        "+*-": ("\omega-1","lft"),
        "+*++": ("\omega+2",),
        "+*+-": ("\omega+{1\over 2}", "rt"),
        "-*+": ("2\epsilon",),
        "-*-": ("\epsilon\over 2", "lft"),
        "+*-*+": ("{1\over 2}\omega+1",) }
    if pos in dicti:
        if len(dicti[pos]) == 2:
            text(wh, dicti[pos][0], dicti[pos][1])
        else:
            text(wh, dicti[pos][0])

chwh = dict()
def makeAtree(wh, level, pos, xdiff, father=None, ulevel=0, maxlevel=6, max2level=8):
    chain = None;
    if level > max2level:
        if all(map(lambda c: c==pos[0], pos)):
            chain = "inf" + pos[0]
        elif all(map(lambda c: c==pos[1], pos[1:])) and pos[0]=="+":
            chain = "eps"
        elif all(map(lambda i: pos[i] != pos[i-1], range(2, level))) and pos[:2]=="+-":
            chain = "third"
        elif pos[:4] == "+*+-" and all(map(lambda c: c==pos[3], pos[3:])):
            chain = "infeps"
        elif pos[:5] == "+*-*+" and all(map(lambda c: c=="+", pos[5:])):
            chain = "thrf"

        for i in range(1, 10):
            if pos[:2*i] == "+*"*i and all(map(lambda c: c=="+", pos[2*i:])):
                chain = "inf"+"*"*i
        for i in range(1, 10):
            if pos[:2] == "+*" and pos[2:2*i] == "-*"*(i-1) and all(map(lambda c: c=="-", pos[2*i:])):
                chain = "inf/"+"*"*i

        if chain is not None:
            chwh[chain] = wh
        if chain is None or level > 18-ulevel:
            return

    if level > maxlevel:
        point(wh, width=2)
    else:
        point(wh)
    if father is not None:
        line(father, wh, width=.5 if level>maxlevel else 1)

    textit(wh, pos)

    ycenter = (lines[ulevel][level] + lines[ulevel][level+1])/2
    xcenter = wh[0]

    makeAtree((xcenter-xdiff, ycenter), level+1, pos+"-", xdiff/2, wh, ulevel, maxlevel, max2level)
    makeAtree((xcenter+xdiff, ycenter), level+1, pos+"+", xdiff/2, wh, ulevel, maxlevel, max2level)

makeAtree((-2,0), 0, "", 2.5, ulevel=0, maxlevel=6, max2level=8)
makeAtree(chwh["inf+"], 0, "+*", 1.3, ulevel=1, maxlevel=3, max2level=6)
for q in range(2, 10):
    makeAtree(chwh["inf"+"*"*(q-1)], 0, "+*"*q, .5**q if q>2 else 0.5, ulevel=q, maxlevel=1, max2level=(4 if q<6 else 1))
for q in range(2, 10):
    makeAtree(chwh["inf/"+"*"*(q-1)], 0, "+*"+"-*"*(q-1), .5**q if q>2 else 0.5, ulevel=q, maxlevel=1, max2level=(4 if q<6 else 1))
makeAtree(chwh["eps"], 0, "-*", 0.8, ulevel=1, maxlevel=3, max2level=6)
for cha in chwh:
    point(chwh[cha])
    if cha == "third": text(chwh[cha], "2\over 3", "bot")
    elif cha == "inf+": text((chwh[cha][0], chwh[cha][1]-.1), "\omega", "bot")
    elif cha == "inf-": text(chwh[cha], "-\omega", "bot")
    elif cha == "eps": text((chwh[cha][0], chwh[cha][1]-.1), "\epsilon", "bot")
    elif cha == "inf*": text(chwh[cha], "2\omega", "bot")
    elif cha == "inf**": text(chwh[cha], "3\omega", "lrt")
    elif cha == "inf/*": text(chwh[cha], "{1\over 2}\omega", "bot")
    elif cha == "infeps": text(chwh[cha], "\omega+\epsilon", "bot")
    elif cha == "inf"+"*"*8: text((chwh[cha][0], chwh[cha][1]-.2), "\omega^2", "bot")
    elif cha == "inf/"+"*"*8: text((chwh[cha][0], chwh[cha][1]-.2), "\sqrt{\omega}", "bot") 
    elif cha == "thrf": text(chwh[cha], "{3\over 4}\omega", "bot")
    elif cha == "inf/**": text(chwh[cha], "{1\over 4}\omega", "llft")

endmp()
