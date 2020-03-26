import cv2
from glob import glob

root = "predictions"

def visualize(root):
    images = glob(f"{root}/*")
    curr_index = 0
    while curr_index < len(images):
        img_url = images[curr_index]
        img = cv2.imread(img_url)
        img = cv2.resize(img, (1000,500), fx=.5, fy=.5)
        img_pos = curr_index if curr_index>=0 else len(images) + curr_index
        title = f"{img_pos+1}-{img_url}"
        cv2.putText(img, title, (0,20), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,255,0), 1, cv2.LINE_AA)
        cv2.imshow("Image", img)
        k = cv2.waitKeyEx()
        if k == ord('q'): # quit
            break
        elif k == 2555904: # next
            curr_index+=1
        elif k == 2424832: # prev
            curr_index-=1
        else:
            print("Please use only forward[->], backword[<-] and quit[q].")

    cv2.destroyAllWindows()

visualize(root)