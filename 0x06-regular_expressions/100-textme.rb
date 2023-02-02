#!/usr/bin/env ruby
# Your script should output: [SENDER],[RECEIVER],[FLAGS]
#+ The sender phone number or name (including country code if present)
#+ The receiver phone number or name (including country code if present)
#+ The flags that were used

str = ARGV[0]
scan_o = str.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
get = scan_o.join(",")
puts get
