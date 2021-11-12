;; Auto-generated. Do not edit!


(when (boundp 'new_gigacha::Serial_Info)
  (if (not (find-package "NEW_GIGACHA"))
    (make-package "NEW_GIGACHA"))
  (shadow 'Serial_Info (find-package "NEW_GIGACHA")))
(unless (find-package "NEW_GIGACHA::SERIAL_INFO")
  (make-package "NEW_GIGACHA::SERIAL_INFO"))

(in-package "ROS")
;;//! \htmlinclude Serial_Info.msg.html


(defclass new_gigacha::Serial_Info
  :super ros::object
  :slots (_auto_manual _emergency_stop _gear _speed _steer _brake _encoder ))

(defmethod new_gigacha::Serial_Info
  (:init
   (&key
    ((:auto_manual __auto_manual) 0)
    ((:emergency_stop __emergency_stop) 0)
    ((:gear __gear) 0)
    ((:speed __speed) 0.0)
    ((:steer __steer) 0.0)
    ((:brake __brake) 0)
    ((:encoder __encoder) 0.0)
    )
   (send-super :init)
   (setq _auto_manual (round __auto_manual))
   (setq _emergency_stop (round __emergency_stop))
   (setq _gear (round __gear))
   (setq _speed (float __speed))
   (setq _steer (float __steer))
   (setq _brake (round __brake))
   (setq _encoder (float __encoder))
   self)
  (:auto_manual
   (&optional __auto_manual)
   (if __auto_manual (setq _auto_manual __auto_manual)) _auto_manual)
  (:emergency_stop
   (&optional __emergency_stop)
   (if __emergency_stop (setq _emergency_stop __emergency_stop)) _emergency_stop)
  (:gear
   (&optional __gear)
   (if __gear (setq _gear __gear)) _gear)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:steer
   (&optional __steer)
   (if __steer (setq _steer __steer)) _steer)
  (:brake
   (&optional __brake)
   (if __brake (setq _brake __brake)) _brake)
  (:encoder
   (&optional __encoder)
   (if __encoder (setq _encoder __encoder)) _encoder)
  (:serialization-length
   ()
   (+
    ;; int16 _auto_manual
    2
    ;; int16 _emergency_stop
    2
    ;; int16 _gear
    2
    ;; float32 _speed
    4
    ;; float32 _steer
    4
    ;; int16 _brake
    2
    ;; float32 _encoder
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _auto_manual
       (write-word _auto_manual s)
     ;; int16 _emergency_stop
       (write-word _emergency_stop s)
     ;; int16 _gear
       (write-word _gear s)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _steer
       (sys::poke _steer (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int16 _brake
       (write-word _brake s)
     ;; float32 _encoder
       (sys::poke _encoder (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _auto_manual
     (setq _auto_manual (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _emergency_stop
     (setq _emergency_stop (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _gear
     (setq _gear (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _steer
     (setq _steer (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int16 _brake
     (setq _brake (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _encoder
     (setq _encoder (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get new_gigacha::Serial_Info :md5sum-) "f14c0811292ee3221e383efec3a1d50e")
(setf (get new_gigacha::Serial_Info :datatype-) "new_gigacha/Serial_Info")
(setf (get new_gigacha::Serial_Info :definition-)
      "int16 auto_manual
int16 emergency_stop
int16 gear
float32 speed
float32 steer
int16 brake
float32 encoder
")



(provide :new_gigacha/Serial_Info "f14c0811292ee3221e383efec3a1d50e")


