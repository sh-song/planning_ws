;; Auto-generated. Do not edit!


(when (boundp 'new_gigacha::Local)
  (if (not (find-package "NEW_GIGACHA"))
    (make-package "NEW_GIGACHA"))
  (shadow 'Local (find-package "NEW_GIGACHA")))
(unless (find-package "NEW_GIGACHA::LOCAL")
  (make-package "NEW_GIGACHA::LOCAL"))

(in-package "ROS")
;;//! \htmlinclude Local.msg.html


(defclass new_gigacha::Local
  :super ros::object
  :slots (_x _y _heading ))

(defmethod new_gigacha::Local
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:heading __heading) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _heading (float __heading))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:heading
   (&optional __heading)
   (if __heading (setq _heading __heading)) _heading)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _heading
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _heading
       (sys::poke _heading (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _heading
     (setq _heading (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get new_gigacha::Local :md5sum-) "bc1dd36b5547fef69e6daa06ae2e13ac")
(setf (get new_gigacha::Local :datatype-) "new_gigacha/Local")
(setf (get new_gigacha::Local :definition-)
      "float64 x
float64 y
float64 heading
")



(provide :new_gigacha/Local "bc1dd36b5547fef69e6daa06ae2e13ac")


