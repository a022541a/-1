import numpy as np
import cv2

def img_process(img,lower,upper):
    """根据阈值处理图像，提取阈值内的颜色。返回处理后只留下指定颜色的图像（其余为黑色）
        img：原图像；lower：最低阈值；upper：最高阈值"""
    kernel = np.ones((35, 35), np.uint8)
    YUV = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    Y,U,V = cv2.split(YUV)
    #print(U)
    Open = cv2.morphologyEx(U,cv2.MORPH_OPEN,kernel)
    mask = cv2.inRange(Open, lower, upper)
    res = cv2.bitwise_and(img, img, mask = mask)
    return res
def nothing(a):
    pass




if __name__ == '__main__':
    cap = cv2.VideoCapture('text.mp4')
    a=0
    x=0
    upper_u = np.array([255])
    b = 11
    cv2.namedWindow('frame')
    cv2.createTrackbar('U_less', 'frame', 0, 255, nothing)
    cv2.createTrackbar('size', 'frame', 1, 100, nothing)


    while cap.isOpened():
        lower_u = np.array([x])
        ret, frame = cap.read()

        if ret:
            if  a % 5 == 0:
                w,h = frame.shape[0:2]
                print(h,w)
                lower_u = np.array([x])
                img_1 = img_process(frame, lower_u, upper_u)
                if b > 1:
                    img_2 = cv2.resize(img_1, (int(h / b * 10), int(w / b * 10)))
                    img_1 = cv2.resize(img_2, (h, w))
                cv2.imshow('frame' , img_1)
                x = cv2.getTrackbarPos('U_less', 'frame')
                b = cv2.getTrackbarPos('size', 'frame')
                if cv2.waitKey(50) & 0xFF == ord('q'):
                    break
            a += 1

        else:
            break

    cap.release()
    cv2.destoryAllwindows()
