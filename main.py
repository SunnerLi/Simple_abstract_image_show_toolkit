from check_keyboard import readKeyCode
import numpy as np
import ear_pen
import cv2

def combineImg(tensor, index, scale=1):
    height, width, channel = np.shape(tensor[0][index])
    img = tensor[0][index]
    img = cv2.resize(img, (width * scale, height * scale))
    for i in range(1, len(tensor)):
        concat_img = tensor[i][index]
        concat_img = cv2.resize(concat_img, (width * scale, height * scale))
        img = np.concatenate((img, concat_img), axis=1)
    return img

def work(tensor, scale=1):
    # Load key code
    left_code, right_code, leave_code = readKeyCode()

    # Examine the shape of each tensor are equal
    for i in range(len(tensor)):
        if np.shape(tensor[i]) != np.shape(tensor[0]):
            print("shape isn't equal, exit...")
            exit()

    # Form initial show image
    counter = 0
    show_img = combineImg(tensor, counter, scale=scale)

    # Show infinitly
    while True:
        cv2.imshow('Pair', show_img)
        action = cv2.waitKey(50)
        if action == left_code:
            if counter == 0:
                counter = len(tensor[0]) - 1
            else:
                counter -= 1
            show_img = combineImg(tensor, counter, scale=scale)
            print('image index: ', counter)
        elif action == right_code:
            if counter == len(tensor[0]) - 1:
                counter = 0
            else:
                counter += 1
            show_img = combineImg(tensor, counter, scale=scale)
            print('image index: ', counter)
        elif action == leave_code:
            break
        else:
            pass

if __name__ == '__main__':
    (train_x, train_y), (test_x, test_y) = ear_pen.load_data()
    print('train shape: ', np.shape(train_x))
    print('test shape: ', np.shape(test_x))
    work([train_x, train_y], scale=2)