# HeartbeatFrameHeader

Header for the heartbeat frame

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| version | 8 | Version |
| magic | 56 | Magic number |
| length | 32 | Length (in bytes) |
| headerLength | 16 | Header length (in bytes) |
| type | 16 | Type |

![Bit Field Diagram](svg/header-heartbeatframe.svg)
