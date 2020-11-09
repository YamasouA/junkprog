import cv2
import matplotlib.pyplot as plt
import numpy as np

def alpha_blend(img, img2, alpha):
    #blend
    out = img * alpha + img2 * (1 - alpha)
    out = out.astype(np.uint8)
    return out

#Read image
img = cv2.imread("./image/12.png").astype(np.float32)
img2 = cv2.imread("./image/13.png").astype(np.float32)
img = cv2.resize(img, (800, 600))
img2 = cv2.resize(img2, (800, 600))
out = alpha_blend(img, img2, alpha=0.5)

#save result
cv2.imwrite("./image/out.jpg", out)
cv2.imshow("img1", img)
cv2.imshow("img2", img2)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
