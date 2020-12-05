#!/bin/bash
#!/bin/bash
directory=test_orig
find "${directory}" '!' -path "${directory}" -prune -type f -ls | awk '{s+=$7} END {printf "%.0f\n", s/NR}'