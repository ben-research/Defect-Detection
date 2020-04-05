import numpy as np
import argparse
import cv2
from pathlib import Path
import matplotlib.pyplot as plt
from tqdm import tqdm

__author__ = "Ben Mussay"


def main():
    parser = argparse.ArgumentParser(description="Defect-Detection in Chips using Image Restoration")
    parser.add_argument("--path-inspect", type=str, help="Full path to the defected image_3d")
    parser.add_argument("--path-reference", type=str, help="Full path to the reference image_3d")
    args = parser.parse_args()

    print("***** Image Restoration *****")
    print("Written By: {}".format(__author__))
    image_3d = cv2.imread(str(Path(args.path_inspect)))
    print("Defected Image dimensions:")
    print(np.array(image_3d).shape)

    image_3d_reference = cv2.imread(str(Path(args.path_reference)))
    print("Reference Image dimensions:")
    print(np.array(image_3d_reference).shape)

    cv2.imshow('Defected Image', image_3d)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.imshow('Defected Image', image_3d_reference)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # convert 3-d image to 1-d image
    image_2d = cv2.cvtColor(image_3d, cv2.COLOR_BGR2GRAY)
    image_2d_reference = cv2.cvtColor(image_3d_reference, cv2.COLOR_BGR2GRAY)


if __name__ == "__main__":
    main()
