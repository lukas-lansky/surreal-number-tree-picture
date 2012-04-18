def line(fro, to, width=1, dashed=False):
    print("pickup pencircle scaled {}pt;".format(width))
    print("draw ({:.4f}u, {:.4f}u)--({:.4f}u, {:.4f}u){};".format(fro[0], fro[1], to[0], to[1], " dashed evenly" if dashed else ""))

def point(wh, width=4):
    print("pickup pencircle scaled {}pt;".format(width))
    print("draw ({:.4f}u, {:.4f}u);".format(wh[0], wh[1]))

def text(wh, tex, dire="rt"):
    print("label.{}(btex ${}$ etex, ({:.4f}u, {:.4f}u));".format(dire, tex, wh[0], wh[1]))

def startmp():
    print("prologues:=3;")
    print('filenametemplate "%j-%c.mps";')
    print("beginfig(1);")
    print("u:=1cm;")

def endmp():
    print("endfig;")
    print("bye;")
