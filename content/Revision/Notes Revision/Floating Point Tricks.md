# Floating Point Tricks

Created: May 14, 2023 6:10 PM

![Untitled](Revision/Notes%20Revision/media/Untitled%204.png)

1. ************************************************************Calculate the Exponent Based so Fast************************************************************

******M =****** 10000011 

subtract by 128 (remove the MSB) ⇒ 11
then add 1 ⇒ 11 + 1 ⇒ 100

anwser ⇒ 4

1. **********************Convert Binary to Decimal so Fast**********************
    1. e.g. 100000011
        1. digit after the first MSB is 8 ⇒ 2^8 ⇒ 256
        digit after the add the 11 ⇒ 256 + 3 ⇒ 259