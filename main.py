import cv2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # 读取文件
    img = cv2.imread("data/type_3/2.png")
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    x, y = img_gray.shape[0:2]
    img = cv2.resize(img, (10 * y, 10 * x))
    img_gray = cv2.resize(img_gray, (10 * y, 10 * x))

    # 二值化
    ## 简单滤波
    ret1, th1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    ## Otsu 滤波
    ret2, th2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 黑白反转
    img_pre_1 = 255 - th2

    # 寻找轮廓
    contours, hierarchy = cv2.findContours(img_pre_1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # 找矩形
    for contour in contours:
        x_list = []
        y_list = []
        for ps in contour:
            for p in ps:
                x_list.append(int(list(p)[0]))
                y_list.append(int(list(p)[1]))
        x_list.sort()
        y_list.sort()


        p1 = (x_list[0], y_list[0])
        p2 = (x_list[-1], y_list[-1])
        cv2.rectangle(img, p1, p2, (255, 0, 0), 2)

    cv2.imshow("二值化", img)
    cv2.waitKey(-1)