A simple script that can be used to determine how black images are from a given directory.

This is needed for example when converting Mr. Sid files to Tiff. That process results in a lot of files that are mostly black.

## Assumptions

This is a simple script right now, merge requests are welcomed.

1. You must pass in a single arg which is a full directory path, `/home/you/images/tiffs` for example.
1. The arg directory contains only tiff images, nothing else
1. The output is in the format of `{percent-confidence}TAB{filename-and-path}`

## Use

Get a list

    python main.py '/home/you/files/tiff'

    ## Example Output
    1.0     /home/marc_miles/1962/tiff/1962AP_10_09.tif
    0.46    /home/marc_miles/1962/tiff/1962AP_03_01.tif
    0.78    /home/marc_miles/1962/tiff/1962AP_03_10.tif
    0.08    /home/marc_miles/1962/tiff/1962AP_09_04.tif
    0.0     /home/marc_miles/1962/tiff/1962AP_04_03.tif
    0.18    /home/marc_miles/1962/tiff/1962AP_07_02.tif
    0.0     /home/marc_miles/1962/tiff/1962AP_02_05.tif
    0.0     /home/marc_miles/1962/tiff/1962AP_05_02.tif
    1.0     /home/marc_miles/1962/tiff/1962AP_10_10.tif

Pipe the results to sort.  This will list the highest % of nodata images at the bottom of the output.

    python main.py '/home/you/files/tiff' | sort -s -n -k 1,1

    ## Example Output
    0.89    /home/marc_miles/1962/tiff/1962AP_01_01.tif
    0.92    /home/marc_miles/1962/tiff/1962AP_05_10.tif
    0.96    /home/marc_miles/1962/tiff/1962AP_10_06.tif
    0.99    /home/marc_miles/1962/tiff/1962AP_06_10.tif
    1.0     /home/marc_miles/1962/tiff/1962AP_10_07.tif
    1.0     /home/marc_miles/1962/tiff/1962AP_09_10.tif
    1.0     /home/marc_miles/1962/tiff/1962AP_08_10.tif
    1.0     /home/marc_miles/1962/tiff/1962AP_10_08.tif
    1.0     /home/marc_miles/1962/tiff/1962AP_08_09.tif

Get just the ones that are 100% black `$1 = 1.0` and delete those files `$2` with `rm`.

    python main.py '/home/you/files/tiff' | awk '{ if ($1 == 1.0) { print $2} }' | xargs rm

## Tips

1. An image that is = 1.0 percent black can be deleted.
1. An image that is <= 0.93 percent black, probably has a small corner with legitimate imagery.
1. An image that is >= 0.97 percent black, is probably mostly black and can be deleted.
1. You may need to ignore these tips above and spot check for a % black comfort level for any given Mr. Sid conversion.
