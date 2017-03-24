#!/bin/bash

for i in `seq 1 1 \`pdfinfo main.pdf | grep 'Pages' | cut -d: -f2 | sed -e 's/ //g'\``
do
        echo Page $i;
        pdffonts -f $i -l $i main.pdf|grep 'Type 3';
done
exit

