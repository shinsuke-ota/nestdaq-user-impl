# TimeFrameHeader (v1)

Header for the time frame. In the version of 'v1, the frame contains the heartbeat delimiter if the type is META and the frame contains the time slice data.

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| version | 8 | Version |
| magic | 56 | Magic number |
| length | 32 | Length (in bytes) |
| hLength | 16 | Header length (in bytes) |
| type | 16 | Type of the time frame (0: META, 1: SLICE) |
| timeFrameId | 32 | Identifier for the time frame |
| numSource | 32 | Number of sources in the time frame |

![Bit Field Diagram](png/header-timeframe-v1.png)
