import cv2
import time
x1=0
x2=20
y1=0
y2=20

negx1=1
negx2=1
negx3=1
negx4=1

l1=679
l2=699
m1=0
m2=20

negl1=1
negl2=1
negl3=1
negl4=1

a1=300
b1=679
a2=320
b2=699

nega1=1
nega2=1
nega3=1
nega4=1

p1=679
p2=699
q1=679
q2=699

negp1=1
negp2=1
negp3=1
negp4=1

u1=300
u2=320
v1=0
v2=20

negu1=1
negu2=1
negu3=1
negu4=1

negu1=1
negu2=1
negu3=1
negu4=1

e1=0
e2=20
f1=300
f2=320

nege1=1
nege2=1
nege3=1
nege4=1

c1=679
c2=699
d1=300
d2=320

negc1=1
negc2=1
negc3=1
negc4=1

r1=679
r2=699
s1=300
s2=320

negr1=1
negr2=1
negr3=1
negr4=1



cap=cv2.VideoCapture(0)
while True:
    success,frame=cap.read()
    frame = cv2.resize(frame, (700, 700))
    x1+=1*negx1
    x2+=1*negx2
    y1+=2*negx3
    y2+=2*negx4

    p1+=1*negp1
    p2+=1*negp2
    q1+=2*negp3
    q2+=2*negp4    

    a1+=2*nega1
    a2+=2*nega2
    b1+=1*nega3
    b2+=1*nega4

    l1+=1*negl1
    l2+=1*negl2
    m1+=2*negl3
    m2+=2*negl4
 
    u1+=1*negu1
    u2+=1*negu1
    v1+=2*negu3
    v2+=2*negu4

    e1+=2*nege1
    e2+=2*nege1
    f1+=1*nege3
    f2+=1*nege4

    c1+=2*negc1
    c2+=2*negc1
    d1+=1*negc3
    d2+=1*negc4

    r1+=1*negr1
    r2+=1*negr2
    s1+=2*negr3
    s2+=2*negr4

    if y2>699 or y1<0 :
        negx3*=-1
        negx4*=-1
        '''while True:
            x1+=1
            x2+=1
            y1+=1
            y2+=1
            cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,150),3)
            cv2.imshow("image",frame)
            if(y2>699):
                break
            looping it this way makes the program really fast'''
        
    if x2>699 or x1<0 :
        negx1*=-1
        negx2*=-1

    if b2>699 or b1<0 :
        nega3*=-1
        nega4*=-1
    if a2>699 or a1<0 :
        nega1*=-1
        nega2*=-1

    if q2>699 or q1<0:
        negp3*=-1
        negp4*=-1
    
    if p1<0 or p2>699:
        negp1*=-1
        negp2*=-1

    if l1<0 or l2>699:
        negl1*=-1
        negl2*=-1

    if m1<0 or m2>699:
        negl3*=-1
        negl4*=-1
        
    if u1<0 or u2>699:
        negu1*=-1
        negu2*=-1

    if v1<0 or v2>699:
        negu3*=-1
        negu4*=-1

    if e1<0 or e2>699:
        nege1*=-1
        nege2*=-1

    if f1<0 or f2>699:
        nege3*=-1
        nege4*=-1

    if c1<0 or c2>699:
        negc1*=-1
        negc2*=-1

    if d1<0 or d2>699:
        negc3*=-1
        negc4*=-1
    
    if r1<0 or r2>699:
        negr1*=-1
        negr2*=-1

    if s1<0 or s2>699:
        negr3*=-1
        negr4*=-1

    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,150),3)
    cv2.rectangle(frame,(a1,b1),(a2,b2),(255,20,0),3)
    cv2.rectangle(frame,(p1,q1),(p2,q2),(0,0,255),3)
    cv2.rectangle(frame,(l1,m1),(l2,m2),(0,255,0),3)
    cv2.rectangle(frame,(u1,v1),(u2,v2),(255,255,255),3)
    cv2.rectangle(frame,(e1,f1),(e2,f2),(0,100,255),3)
    cv2.rectangle(frame,(c1,d1),(c2,d2),(0,255,155),3)
    cv2.rectangle(frame,(r1,s1),(r2,s2),(0,0,0),3)
    cv2.imshow("image",frame)

    cv2.putText(frame,"Bouncing boxes",(260,50),cv2.FONT_HERSHEY_PLAIN,1.5,(255,255,255),3)
    
    
    
    if cv2.waitKey(1)==ord("q"):
        cap.release()
        break

cv2.destroyAllWindows()