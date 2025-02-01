# FileSinkHeader (v1)

Header for the output from FileSink

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| version | 8 | Version |
| magic | 56 | Magic number |
| length | 32 | Length (in bytes) |
| headerLength | 16 | Header length (in bytes) |
| type | 16 | Type |
| fairMQDeviceType | 64 | FairMQ device type |
| runNumber | 64 | Run number |
| startUnixTime | 64 | Start Unix time |
| stopUnixTime | 64 | Stop Unix time |
| comments | 64 | Comments .. (256 characters)  |

![Bit Field Diagram](svg/header-filesink-v1.svg)
