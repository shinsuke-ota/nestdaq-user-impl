# SubTimeFrameHeader (v1)

Header for the sub-time frame

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| version | 8 | Version |
| magic | 56 | Magic number |
| length | 32 | Length (in bytes) |
| headerLength | 16 | Header length (in bytes) |
| type | 16 | type of the structure (1: META) |
| timeFrameId | 32 | Time frame ID |
| femType | 32 | FEM type (1: L_V1, 2: H / H_V1, 3: L/L_V2, 5: H_V3, 6: LV3) |
| femId | 32 | FEM ID (currently IP address of modules) |
| numMessages | 32 | Number of messages |
| timeSec | 64 | Time in seconds |
| timeUSec | 64 | Time in microseconds |

![Bit Field Diagram](svg/header-subtimeframe-v1.svg)
