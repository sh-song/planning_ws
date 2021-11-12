; Auto-generated. Do not edit!


(cl:in-package new_gigacha-msg)


;//! \htmlinclude Control_Info.msg.html

(cl:defclass <Control_Info> (roslisp-msg-protocol:ros-message)
  ((emergency_stop
    :reader emergency_stop
    :initarg :emergency_stop
    :type cl:fixnum
    :initform 0)
   (gear
    :reader gear
    :initarg :gear
    :type cl:fixnum
    :initform 0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0)
   (steer
    :reader steer
    :initarg :steer
    :type cl:float
    :initform 0.0)
   (brake
    :reader brake
    :initarg :brake
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Control_Info (<Control_Info>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Control_Info>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Control_Info)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name new_gigacha-msg:<Control_Info> is deprecated: use new_gigacha-msg:Control_Info instead.")))

(cl:ensure-generic-function 'emergency_stop-val :lambda-list '(m))
(cl:defmethod emergency_stop-val ((m <Control_Info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader new_gigacha-msg:emergency_stop-val is deprecated.  Use new_gigacha-msg:emergency_stop instead.")
  (emergency_stop m))

(cl:ensure-generic-function 'gear-val :lambda-list '(m))
(cl:defmethod gear-val ((m <Control_Info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader new_gigacha-msg:gear-val is deprecated.  Use new_gigacha-msg:gear instead.")
  (gear m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <Control_Info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader new_gigacha-msg:speed-val is deprecated.  Use new_gigacha-msg:speed instead.")
  (speed m))

(cl:ensure-generic-function 'steer-val :lambda-list '(m))
(cl:defmethod steer-val ((m <Control_Info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader new_gigacha-msg:steer-val is deprecated.  Use new_gigacha-msg:steer instead.")
  (steer m))

(cl:ensure-generic-function 'brake-val :lambda-list '(m))
(cl:defmethod brake-val ((m <Control_Info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader new_gigacha-msg:brake-val is deprecated.  Use new_gigacha-msg:brake instead.")
  (brake m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Control_Info>) ostream)
  "Serializes a message object of type '<Control_Info>"
  (cl:let* ((signed (cl:slot-value msg 'emergency_stop)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'gear)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'steer))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'brake)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Control_Info>) istream)
  "Deserializes a message object of type '<Control_Info>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'emergency_stop) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gear) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'steer) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'brake) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Control_Info>)))
  "Returns string type for a message object of type '<Control_Info>"
  "new_gigacha/Control_Info")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Control_Info)))
  "Returns string type for a message object of type 'Control_Info"
  "new_gigacha/Control_Info")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Control_Info>)))
  "Returns md5sum for a message object of type '<Control_Info>"
  "3dc9a678baa6090d119c5483385b8223")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Control_Info)))
  "Returns md5sum for a message object of type 'Control_Info"
  "3dc9a678baa6090d119c5483385b8223")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Control_Info>)))
  "Returns full string definition for message of type '<Control_Info>"
  (cl:format cl:nil "int16 emergency_stop~%int16 gear~%float32 speed~%float32 steer~%int16 brake~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Control_Info)))
  "Returns full string definition for message of type 'Control_Info"
  (cl:format cl:nil "int16 emergency_stop~%int16 gear~%float32 speed~%float32 steer~%int16 brake~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Control_Info>))
  (cl:+ 0
     2
     2
     4
     4
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Control_Info>))
  "Converts a ROS message object to a list"
  (cl:list 'Control_Info
    (cl:cons ':emergency_stop (emergency_stop msg))
    (cl:cons ':gear (gear msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':steer (steer msg))
    (cl:cons ':brake (brake msg))
))
