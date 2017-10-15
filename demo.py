import numpy as np
import ear_pen
import tool

if __name__ == '__main__':
    (train_x, train_y), (test_x, test_y) = ear_pen.load_data()
    print('train shape: ', np.shape(train_x))
    print('test shape: ', np.shape(test_x))
    tool.work([train_x,])