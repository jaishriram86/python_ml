import cv2
import pytesseract as pyt

cam = cv2.VideoCapture(0)
cv2.namedWindow("Webcam")

img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame\n")
        break
    cv2.imshow("webcam LIVE", frame)

    k = cv2.waitKey(1)

    # press q to exit webcam
    if k % 256 == 113: 
        print("Quit hit...Closing the app\n")
        break

    # press space bar to capture image
    elif k % 256 == 32:
        img_name = "open_frame{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Screenshot Taken\n")
        img_counter += 1    
        if img_counter == 1:
            break    

img = cv2.imread(img_name)
pyt.pytesseract.tesseract_cmd = "C:\\Users\\ms867\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
text = pyt.image_to_string(img)

if text.strip() == "":
    print("Cannot Recognize the image...Please capture it properly")
else:
    print("Successfully Text found...\n")
    print(text)

    with open("textFound.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print("Text saved in textFound.txt")

cam.release()
