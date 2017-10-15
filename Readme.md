## Simple Abstract Image Show Toolkit

This toolkit can let you see the image and annotation directly. You can just use `left` or `right` keyboard to see the each image with convenience.    

Usage
---
First, you should set up which are the control keys. For example, you choose `.` key as left key and `/` key as right key. Notice the `q` key is escaping which you cannot set it as direction key.

```
$ python check_keyboard.py
# Press `.`, `/` and `q` on keyboard inorder
```

Second, you should load your tensor and use the `work` function:
```python
>> import numpy as np
>> images, annotations = load_images()   # You should load your data by yourself
>> np.shape(tensor)
[batch_num, height_num, width_num, channel_num]

>> work([images,])                       # Show the image

>> work([images,annotations])            # Show the image and annotation parallelly

>> work([images,], scale=2)              # Show the image with shrink 2 times
```

Requirement
---
Opencv

Data
---
This toolkit use [Ear-Pen](https://github.com/SunnerLi/Ear-Pen) data repository as example. You should refer the introduction of that repo to see how to deal with the tensor first ([generate the data](https://github.com/SunnerLi/Ear-Pen/tree/master/generate) and [put the essential code and file into current folder](https://github.com/SunnerLi/Ear-Pen/tree/master/load)).    