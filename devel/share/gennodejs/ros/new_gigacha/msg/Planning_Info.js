// Auto-generated. Do not edit!

// (in-package new_gigacha.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Local = require('./Local.js');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class Planning_Info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.mode = null;
      this.local = null;
      this.index = null;
      this.path_x = null;
      this.path_y = null;
      this.path_heading = null;
      this.path_local_x = null;
      this.path_local_y = null;
      this.point = null;
    }
    else {
      if (initObj.hasOwnProperty('mode')) {
        this.mode = initObj.mode
      }
      else {
        this.mode = '';
      }
      if (initObj.hasOwnProperty('local')) {
        this.local = initObj.local
      }
      else {
        this.local = new Local();
      }
      if (initObj.hasOwnProperty('index')) {
        this.index = initObj.index
      }
      else {
        this.index = 0;
      }
      if (initObj.hasOwnProperty('path_x')) {
        this.path_x = initObj.path_x
      }
      else {
        this.path_x = [];
      }
      if (initObj.hasOwnProperty('path_y')) {
        this.path_y = initObj.path_y
      }
      else {
        this.path_y = [];
      }
      if (initObj.hasOwnProperty('path_heading')) {
        this.path_heading = initObj.path_heading
      }
      else {
        this.path_heading = [];
      }
      if (initObj.hasOwnProperty('path_local_x')) {
        this.path_local_x = initObj.path_local_x
      }
      else {
        this.path_local_x = [];
      }
      if (initObj.hasOwnProperty('path_local_y')) {
        this.path_local_y = initObj.path_local_y
      }
      else {
        this.path_local_y = [];
      }
      if (initObj.hasOwnProperty('point')) {
        this.point = initObj.point
      }
      else {
        this.point = new geometry_msgs.msg.Point32();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Planning_Info
    // Serialize message field [mode]
    bufferOffset = _serializer.string(obj.mode, buffer, bufferOffset);
    // Serialize message field [local]
    bufferOffset = Local.serialize(obj.local, buffer, bufferOffset);
    // Serialize message field [index]
    bufferOffset = _serializer.int16(obj.index, buffer, bufferOffset);
    // Serialize message field [path_x]
    bufferOffset = _arraySerializer.float64(obj.path_x, buffer, bufferOffset, null);
    // Serialize message field [path_y]
    bufferOffset = _arraySerializer.float64(obj.path_y, buffer, bufferOffset, null);
    // Serialize message field [path_heading]
    bufferOffset = _arraySerializer.float64(obj.path_heading, buffer, bufferOffset, null);
    // Serialize message field [path_local_x]
    bufferOffset = _arraySerializer.float64(obj.path_local_x, buffer, bufferOffset, null);
    // Serialize message field [path_local_y]
    bufferOffset = _arraySerializer.float64(obj.path_local_y, buffer, bufferOffset, null);
    // Serialize message field [point]
    bufferOffset = geometry_msgs.msg.Point32.serialize(obj.point, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Planning_Info
    let len;
    let data = new Planning_Info(null);
    // Deserialize message field [mode]
    data.mode = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [local]
    data.local = Local.deserialize(buffer, bufferOffset);
    // Deserialize message field [index]
    data.index = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [path_x]
    data.path_x = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [path_y]
    data.path_y = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [path_heading]
    data.path_heading = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [path_local_x]
    data.path_local_x = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [path_local_y]
    data.path_local_y = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [point]
    data.point = geometry_msgs.msg.Point32.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.mode);
    length += Local.getMessageSize(object.local);
    length += 8 * object.path_x.length;
    length += 8 * object.path_y.length;
    length += 8 * object.path_heading.length;
    length += 8 * object.path_local_x.length;
    length += 8 * object.path_local_y.length;
    return length + 38;
  }

  static datatype() {
    // Returns string type for a message object
    return 'new_gigacha/Planning_Info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c4d20caaea3ca6d27e075a2a5f2e1296';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string mode
    Local local
    int16 index
    float64[] path_x
    float64[] path_y
    float64[] path_heading
    float64[] path_local_x
    float64[] path_local_y
    
    geometry_msgs/Point32 point
    
    ================================================================================
    MSG: new_gigacha/Local
    Header header
    
    float64 x
    float64 y
    float64 heading
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Planning_Info(null);
    if (msg.mode !== undefined) {
      resolved.mode = msg.mode;
    }
    else {
      resolved.mode = ''
    }

    if (msg.local !== undefined) {
      resolved.local = Local.Resolve(msg.local)
    }
    else {
      resolved.local = new Local()
    }

    if (msg.index !== undefined) {
      resolved.index = msg.index;
    }
    else {
      resolved.index = 0
    }

    if (msg.path_x !== undefined) {
      resolved.path_x = msg.path_x;
    }
    else {
      resolved.path_x = []
    }

    if (msg.path_y !== undefined) {
      resolved.path_y = msg.path_y;
    }
    else {
      resolved.path_y = []
    }

    if (msg.path_heading !== undefined) {
      resolved.path_heading = msg.path_heading;
    }
    else {
      resolved.path_heading = []
    }

    if (msg.path_local_x !== undefined) {
      resolved.path_local_x = msg.path_local_x;
    }
    else {
      resolved.path_local_x = []
    }

    if (msg.path_local_y !== undefined) {
      resolved.path_local_y = msg.path_local_y;
    }
    else {
      resolved.path_local_y = []
    }

    if (msg.point !== undefined) {
      resolved.point = geometry_msgs.msg.Point32.Resolve(msg.point)
    }
    else {
      resolved.point = new geometry_msgs.msg.Point32()
    }

    return resolved;
    }
};

module.exports = Planning_Info;
