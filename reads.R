#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)

data = read.table(args[1])

values = c()

for(i in 1:dim(data)[1]){
  values = c(values,data[i,1])
}


pdf("coverage.pdf")

barplot(values, ylim = c(0,200), main ="Coverage")

dev.off()