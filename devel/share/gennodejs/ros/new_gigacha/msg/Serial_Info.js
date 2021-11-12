// Auto-generated. Do not edit!

// (in-package new_gigacha.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Serial_Info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.auto_manual = null;
      this.emergency_stop = null;
      this.gear = null;
      this.speed = null;
      this.steer = null;
      this.brake = null;
      this.encoder = null;
    }
    else {
      if (initObj.hasOwnProperty('auto_manual')) {
        this.auto_manual = initObj.auto_manual
      }
      else {
        this.auto_manual = 0;
      }
      if (initObj.hasOwnProperty('emergency_stop')) {
        this.emergency_stop = initObj.emergency_stop
      }
      else {
        this.emergency_stop = 0;
      }
      if (initObj.hasOwnProperty('gear')) {
        this.gear = initObj.gear
      }
      else {
        this.gear = 0;
      }
      if (initObj.hasOwnProperty('speed')) {
        this.speed = initObj.speed
      }
      else {
        this.speed = 0.0;
      }
      if (initObj.hasOwnProperty('steer')) {
        this.steer = initObj.steer
      }
      else {
        this.steer = 0.0;
      }
      if (initObj.hasOwnProperty('brake')) {
        this.brake = initObj.brake
      }
      else {
        this.brake = 0;
      }
      if (initObj.hasOwnProperty('encoder')) {
        this.encoder = initObj.encoder
      }
      else {
        this.encoder = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Serial_Info
    // Serialize message field [auto_manual]
    bufferOffset = _serializer.int16(obj.auto_manual, buffer, bufferOffset);
    // Serialize message field [emergency_stop]
    bufferOffset = _serializer.int16(obj.emergency_stop, buffer, bufferOffset);
    // Serialize message field [gear]
    bufferOffset = _serializer.int16(obj.gear, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.float32(obj.speed, buffer, bufferOffset);
    // Serialize message field [steer]
    bufferOffset = _serializer.float32(obj.steer, buffer, bufferOffset);
    // Serialize message field [brake]
    bufferOffset = _serializer.int16(obj.brake, buffer, bufferOffset);
    // Serialize message field [encoder]
    bufferOffset = _serializer.float32(obj.encoder, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Serial_Info
    let len;
    let data = new Serial_Info(null);
    // Deserialize message field [auto_manual]
    data.auto_manual = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [emergency_stop]
    data.emergency_stop = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [gear]
    data.gear = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [steer]
    data.steer = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [brake]
    data.brake = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [encoder]
    data.encoder = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'new_gigacha/Serial_Info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f14c0811292ee3221e383efec3a1d50e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 auto_manual
    int16 emergency_stop
    int16 gear
    float32 speed
    float32 steer
    int16 brake
    float32 encoder
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Serial_Info(null);
    if (msg.auto_manual !== undefined) {
      resolved.auto_manual = msg.auto_manual;
    }
    else {
      resolved.auto_manual = 0
    }

    if (msg.emergency_stop !== undefined) {
      resolved.emergency_stop = msg.emergency_stop;
    }
    else {
      resolved.emergency_stop = 0
    }

    if (msg.gear !== undefined) {
      resolved.gear = msg.gear;
    }
    else {
      resolved.gear = 0
    }

    if (msg.speed !== undefined) {
      resolved.speed = msg.speed;
    }
    else {
      resolved.speed = 0.0
    }

    if (msg.steer !== undefined) {
      resolved.steer = msg.steer;
    }
    else {
      resolved.steer = 0.0
    }

    if (msg.brake !== undefined) {
      resolved.brake = msg.brake;
    }
    else {
      resolved.brake = 0
    }

    if (msg.encoder !== undefined) {
      resolved.encoder = msg.encoder;
    }
    else {
      resolved.encoder = 0.0
    }

    return resolved;
    }
};

module.exports = Serial_Info;
