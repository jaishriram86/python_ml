
import cv2
import easyocr
import matplotlib.pyplot as plt

cam=cv2.VideoCapture(0)
cv2.namedWindow("Webcam")

img_counter=0
while (img_counter!=1):
    no_frame,frame=cam.read()
    if (not no_frame):
        print("Failed to grab frame")
        break
    cv2.imshow("LIVE",frame)

    k=cv2.waitKey(1)

    if (k%256==113):
        print("\nQuit hit...Closing the app\n")
        break

    elif (k%256==32):
        img_name="IMG_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("\nScreenshot Taken\n")
        img_counter+=1  

img=cv2.imread(img_name)

reader=easyocr.Reader(['en'],gpu=False)

text_=reader.readtext(img)

passed=0
if (len(text_)==0):
    print("Cannot Recognize the image...Please capture it properly")
else:
    print("Successfully Text found...\n")

    passed=1
    extracted_text = ""
    for t in text_:
        print(t)
        bbox, text, score = t
        extracted_text += text + "\n"
        
        cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 2)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,0,0), 1)

    with open("textFound.txt", "w", encoding="utf-8") as file:
        file.write(extracted_text)
    print("Text saved in textFound.txt")
        
if(passed==1):
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show()