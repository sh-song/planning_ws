// Generated by gencpp from file new_gigacha/Local.msg
// DO NOT EDIT!


#ifndef NEW_GIGACHA_MESSAGE_LOCAL_H
#define NEW_GIGACHA_MESSAGE_LOCAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace new_gigacha
{
template <class ContainerAllocator>
struct Local_
{
  typedef Local_<ContainerAllocator> Type;

  Local_()
    : x(0.0)
    , y(0.0)
    , heading(0.0)  {
    }
  Local_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , heading(0.0)  {
  (void)_alloc;
    }



   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef double _heading_type;
  _heading_type heading;





  typedef boost::shared_ptr< ::new_gigacha::Local_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::new_gigacha::Local_<ContainerAllocator> const> ConstPtr;

}; // struct Local_

typedef ::new_gigacha::Local_<std::allocator<void> > Local;

typedef boost::shared_ptr< ::new_gigacha::Local > LocalPtr;
typedef boost::shared_ptr< ::new_gigacha::Local const> LocalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::new_gigacha::Local_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::new_gigacha::Local_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::new_gigacha::Local_<ContainerAllocator1> & lhs, const ::new_gigacha::Local_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.heading == rhs.heading;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::new_gigacha::Local_<ContainerAllocator1> & lhs, const ::new_gigacha::Local_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace new_gigacha

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::new_gigacha::Local_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::new_gigacha::Local_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::new_gigacha::Local_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::new_gigacha::Local_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::new_gigacha::Local_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::new_gigacha::Local_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::new_gigacha::Local_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bc1dd36b5547fef69e6daa06ae2e13ac";
  }

  static const char* value(const ::new_gigacha::Local_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbc1dd36b5547fef6ULL;
  static const uint64_t static_value2 = 0x9e6daa06ae2e13acULL;
};

template<class ContainerAllocator>
struct DataType< ::new_gigacha::Local_<ContainerAllocator> >
{
  static const char* value()
  {
    return "new_gigacha/Local";
  }

  static const char* value(const ::new_gigacha::Local_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::new_gigacha::Local_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 x\n"
"float64 y\n"
"float64 heading\n"
;
  }

  static const char* value(const ::new_gigacha::Local_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::new_gigacha::Local_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.heading);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Local_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::new_gigacha::Local_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::new_gigacha::Local_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "heading: ";
    Printer<double>::stream(s, indent + "  ", v.heading);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NEW_GIGACHA_MESSAGE_LOCAL_H