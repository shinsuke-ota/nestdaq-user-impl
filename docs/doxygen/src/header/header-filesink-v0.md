# FileSinkHeader (v0)

Header for the output from FileSink

| Property Name | Bit Length | Description |
|---------------|------------|-------------|
| magic | 64 | Magic number |
| size | 64 | Size |
| fairMQDeviceType | 64 | FairMQ device type |
| runNumber | 64 | Run number |
| startUnixTime | 64 | Start Unix time |
| stopUnixTime | 64 | Stop Unix time |
| comments | 64 | Comments .. (256 characters)  |

![Bit Field Diagram](svg/header-filesink-v0.svg)
