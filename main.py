import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import argparse
import cv2
from pathlib import Path


__author__ = "Ben Mussay"


def main():
    parser = argparse.ArgumentParser(description="Defect-Detection in Chips using Image Restoration")
    parser.add_argument("--path", type=str, help="Full path to the defected image")
    args = parser.parse_args()

    print("***** Image Restoration *****")
    print("Written By: {}".format(__author__))
    print(args.path)
    image = cv2.imread(str(Path(args.path)))
    print("Original Image dimensions:")
    print(np.array(image).shape)

    cv2.imshow('Original Image', image)
    cv2.waitKey()
    cv2.destroyAllWindows()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Gray-Scale Image dimensions:")
    print(np.array(image).shape)

    cv2.imshow('Gray Scale Image', image)
    cv2.waitKey()


if __name__ == "__main__":
    main()
