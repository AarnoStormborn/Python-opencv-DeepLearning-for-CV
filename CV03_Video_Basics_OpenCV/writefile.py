import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter('myvideo.avi', -1, 20, (w,h))

while True:

    ret, frame = cap.read()
    
    writer.write(frame)

    frame = cv2.flip(frame, 1)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) &0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()