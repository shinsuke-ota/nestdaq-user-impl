#ifndef SubTimeFrameHeader_h
#define SubTimeFrameHeader_h

#include <cstdint>

#include "version.h"

namespace SubTimeFrame {

// This format is temporary and should be updated.
# if VERSION_H == 0
inline
#endif
namespace v0 {

// "DAEH-FTS" : little endian of "STF-HEAD"
constexpr uint64_t MAGIC  {0x444145482d465453};
//constexpr uint32_t TDC64H {0x48434454};
//constexpr uint32_t TDC64L {0x4c434454};
constexpr uint32_t TDC64H    {2};
constexpr uint32_t TDC64H_V1 {2};
constexpr uint32_t TDC64L    {3};
constexpr uint32_t TDC64L_V1 {1};
constexpr uint32_t TDC64L_V2 {3};
constexpr uint32_t TDC64H_V3 {5};
constexpr uint32_t TDC64L_V3 {6};

constexpr uint32_t FLT_TDC   {0x0000'1000};
constexpr uint32_t NULDEV    {0};

struct Header {
    uint64_t magic        {MAGIC};
    uint32_t timeFrameId  {0}; 
    uint32_t reserved     {0};
    uint32_t femType      {0};
    uint32_t femId        {0};
    uint32_t length       {0};
    uint32_t numMessages  {0};
    uint64_t timeSec     {0};
    uint64_t timeUSec    {0};
};

} // namespace v0

# if VERSION_H == 1
inline
#endif
namespace v1 {

// " EMITBUS" : little endian of "SUBTIME "
constexpr uint64_t MAGIC  {0x00454d4954425553};
constexpr uint32_t TDC64H    {2};
constexpr uint32_t TDC64H_V1 {2};
constexpr uint32_t TDC64L    {3};
constexpr uint32_t TDC64L_V1 {1};
constexpr uint32_t TDC64L_V2 {3};
//constexpr uint32_t TDC64H_V3 {4};
//constexpr uint32_t TDC64L_V3 {5};
constexpr uint32_t TDC64H_V3 {5};
constexpr uint32_t TDC64L_V3 {6};
constexpr uint32_t INPUT_REG {21};
constexpr uint32_t FLT_TDC   {0x0000'1000};

constexpr uint32_t NULDEV    {0};

constexpr uint16_t META {1};

struct Header {
    uint64_t magic        {MAGIC};
    uint32_t length       {0};
    uint16_t hLength      {48};
    uint16_t type         {0};
    uint32_t timeFrameId  {0};
    uint32_t femType      {0};
    uint32_t femId        {0};
    uint32_t numMessages  {0};
    uint64_t timeSec     {0};
    uint64_t timeUSec    {0};
};  

} // namespace v1

# if VERSION_H == 2
inline
#endif
namespace v2 {
    using v1::MAGIC;
    using v1::TDC64H;
    using v1::TDC64H_V1;
    using v1::TDC64L;
    using v1::TDC64L_V1;
    using v1::TDC64L_V2;
    using v1::TDC64H_V3;
    using v1::TDC64L_V3;
    using v1::INPUT_REG;
    using v1::FLT_TDC;
    using v1::NULDEV;
    using v1::META;
    #pragma pack(4)
      struct Header : public v1::Header {
        Header () {
            hLength = sizeof(Header);
            magic = MAGIC | (2L << 56) ; // version 2 header
        }
        uint64_t elapsedTime{0}; // elapsed time in microsecond
        uint64_t inDataSize{0}; // incoming data size 
      };
    #pragma pack()
} // namespace v2

} // namespace SubTimeFrame

#endif
