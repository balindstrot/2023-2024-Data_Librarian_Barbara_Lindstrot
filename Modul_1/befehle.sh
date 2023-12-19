sed -e '/^#/d' -e '/IMPOTANT/d' 2023-11-20-Article_list_dirty.txt | cut -f5,12 2023-11-20-Article_list_dirty.txt | sed -e '/^\s/d' -e '/eng/d' -e '/^#/d' -e '/ISSN:/d' -e '/issn:\s/d' -e '/Issn:\s*/d' | sort -n | uniq > 2023-11-20-Dates_and_ISSNs.tsv

