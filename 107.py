def drawBox( img,bbox):
	x,y,w,h = int (bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img, (x,y) ,((x+w) , (y+h)) , (255, 0, 255) 3 , 1) 
    cv2 .putText(img,"Tracking" , (75, 90) , cv2. FONT_HERSHEY_SIMPLEX,0.7,, (0, 255.0) ,2)

while True: 
	check, img = video.read() 
success,bbox = tracker.update(img) 

if success: 
	drawBox(img,bbox)
else: 
    cv2.putText(img , "Lost" , (75, 90) ,cv2.FONT_HERSHEY_SIMPLEX,0. 7, (0, 0 ,255) ,2)

key = cv2.waitKey(1) 
if key == ord('q'):
	print( " Closing " ) 
break 