import numpy as np
import getch
import cv2

def saveKeyCode():
    img = np.zeros([100, 700, 3])
    cv2.putText(img, "press left key...(Don't press q)", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
    cv2.imshow(' ', img)
    left_code = cv2.waitKey(0)

    img = np.zeros([100, 700, 3])
    cv2.putText(img, "press right key...(Don't press q)", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
    cv2.imshow(' ', img)
    right_code = cv2.waitKey(0)

    img = np.zeros([100, 700, 3])
    cv2.putText(img, "press q...", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
    cv2.imshow(' ', img)
    leave_code = cv2.waitKey(0)

    print('left code: ', left_code, '\tright code: ', right_code, '\tleave code: ', leave_code)
    with open('keycode.dat', 'w') as f:
        f.write(str(left_code) + '\n' + str(right_code) + '\n' + str(leave_code))

def readKeyCode(path='./keycode.dat'):
    string = open(path, 'r').read().split('\n')
    return int(string[0]), int(string[1]), int(string[2])

if __name__ == '__main__':
    saveKeyCode()