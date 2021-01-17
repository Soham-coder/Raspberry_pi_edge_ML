![visitors](https://visitor-badge.glitch.me/badge?page_id=Soham-coder-Raspberry_pi_edge_ML)
# Brain_cancer_detection_on_Raspberry_Pi

```diff
@@ First check whether git is installed in Rpi3b+@@

! git --version

If this fails with a error message install git ...

! sudo apt install git
```


```diff
@@ Clone this repository@@

! git clone https://github.com/Soham-coder/Raspberry_pi_edge_ML.git
```





```diff
@@ Run normal_quantized code@@
Go inside directory Normal_quantized

! sudo chmod +x script_normal.sh

! ./script_normal.sh

It will give print "Press pushbutton for predicting images"

Press pushbutton connected to GPIO-15

It will ask for prompt "Enter path of image directory where images are present:"

Give prompt input as ./test_orig

- Note: Don't press pushbutton until current prediction operation is finished, else it will ask for next prompt

Once all finish, press ctrl+c

Output log - ./log/out.txt
```
<a href="Normal_quantized/log/out.txt">Normal_quantized_log</a>

```diff
+ Average Prediction Time: 5.3895740906397505 Seconds
+ Average Size of test images - 24035 bytes
+ Pre-trained Model Size - 7255312 bytes
+ Accuracy - 97.92% 
```







```diff
@@ Run dwt_quantized code@@
Go inside directory DWT_quantized

! sudo chmod +x script_dwt.sh

! ./script_dwt.sh

It will give print "Press pushbutton for predicting images"

Press pushbutton connected to GPIO-15

It will ask for prompt "Enter path of image directory where images are present:"

Give prompt input as ./test_dwt

- Note: Don't press pushbutton until current prediction operation is finished, else it will ask for next prompt

Once all finish, press ctrl+c

Output log - ./log/out.txt
```
<a href="DWT_quantized/log/out.txt">DWT_quantized_log</a>
```diff
+ Average Prediction Time: 0.24476244866847993 Seconds
+ Average Size of test images - 5894 bytes
+ Pre-trained Model Size - 795552 bytes
+ Accuracy - 95.33%
```



```diff
@@ Run vgg16_quantized code@@
Go inside directory VGG16_quantized

! sudo chmod +x script_vgg16.sh

! ./script_vgg16.sh

It will give print "Press pushbutton for predicting images"

Press pushbutton connected to GPIO-15

It will ask for prompt "Enter path of image directory where images are present:"

Give prompt input as ./test_orig

- Note: Don't press pushbutton until current prediction operation is finished, else it will ask for next prompt

Once all finish, press ctrl+c

Output log - ./log/out.txt
```
<a href="VGG16_quantized/log/out.txt">VGG16_quantized</a>
```diff
+ Average Prediction Time: 30.64683867924249 Seconds
+ Average Size of test images - 24035 bytes
+ Pre-trained Model Size - 18143072 bytes
```








# Accuracy_logs

<a href="Calculate_accuracy/log/normal.txt">Normal_accuracy</a> <br>

<a href="Calculate_accuracy/log/dwt.txt">DWT_accuracy</a>

```diff
@@ Run Accuracy scripts@@
Go inside directory Calculate_accuracy
@@ Run normal accuracy@@
! sudo chmod +x script_accuracy_normal.sh
! ./script_accuracy_normal.sh
Output logs - 
# ./log/normal.txt

@@ Run dwt accuracy@@
! sudo chmod +x script_accuracy_dwt.sh
! ./script_accuracy_dwt.sh
Output logs -
# ./log/dwt.txt

@@ Run cs accuracy@@
! sudo chmod +x script_accuracy_cs.sh
! ./script_accuracy_cs.sh
Output logs - 
# ./log/cs.txt
```


# Final_Report
<a href="https://docs.google.com/document/d/1-opeGVWXdi5GVH5XuO0zO1pk_tW50uZuuCSQMujsFfE/edit">Final Report</a> <br>


# Utility
```diff prompt
### Utility scripts

average_prediction_runtime.py - Parses the log file and calculates average prediction time
find_avg_test_image_size.sh - Calculates the average image size of test images in test image folder in bytes
find_model_size.sh - Calculates the Pretrained model size in weights folder
install_git.sh - Incase you want to install git in Linux-Ubuntu based system through apt package manager, use this
form_dict.py - Creates Dictionary/associative array of "image name" & "category"- Enter prompt as ./test_dwt

```

```diff prompt
install_tf_2_4_0_rpi3b.sh - Install tf==2.4.0 in Rpi 3b+/4 in Debian Raspbian OS
cd Install_tf-2.4.0-armv71-rpi3b
chmod +x install_tf_2_4_0_rpi3b.sh
./install_tf_2_4_0_rpi3b.sh
[Restart the Terminal](needed)

P.S - tf=2.4.0 should get installed in pip3, python3
```

# Project Maintainers 

<table>
  <tr>
    <td align="center"><a href="https://arindam-coder.github.io/Personal-site/"><img src="https://avatars2.githubusercontent.com/u/61356344?s=460&u=7a632344440dfe0fbba3021ab30cd73935024f43&v=4" width="100px;" alt=""/><br /><sub><b>Arindam Majee</b></sub></a></td>
  </tr>
</table>
