import cv2
import os
import matplotlib.pyplot as plt

def get_roi(filename):
    img = cv2.imread(filename)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    x, y = img_gray.shape[0:2]
    ret1, th1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_pre_1 = 255 - th2
    contours, hierarchy = cv2.findContours(img_pre_1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    ROI_IMAGS = []
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
        if (x_list[-1] - x_list[0]) > 50:
            continue
        #cv2.rectangle(img, p1, p2, (255, 0, 0), 2)
        print("x_min {}, x_max {}, y_min {}, y_max {}".format(x_list[0], x_list[-1], y_list[0], y_list[-1]))
        roi_img = img_gray[y_list[0]: y_list[-1], x_list[0]: x_list[-1]]
        ROI_IMAGS.append(roi_img)

    return ROI_IMAGS

if __name__ == '__main__':
    paths = os.walk(r'C:\Users\juhao\Downloads\jietu_type1\jietu')
    image_paths = []
    for path, dir_lst, file_lst in paths:
        for file_name in file_lst:
            image_paths.append(os.path.join(path, file_name))

    index = 0
    for one_image in image_paths:
        images = get_roi(one_image)
        for ele in images:
            index = index + 1
            cv2.imwrite("data_type1/roi_{}.png".format(index), ele)
            print(one_image)
