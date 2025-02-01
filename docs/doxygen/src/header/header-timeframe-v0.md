# TimeFrameHeader (v0)

Header for the time frame. In the version of 'v1, the frame contains the heartbeat delimiter if the type is META and the frame contains the time slice data.

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| magic | 64 | Magic number identifying the header |
| timeFrameId | 32 | Identifier for the time frame |
| numSource | 32 | Number of sources in the time frame |
| length | 64 | Total length of the time frame |

![Bit Field Diagram](svg/header-timeframe-v0.svg)
