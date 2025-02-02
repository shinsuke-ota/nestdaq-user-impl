#ifndef FilterHeader_h
#define FilterHeader_h

#include <cstdint>
#include <sys/time.h>

#include "version.h"

namespace Filter {
    #if VERSION_H == 0
    inline 
    #endif
    namespace v0 {

// "NIOC-TLF" : little endian of "FLT-COIN"
constexpr uint64_t MAGIC {0x4e494f43'2d544c46};

struct Header {
    uint64_t magic       {MAGIC};
    uint64_t length      {0};
    uint32_t numTrigs    {0};
    uint32_t workerId    {0};
    uint32_t elapseTime  {0};
    //struct timeval processTime {0, 0};
    uint64_t timeSec     {0};
    uint64_t timeUSec    {0};
};
} //namespace v0
    #if VERSION_H == 1
    inline 
    #endif
    namespace v1 {
#pragma pack(4)

// " IGOLTLF" : little endian of "FLTLOGI "
static constexpr uint64_t MAGIC {0x0049474f'4c544c46};

struct Header {
    uint64_t magic       {MAGIC};
    uint32_t length      {0};
    uint16_t hLength     {56};
    uint16_t type        {0};
    uint32_t timeFrameId {0};
    uint32_t numTrigs    {0};
    uint32_t workerId    {0};
    uint32_t numMessages {0};
    uint32_t elapsedTime  {0};
    uint32_t reserve     {0xff00ff00};
    //struct timeval processTime {0, 0};
    uint64_t timeSec     {0};
    uint64_t timeUSec    {0};
};

// " EMITGRT"
static constexpr uint64_t TDC_MAGIC {0x00454d49'54475254};
struct TrgTimeHeader {
    union {
        uint32_t u32data[4];
        struct {
            uint64_t magic       {TDC_MAGIC};
            uint32_t length      {0};
            uint16_t hLength     {16};
            uint16_t type        {0};
            //uint32_t timeFrameId {0};
        };
    };
};

constexpr unsigned char FLT_TDC_TYPE {0xaa};
struct TrgTime {
    union {
        struct {
            uint32_t time;
            uint32_t type;
        };
        unsigned char cdata[8]  {0, 0, 0, 0, 0, 0, 0, FLT_TDC_TYPE};
    };
};

#pragma pack()
} //namespace v1

#if VERSION_H == 2
inline
#endif
namespace v2 {
#pragma pack(4)
struct Header : public v1::Header {
    Header () {
        hLength = sizeof(Header);
        magic = v1::MAGIC | (2L << 56) ; // version 2 header
    }
    uint64_t elapsedTime; // elapsed time in microsecond
    uint64_t inDataSize; // incoming data size 
};
using v1::TrgTime;
using v1::TrgTimeHeader;

#pragma pack()
} //namespace v2

} // namespace Filter

#endif
