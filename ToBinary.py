# -*- coding:utf-8 -*-
# 将彩色图片阈值化，转为单通道图片
# 探讨是否会将模型准确率提升
import argparse
import logging
import os
import cv2
logging.basicConfig(level=logging.INFO)

def ToBinary(image_src, image_dest):
    img = cv2.imread(image_src)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret1, th1 = cv2.threshold(img_gray, 120, 255, cv2.THRESH_TOZERO_INV)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_pre_1 = 255 - th2
    cv2.imshow("show", img_pre_1)
    cv2.imwrite(image_dest, img_pre_1)
    cv2.waitKey(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--src_path", type=str, required=True)
    parser.add_argument("--dest_path", type=str, required=True)
    args = parser.parse_args()

    logging.info("src_path: {}".format(args.src_path))
    logging.info("dest_path: {}".format(args.dest_path))

    if not os.path.exists(args.src_path):
        logging.error("src_path {} is not exist".format(args.src_path))
        exit(0)


    paths = os.walk(args.src_path)
    for path, dir_lst, file_lst in paths:
        dest_sub_path = path.replace(args.src_path, args.dest_path)
        if not os.path.exists(dest_sub_path):
            os.mkdir(dest_sub_path)
            logging.info("Path: {} is not exist, So create it".format(dest_sub_path))

        for file_name in file_lst:
            if file_name.endswith(".png") or file_name.endswith(".jpg"):
                image_src = os.path.join(path, file_name)
                image_dest = os.path.join(dest_sub_path, file_name)
                ToBinary(image_src, image_dest)
                logging.info("{} -> {}".format(image_src, image_dest))
