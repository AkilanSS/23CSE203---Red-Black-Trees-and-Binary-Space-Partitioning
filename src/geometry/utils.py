

from src.geometry.line import Line

def classify_point(pt,line):
    (x1,y1)=line.start_pos
    (x2,y2)=line.end_pos
    (px,py)=pt

    d=(x2-x1)*(py-y1)-(y2-y1)*(px-x1)

    if abs(d)<1e-6:
        return "on"
    elif d>0:
        return "front"
    else:
        return "back"
    
def classify_line(div,line):
    side1=classify_point(line.start_pos,div)
    side2=classify_point(line.end_pos,div)

    if side1=="on" and side2=="on":
        return "on"
    elif side1 in ("front","on") and side2 in ("front","on"):
        return "front"
    elif side1 in ("back","on") and side2 in ("back","on"):
        return "back"
    else:
        return "spanning"
    
def split_line(div,line):

    x1,y1=div.start_pos
    x2,y2=div.end_pos
    x3,y3=line.start_pos
    x4,y4=line.end_pos

    denominator= (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    numerator=(x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)

    if abs(denominator)<1e-6:
        return line,None


    t=numerator/denominator

    xi= x1 + t*(x2-x1)
    yi= y1 + t*(y2-y1)
    intersection=(xi,yi)

    start=classify_point(line.start_pos,div)

    if start in ("front","on"):
        front = Line(line.start_pos,intersection,line.color,line.width,line.layer)
        back  = Line(intersection,line.end_pos,line.color,line.width,line.layer)
    else:
        front = Line(intersection,line.end_pos,line.color,line.width,line.layer)
        back  = Line(line.start_pos,intersection,line.color,line.width,line.layer)
    
    return front,back


    
