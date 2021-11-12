;; Auto-generated. Do not edit!


(when (boundp 'new_gigacha::Path)
  (if (not (find-package "NEW_GIGACHA"))
    (make-package "NEW_GIGACHA"))
  (shadow 'Path (find-package "NEW_GIGACHA")))
(unless (find-package "NEW_GIGACHA::PATH")
  (make-package "NEW_GIGACHA::PATH"))

(in-package "ROS")
;;//! \htmlinclude Path.msg.html


(defclass new_gigacha::Path
  :super ros::object
  :slots (_x _y _heading _k _env _mission ))

(defmethod new_gigacha::Path
  (:init
   (&key
    ((:x __x) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:y __y) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:heading __heading) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:k __k) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:env __env) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:mission __mission) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _x __x)
   (setq _y __y)
   (setq _heading __heading)
   (setq _k __k)
   (setq _env __env)
   (setq _mission __mission)
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
  (:k
   (&optional __k)
   (if __k (setq _k __k)) _k)
  (:env
   (&optional __env)
   (if __env (setq _env __env)) _env)
  (:mission
   (&optional __mission)
   (if __mission (setq _mission __mission)) _mission)
  (:serialization-length
   ()
   (+
    ;; float64[] _x
    (* 8    (length _x)) 4
    ;; float64[] _y
    (* 8    (length _y)) 4
    ;; float64[] _heading
    (* 8    (length _heading)) 4
    ;; float64[] _k
    (* 8    (length _k)) 4
    ;; string[] _env
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _env)) 4
    ;; string[] _mission
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _mission)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _x
     (write-long (length _x) s)
     (dotimes (i (length _x))
       (sys::poke (elt _x i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _y
     (write-long (length _y) s)
     (dotimes (i (length _y))
       (sys::poke (elt _y i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _heading
     (write-long (length _heading) s)
     (dotimes (i (length _heading))
       (sys::poke (elt _heading i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _k
     (write-long (length _k) s)
     (dotimes (i (length _k))
       (sys::poke (elt _k i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; string[] _env
     (write-long (length _env) s)
     (dolist (elem _env)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _mission
     (write-long (length _mission) s)
     (dolist (elem _mission)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _x (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _x i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _y i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _heading
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _heading (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _heading i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _k
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _k (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _k i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; string[] _env
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _env (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _env i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _mission
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _mission (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _mission i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get new_gigacha::Path :md5sum-) "0c0d921e9132160b23d521caaec99f12")
(setf (get new_gigacha::Path :datatype-) "new_gigacha/Path")
(setf (get new_gigacha::Path :definition-)
      "float64[] x
float64[] y
float64[] heading
float64[] k
string[] env
string[] mission
")



(provide :new_gigacha/Path "0c0d921e9132160b23d521caaec99f12")


