# Brain_cancer_detection_on_Raspberry_Pi

```diff
@@ First check whether git is installed in Rpi3b+@@

! git --version

If this fails with a error message

! sudo apt install git
```

```diff
@@ Clone this repository@@

! git clone https://github.com/Soham-coder/Raspberry_pi_edge_ML.git
```

```diff
@@ Instructions to run@@
```

```diff
@@ Run normal code@@



Go inside directory Normal_arindam

! sudo chmod +x script_normal.sh

! ./script_normal.sh

It will give print "Press pushbutton for predicting images"

Press pushbutton connected to GPIO-15

It will ask for prompt "Enter path of image directory where images are present:"

Give prompt input as ./test_orig

Once all finish, press ctrl+c

Output log - ./log/out.txt
```
<a href="Normal_arindam/log/out.txt">Arindam_log</a>
```diff
+ Average Prediction Time: 5.3895740906397505 Seconds
```







```diff
@@ Run dwt code@@



Go inside directory DWT_pratyay

! sudo chmod +x script_dwt.sh

! ./script_dwt.sh

It will give print "Press pushbutton for predicting images"

Press pushbutton connected to GPIO-15

It will ask for prompt "Enter path of image directory where images are present:"

Give prompt input as ./test_dwt

Once all finish, press ctrl+c

Output log - ./log/out.txt
```
<a href="DWT_pratyay/log/out.txt">Pratyay_log</a>
```diff
+ Average Prediction Time: 0.24476244866847993 Seconds
```