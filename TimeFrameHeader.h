#ifndef TimeFrameHeader_h
#define TimeFrameHeader_h

#include <cstdint>
#include "version.h"

namespace TimeFrame {
   
// This format is temporary and should be updated.
#if VERSION_H == 0
   inline
#endif   
   namespace v0 {
// "DAEH-FT@" : little endian of "@TF-HEAD"
      constexpr uint64_t MAGIC {0x444145482d465440};
      struct Header {
         uint64_t magic       {MAGIC};
         uint32_t timeFrameId {0};
         uint32_t numSource   {0};
         uint64_t length      {0};
      };
      
   } // namespace v0
#if VERSION_H == 1
inline   
#endif
   namespace v1 {
      // " MRFEMIT" : little endian of "TIMEFRM "
      constexpr uint64_t MAGIC {0x004d5246454d4954};
      // TYPE 
      constexpr uint16_t META          {1};
      constexpr uint16_t SLICE         {2};
      constexpr uint16_t COMPLETE_TF   {0x00};
      constexpr uint16_t INCOMPLETE_TF {0x10};
      
      #pragma pack(4)
      struct Header {
         uint64_t magic       {MAGIC};
         uint32_t length      {0};
         uint16_t hLength     {24};
         uint16_t type        {0};
         uint32_t timeFrameId {0};
         uint32_t numSource   {0};
         

         void Print() {
            printf("TimeFrameHeader\n");
            printf("Length        = %d\n",length);
            printf("Header Lenght = %d\n",hLength);
            printf("Type          = %d\n",type);
            printf("timeframeid   = %d\n",timeFrameId);
            printf("numSource     = %d\n",numSource);
         }
      };
      #pragma pack()
   } // namespace v1
#if VERSION_H == 2
   inline 
#endif   
   namespace v2 {
      using v1::MAGIC;
      using v1::META;
      using v1::SLICE;         
      using v1::COMPLETE_TF;
      using v1::INCOMPLETE_TF;
      #pragma pack(4)
      struct Header : public v1::Header {
         Header () {
            hLength = sizeof(Header);
            magic = MAGIC | (2L << 56) ; // version 2 header
         }
         uint64_t elapsedTime; // elapsed time in microsecond
         uint64_t inDataSize; // incoming data size 
      }
      #pragma pack()
   }
   
} // namespace TimeFrame

#endif
