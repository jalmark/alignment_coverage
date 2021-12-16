#!/usr/bin/env Rscript

# Jalmari Kettunen 16.12.2021
# This R script visualizes virus genome alignment.
# For direct use, input data file must be given as a argument in command line. 
# Usage example:
# R --args "NC_024771_in_SRR1073679_virosaurus90Human_sortedMAPQ10.txt"
# > source("reads.R")

# Input data file should be created with script 'extractHeaders.sh'.

args = commandArgs(trailingOnly=TRUE)

simpleName = gsub(".txt", "", args[1])

data = read.table(args[1])

values = c()

for(i in 1:dim(data)[1]){
  values = c(values,data[i,1])
}


pdf(paste0(simpleName, ".pdf"))

barplot( values, ylim = c(0,200), main = paste("Coverage:",simpleName) )

dev.off()