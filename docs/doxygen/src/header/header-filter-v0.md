# FilterHeader (v0)

Header for the output from Filter

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| magic | 64 | Magic number |
| length | 64 | Length |
| numTrigs | 32 | Number of triggers |
| workerId | 32 | Worker ID |
| elapseTime | 32 | Elapsed time |
| timeSec | 64 | Time in seconds |
| timeUSec | 64 | Time in microseconds |

![Bit Field Diagram](svg/header-filter-v0.svg)
