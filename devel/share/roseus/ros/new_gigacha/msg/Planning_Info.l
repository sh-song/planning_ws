;; Auto-generated. Do not edit!


(when (boundp 'new_gigacha::Planning_Info)
  (if (not (find-package "NEW_GIGACHA"))
    (make-package "NEW_GIGACHA"))
  (shadow 'Planning_Info (find-package "NEW_GIGACHA")))
(unless (find-package "NEW_GIGACHA::PLANNING_INFO")
  (make-package "NEW_GIGACHA::PLANNING_INFO"))

(in-package "ROS")
;;//! \htmlinclude Planning_Info.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass new_gigacha::Planning_Info
  :super ros::object
  :slots (_mode _local _path_x _path_y _path_heading _path_local_x _path_local_y _point ))

(defmethod new_gigacha::Planning_Info
  (:init
   (&key
    ((:mode __mode) "")
    ((:local __local) (instance new_gigacha::Local :init))
    ((:path_x __path_x) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:path_y __path_y) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:path_heading __path_heading) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:path_local_x __path_local_x) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:path_local_y __path_local_y) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:point __point) (instance geometry_msgs::Point32 :init))
    )
   (send-super :init)
   (setq _mode (string __mode))
   (setq _local __local)
   (setq _path_x __path_x)
   (setq _path_y __path_y)
   (setq _path_heading __path_heading)
   (setq _path_local_x __path_local_x)
   (setq _path_local_y __path_local_y)
   (setq _point __point)
   self)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:local
   (&rest __local)
   (if (keywordp (car __local))
       (send* _local __local)
     (progn
       (if __local (setq _local (car __local)))
       _local)))
  (:path_x
   (&optional __path_x)
   (if __path_x (setq _path_x __path_x)) _path_x)
  (:path_y
   (&optional __path_y)
   (if __path_y (setq _path_y __path_y)) _path_y)
  (:path_heading
   (&optional __path_heading)
   (if __path_heading (setq _path_heading __path_heading)) _path_heading)
  (:path_local_x
   (&optional __path_local_x)
   (if __path_local_x (setq _path_local_x __path_local_x)) _path_local_x)
  (:path_local_y
   (&optional __path_local_y)
   (if __path_local_y (setq _path_local_y __path_local_y)) _path_local_y)
  (:point
   (&rest __point)
   (if (keywordp (car __point))
       (send* _point __point)
     (progn
       (if __point (setq _point (car __point)))
       _point)))
  (:serialization-length
   ()
   (+
    ;; string _mode
    4 (length _mode)
    ;; new_gigacha/Local _local
    (send _local :serialization-length)
    ;; float64[] _path_x
    (* 8    (length _path_x)) 4
    ;; float64[] _path_y
    (* 8    (length _path_y)) 4
    ;; float64[] _path_heading
    (* 8    (length _path_heading)) 4
    ;; float64[] _path_local_x
    (* 8    (length _path_local_x)) 4
    ;; float64[] _path_local_y
    (* 8    (length _path_local_y)) 4
    ;; geometry_msgs/Point32 _point
    (send _point :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _mode
       (write-long (length _mode) s) (princ _mode s)
     ;; new_gigacha/Local _local
       (send _local :serialize s)
     ;; float64[] _path_x
     (write-long (length _path_x) s)
     (dotimes (i (length _path_x))
       (sys::poke (elt _path_x i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _path_y
     (write-long (length _path_y) s)
     (dotimes (i (length _path_y))
       (sys::poke (elt _path_y i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _path_heading
     (write-long (length _path_heading) s)
     (dotimes (i (length _path_heading))
       (sys::poke (elt _path_heading i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _path_local_x
     (write-long (length _path_local_x) s)
     (dotimes (i (length _path_local_x))
       (sys::poke (elt _path_local_x i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _path_local_y
     (write-long (length _path_local_y) s)
     (dotimes (i (length _path_local_y))
       (sys::poke (elt _path_local_y i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; geometry_msgs/Point32 _point
       (send _point :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _mode
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _mode (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; new_gigacha/Local _local
     (send _local :deserialize buf ptr-) (incf ptr- (send _local :serialization-length))
   ;; float64[] _path_x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _path_x (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _path_x i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _path_y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _path_y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _path_y i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _path_heading
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _path_heading (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _path_heading i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _path_local_x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _path_local_x (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _path_local_x i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _path_local_y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _path_local_y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _path_local_y i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; geometry_msgs/Point32 _point
     (send _point :deserialize buf ptr-) (incf ptr- (send _point :serialization-length))
   ;;
   self)
  )

(setf (get new_gigacha::Planning_Info :md5sum-) "ca3fd13cb64cf71fd7e0db5debcdd949")
(setf (get new_gigacha::Planning_Info :datatype-) "new_gigacha/Planning_Info")
(setf (get new_gigacha::Planning_Info :definition-)
      "string mode
Local local
float64[] path_x
float64[] path_y
float64[] path_heading
float64[] path_local_x
float64[] path_local_y

geometry_msgs/Point32 point

================================================================================
MSG: new_gigacha/Local
float64 x
float64 y
float64 heading
================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
")



(provide :new_gigacha/Planning_Info "ca3fd13cb64cf71fd7e0db5debcdd949")


