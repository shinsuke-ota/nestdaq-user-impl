# FilterHeader (v1)

Header for the output from Filter

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| version | 8 | Version |
| magic | 56 | Magic number |
| length | 32 | Length (in bytes) |
| headerLength | 16 | Header length (in bytes) |
| type | 16 | Type |
| timeFrameId | 32 | Time frame ID |
| numTrigs | 32 | Number of triggers |
| workerId | 32 | Worker ID |
| numMessages | 32 | Number of messages |
| elapseTime | 32 | Elapsed time |
| reserve | 32 | Reserve |
| timeSec | 64 | Time in seconds |
| timeUSec | 64 | Time in microseconds |

![Bit Field Diagram](svg/header-filter-v1.svg)
