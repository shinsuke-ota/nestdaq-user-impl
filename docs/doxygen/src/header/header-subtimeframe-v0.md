# SubTimeFrameHeader (v0)

Header for the sub-time frame

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| magic | 64 | Magic number |
| timeFrameId | 32 | Time frame ID |
| reserved | 32 | Reserved |
| femType | 32 | FEM type (1: L_V1, 2: H / H_V1, 3: L/L_V2, 5: H_V3, 6: LV3) |
| femId | 32 | FEM ID (currently IP address of modules) |
| length | 32 | Length |
| numMessages | 32 | Number of messages |
| timeSec | 64 | Time in seconds |
| timeUSec | 64 | Time in microseconds |

![Bit Field Diagram](svg/header-subtimeframe-v0.svg)
