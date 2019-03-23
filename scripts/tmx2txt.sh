#!/bin/sh

mkdir text

cat baekur.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/baekur.txt
cat biblian.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/biblian.txt
cat ees.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/ees.txt
cat ema.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="is">/<tuv xml:lang="is">/g' | sed 's/<tuv xml:lang="en"><seg>//g' | sed 's/<tuv xml:lang="is"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/ema.txt
cat eso.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/eso.txt
cat fornritin.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/fornritin.txt
cat hagstofan.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="is">/<tuv xml:lang="is">/g' | sed 's/<tuv xml:lang="en"><seg>//g' | sed 's/<tuv xml:lang="is"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/hagstofan.txt
cat kde4.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/kde4.txt
cat opensubtitles.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/opensubtitles.txt
cat tatoeba.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/tatoeba.txt
cat ubuntu.tmx | egrep "<tuv xml:lang=" | sed 's/^[ \t]*//;s/[ \t]*$//'  | sed ':r;$!{N;br};s/\n<tuv xml:lang="IS-IS">/<tuv xml:lang="IS-IS">/g' | sed 's/<tuv xml:lang="EN-GB"><seg>//g' | sed 's/<tuv xml:lang="IS-IS"><seg>//g' | sed 's|</seg></tuv>$||g' | sed 's|</seg></tuv>|\t|g' > text/ubuntu.txt

split -dl 50000 --additional-suffix=.txt text/ees.txt text/ees
rm text/ees.txt

split -dl 50000 --additional-suffix=.txt text/ema.txt text/ema
rm text/ema.txt

split -dl 50000 --additional-suffix=.txt text/opensubtitles.txt text/opensubtitles
rm text/opensubtitles.txt