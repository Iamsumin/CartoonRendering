import cv2
import numpy as np

def cartoonify_image(image_path, output_path):
    # 이미지 읽기
    img = cv2.imread(image_path)
    if img is None:
        print("이미지를 불러올 수 없습니다.")
        return

    # 이미지 리사이즈 (선택 사항)
    img = cv2.resize(img, (800, 600))

    # 스무딩을 위한 블러 적용
    img_color = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # 그레이스케일 변환
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 엣지 검출 (adaptive threshold)
    img_edges = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, blockSize=9, C=2)

    # 컬러 이미지와 엣지를 합쳐서 만화 스타일 생성
    img_cartoon = cv2.bitwise_and(img_color, img_color, mask=img_edges)

    # 결과 저장
    cv2.imwrite(output_path, img_cartoon)

    # 결과 출력
    cv2.imshow("Cartoon Image", img_cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 실행 예제
cartoonify_image("input.jpg", "cartoon_output.jpg")
