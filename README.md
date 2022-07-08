# Mongo-Analyzer
## Prerequirements
- Install keyhole from here : [link](https://www.simagix.com/2021/02/build-and-download-keyhole_7.html)
- Install python packages : pandas, matplotlib, numpy, imageio, PIL, glob, os, PyPDF2

To run the script, use this command `bash pr.sh <your_FTDC_file_path>`

After the scripts run, open Final.pdf and it will be all you need to analyze FTDC - logs

## A guide to read Final.pdf


**Wired Tiger Tickets**: First check if any tickets dropped to zero.
 
If the server ran out of read tickets, check MongoDB logs for long-running database operations. To resolve the running-out-read-tickets problem, solutions can be as simple as adding indexes to improve query performance and free up read tickets quicker. If all queries are supported by proper indexes, but the problems are due to high transaction rate of read operations, consider adding more shards to the MongoDB cluster.

If the server was out of write tickets, the problem is likely disk performance-related, high disk latency or under-provisioned IOPS. Cross-reference the Disk IOPS and Disk Utilization (%) panels to see if it reached the maximum disk IOPS.

**IOPS**: If the IOPS of a disk device is showing as a plateau line, it’s very likely that the device has reached its maximum provisioned IOPS. The solution is to increase disk IOPS.

**Wired Tiger Cache**: Growing amounts of dirty data usually implies that the rate of writing to the database overwhelms the provisioned disk IOPS
