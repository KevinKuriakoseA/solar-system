import cv2 

img = cv2.imread("solar-system.jpg")



cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Mercury",
            (90,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Venus",
            (216,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Earth",
            (288,144),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Mars",
            (387,165),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Jupiter",
            (551,374),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Saturn",
            (764,106),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Uranus",
            (963,281),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Neptune",
            (1118,281),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.imshow('output',img)
cv2.waitKey(0)
