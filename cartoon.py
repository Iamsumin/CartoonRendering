import cv2
import numpy as np

def cartoonify_image(image_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("이미지를 불러올 수 없습니다.")
        return

    img = cv2.resize(img, (600, 600))

    img_color = cv2.bilateralFilter(img, d=9, sigmaColor=100, sigmaSpace=100)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_edges = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, blockSize=11, C=5)

    img_cartoon = cv2.bitwise_and(img_color, img_color, mask=img_edges)

    cv2.imwrite(output_path, img_cartoon)

    cv2.imshow("Cartoon Image", img_cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cartoonify_image("cartoon1.jpg", "cartoon_output1.jpg")
#cartoonify_image("cartoon2.jpg", "cartoon_output2.jpg")
