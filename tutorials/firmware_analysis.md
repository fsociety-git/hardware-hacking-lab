# Firmware Analysis Tutorial

## Steps
1. Acquire firmware (e.g., from device update).
2. Use binwalk: binwalk firmware.bin
3. Extract: binwalk -e firmware.bin
4. Analyze filesystem: Explore extracted dirs for configs, binaries.
5. Reverse binaries: Use Ghidra or IDA for ELF files.

## Tools Needed
- Binwalk
- Ghidra (free reverse engineering tool)

Practice on samples/vulnerable_firmware.bin.
