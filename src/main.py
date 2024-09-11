import argparse
import cv2


def main():
    parser = argparse.ArgumentParser(
        description="Simple point and click and record coordinates in image"
    )
    parser.add_argument("path", help="Description for foo argument")
    args = parser.parse_args()

    # image path
    image_path = args.path
    image = cv2.imread(image_path)

    cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
