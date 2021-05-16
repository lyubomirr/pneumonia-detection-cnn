# CNN implementation for pneumonia detection using [Chest X-Ray Images dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

In folder `train` is the jupyter notebooks for the two networks I've trained - a regular CNN and one using Transfer Learning with VGG.

Vanilla CNN results:
![cnn result](https://raw.githubusercontent.com/lyubomirr/pneumonia-detection-cnn/main/train/results/vanilla-cnn.PNG)

VGG Transfer Learning results:
![vgg transfer results](https://raw.githubusercontent.com/lyubomirr/pneumonia-detection-cnn/main/train/results/vgg_transfer.PNG)

In `app` is located a simple web application which allows you to upload an image and it classifies it as 'pneumonia' or 'normal'. I haven't uploaded the trained model which the app is using because its too large.
