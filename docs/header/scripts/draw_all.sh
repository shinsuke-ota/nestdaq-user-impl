#/bin/sh

python3 draw_bit_field.py ../schema/header-filesink.json --version v0 --output ../../doxygen/src/header
python3 draw_bit_field.py ../schema/header-filesink.json --version v1 --output ../../doxygen/src/header

python3 draw_bit_field.py ../schema/header-subtimeframe.json --version v0 --output ../../doxygen/src/header
python3 draw_bit_field.py ../schema/header-subtimeframe.json --version v1 --output ../../doxygen/src/header

python3 draw_bit_field.py ../schema/header-timeframe.json --version v0 --output ../../doxygen/src/header
python3 draw_bit_field.py ../schema/header-timeframe.json --version v1 --output ../../doxygen/src/header

python3 draw_bit_field.py ../schema/header-filter.json --version v0 --output ../../doxygen/src/header
python3 draw_bit_field.py ../schema/header-filter.json --version v1 --output ../../doxygen/src/header

python3 draw_bit_field.py ../schema/header-heartbeatframe.json --output ../../doxygen/src/header

python3 draw_bit_field.py ../schema/header-triggertime.json --output ../../doxygen/src/header
